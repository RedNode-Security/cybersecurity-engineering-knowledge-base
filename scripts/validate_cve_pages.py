#!/usr/bin/env python3
"""Check CVE pages for required reference-grade sections."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CVE_DIR = ROOT / '03-Threat-Intelligence' / 'CVE-Intelligence'
REQUIRED_SECTIONS = ['Executive Summary', 'Detection', 'Mitigation', 'References']
errors = []

for path in sorted(CVE_DIR.rglob('cve-*.md')) if CVE_DIR.exists() else []:
    if not re.match(r'^cve-\d{4}-\d+', path.name, re.IGNORECASE):
        continue
    text = path.read_text(encoding='utf-8', errors='replace')
    rel = path.relative_to(ROOT)
    if not re.search(r'CVE-\d{4}-\d+', text, re.IGNORECASE):
        errors.append(f'{rel}: missing CVE identifier')
    for section in REQUIRED_SECTIONS:
        if f'## {section}' not in text and section.lower() not in text.lower():
            errors.append(f'{rel}: missing section similar to {section!r}')
    if 'http://' not in text and 'https://' not in text:
        errors.append(f'{rel}: missing external references')

if errors:
    print('CVE page validation failed:')
    for err in errors:
        print(f'- {err}')
    sys.exit(1)
print('CVE page validation passed.')
