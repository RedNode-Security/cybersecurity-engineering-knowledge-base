#!/usr/bin/env python3
"""Check Markdown front matter for pages marked reviewed or published without updated date."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
for path in sorted(ROOT.rglob('*.md')):
    if '.git' in path.parts:
        continue
    text = path.read_text(encoding='utf-8', errors='replace')
    if not text.startswith('---'):
        continue
    status = re.search(r'^status:\s*(reviewed|published)\s*$', text, re.MULTILINE)
    if status and not re.search(r'^updated:\s*\d{4}-\d{2}-\d{2}\s*$', text, re.MULTILINE):
        errors.append(f'{path.relative_to(ROOT)}: reviewed/published page missing updated date')
if errors:
    print('Review date check failed:')
    for err in errors:
        print(f'- {err}')
    sys.exit(1)
print('Review date check passed.')
