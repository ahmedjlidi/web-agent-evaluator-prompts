"""Archived message construction snippets; supporting helpers come from the cited original runner.
This file documents assembly and is not a standalone evaluation runner.
"""

def independent_messages(task, initial_screenshot_path, task_image_paths=()):
    """Only the task, objective images and first recorded state enter the model request."""
    if not isinstance(task, str) or not task.strip():
        raise StageError('inputs', 'Original task is missing or empty.')
    content = [{'type': 'text', 'text': '## OBJECTIVE: ' + task}]
    for i, path in enumerate(task_image_paths):
        content.extend([{'type': 'text', 'text': f'## IMAGES: Image {i}: task objective image'}, image_part(path)])
    content.extend([{'type': 'text', 'text': 'Initial webpage screenshot:'}, image_part(initial_screenshot_path),
                    {'type': 'text', 'text': FIRST_REQUEST}])
    return [{'role': 'system', 'content': FIRST_SYSTEM}, {'role': 'user', 'content': content}]
