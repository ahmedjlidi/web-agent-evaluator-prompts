from pathlib import Path
import json,hashlib,re
root=Path(__file__).resolve().parents[1]
index=json.loads((root/'prompt_index.json').read_text())
assert set(range(1,48))=={x['appendix_prompt'] for x in index['prompts'] if x['appendix_prompt']}
for item in index['prompts']:
    assert hashlib.sha256((root/item['path']).read_bytes()).hexdigest()==item['sha256'],item['path']
for path in root.rglob('*.md'):
    for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',path.read_text()):
        if not re.match(r'^[a-z]+:',target) and not target.startswith('#'):
            assert (path.parent/target.split('#')[0]).exists(),(path,target)
print('Validated prompt hashes, appendix boxes 1–47, and local Markdown links.')
