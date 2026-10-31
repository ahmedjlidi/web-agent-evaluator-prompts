"""Archived message construction snippets; supporting helpers come from the cited original runner.
This file documents assembly and is not a standalone evaluation runner.
"""

def render_evidence(records):
    if [r['pair_index'] for r in records] != list(range(len(records))):
        raise ValueError('Step evidence is missing, duplicated or out of order.')
    # The paper does not specify a renderer. Pin this simple chronological serialization.
    return '\n\n'.join(f"Step {r['pair_index']+1}:\n{r['parsed']['model_text']}" for r in records)
