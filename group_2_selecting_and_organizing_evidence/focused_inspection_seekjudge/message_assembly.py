"""Archived message construction snippets; supporting helpers come from the cited original runner.
This file documents assembly and is not a standalone evaluation runner.
"""

def observation_content(obs,limit,use_a11y=True,image_override=None):
    parts=[image_part(image_override or obs['local_path'])]
    text=obs['a11y'] if use_a11y else None
    if text:
        parts.append({'type':'text','text':'\n\nA11y tree:'})
        parts.append({'type':'text','text':text[:limit]+('[truncated]' if len(text)>limit else '')})
    else:parts.append({'type':'text','text':'\n\nA11y tree: Not Given.'})
    return parts

def condense_messages(before,after,annotated,cfg):
    parts=[text_part('Here are the two observations to analyze:'),text_part('\n\nIMG1 (earlier state):')]
    if annotated:
        parts.append(text_part('The red circle in IMG1 marks where the action was performed. Focus on describing what changed in that area.'))
    parts+=observation_content(before,cfg.condense_a11y_chars,cfg.use_a11y,annotated)
    parts.append(text_part('\n\nIMG2 (later state):'))
    parts+=observation_content(after,cfg.condense_a11y_chars,cfg.use_a11y)
    parts.append(text_part('\n\nPlease analyze the visual changes between these two observations.'))
    return [{'role':'system','content':PUBLISHED['CONDENSE_AGENT_PROMPT']},{'role':'user','content':parts}]

def ground_messages(obs,action,annotated,cfg):
    if annotated:
        parts=[text_part('Here is the observation with a RED CIRCLE marking the action location:'),
            text_part('\n\nIMG1:'),image_part(annotated),text_part('\n\nACTION performed at the red circle location:'),
            text_part(action),text_part('\n\nPlease identify the UI element at the red circle and output in function call format.')]
        prompt=PUBLISHED['CONDENSE_ACTION_VL_PROMPT']
    else:
        parts=[text_part('Here is the observation to analyze:'),text_part('\n\nIMG1:')]
        parts+=observation_content(obs,cfg.ground_a11y_chars,cfg.use_a11y)
        parts += [text_part('\n\nACTION to be performed on IMG1:'),text_part(action),
            text_part('\n\nPlease identify what UI element is being interacted with.')]
        prompt=PUBLISHED['CONDENSE_ACTION_PROMPT']
    return [{'role':'system','content':prompt},{'role':'user','content':parts}]

def analyse_messages(obs,query,cfg):
    parts=[text_part(f'QUERY: {query}'),text_part('\n\nObservation data follows (scan ALL of it for matches):\n')]
    parts+=observation_content(obs,cfg.analyse_a11y_chars,cfg.use_a11y)
    parts.append(text_part(f'\n\nREMINDER — answer this query using ALL matching data from above.\nQUERY: {query}'))
    return [{'role':'system','content':PUBLISHED['ANALYSIS_AGENT_PROMPT']},{'role':'user','content':parts}]

def goal_image_messages(path):
    return [{'role':'user','content':[image_part(path),text_part(PUBLISHED['DESCRIBE_IMAGE_PROMPT'].strip())]}]

def actor_claim(raw):
    responses=[step.get('action') or 'None' for step in raw['steps']]
    patterns=('report_infeasible','send_msg_to_user','computer.terminate(status','finished(')
    for index in (-1,-2):
        if len(responses)>=abs(index) and any(p in responses[index] for p in patterns):
            return {'text':responses[index],'source_state_index':len(responses)+index,'origin':'recorded_terminal_action'}
    return {'text':'The trajectory reached the goal.','source_state_index':None,'origin':'upstream_default_unverified_hypothesis'}

def initial_seek_messages(goal,claim,summaries,num_images):
    content=[text_part(f'GOAL: {goal}'),text_part(f"UNVERIFIED_CLAIM: {claim['text']}"),
        text_part(f'TRAJECTORY_INFO: The trajectory has {num_images} images, indexed from 0 to {num_images-1}.'),
        text_part('STATE_SUMMARIES:')]
    content += [text_part(f'Transition {i+1} (img{i} -> img{i+1}):\n{summary}') for i,summary in enumerate(summaries)]
    content.append(text_part('Please analyze this trajectory and provide your evaluation following the format specified in the system prompt (Reasoning and Sub-metrics).'))
    return [{'role':'system','content':PUBLISHED['HOLISTIC_SYSTEM_PROMPT']},{'role':'user','content':content}]

def evidence_history(goal_descriptions,claim,summaries,inspections,budget):
    # No raw actor thoughts or Seek interpretations are reintroduced to the final judge.
    parts=['Evaluator-generated evidence (not the actor reasoning):']
    if goal_descriptions:
        parts.append('Task reference-image descriptions:\n'+ '\n'.join(f"Image {i+1}: {d['description']}" for i,d in enumerate(goal_descriptions)))
    parts.append('Unverified terminal claim / hypothesis ('+claim['origin']+'):\n'+claim['text'])
    parts += [f'Transition {i+1} (img{i} -> img{i+1}):\n{s}' for i,s in enumerate(summaries)]
    parts.append('Focused observations returned by AnalyseAgent:')
    for i,entry in enumerate(inspections):
        if entry.get('answer') is not None:
            parts.append(f"Inspection {i+1}; img_id={entry['img_id']}; query={entry['query']}\n{entry['answer']}")
    parts.append('Inspection-budget diagnostic: '+json.dumps(budget,ensure_ascii=False)+
        '. A budget limit is not evidence that the actor failed.')
    return '\n\n'.join(parts)

def binary_messages(raw,goal_descriptions,claim,summaries,inspections,budget,final_image):
    history=evidence_history(goal_descriptions,claim,summaries,inspections,budget)
    user=VANILLA_REFERENCE['user_template'].format(intent=raw['goal'],last_actions=history)
    return [{'role':'system','content':VANILLA_REFERENCE['system_prompt']},
        {'role':'user','content':[text_part(user),image_part(final_image)]}]
