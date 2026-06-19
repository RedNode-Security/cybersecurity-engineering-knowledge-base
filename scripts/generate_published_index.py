#!/usr/bin/env python3
"""Generate a simple index of pages with status: published."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'PUBLISHED_INDEX.generated.md'

pages = []
for path in sorted(ROOT.rglob('*.md')):
    if '.git' in path.parts or path.name.startswith('PUBLISHED_INDEX'):
        continue
    text = path.read_text(encoding='utf-8', errors='replace')
    if text.startswith('---') and re.search(r'^status:\s*published\s*$', text, re.MULTILINE):
        title_match = re.search(r'^title:\s*(.+)$', text, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else path.stem
        pages.append((title, path.relative_to(ROOT).as_posix()))

lines = ['# Generated Published Index', '', 'Generated from pages with `status: published`.', '']
for title, rel in pages:
    lines.append(f'- [{title}]({rel})')
lines.append('')
OUT.write_text('\n'.join(lines), encoding='utf-8')
print(f'Wrote {OUT.relative_to(ROOT)} with {len(pages)} pages.')
