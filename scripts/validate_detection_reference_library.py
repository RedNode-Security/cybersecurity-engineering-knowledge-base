#!/usr/bin/env python3
"""Validate that detection reference pages exist for detection metadata."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
RULE_DIR = ROOT / '02-Blue-Team' / 'Detection-Engineering' / 'rules'
errors = []
required_sections = ['## Hypothesis', '## Required Telemetry', '## Normalized Logic', '## Triage Workflow', '## Response Guidance', '## Test Case']

for path in sorted(RULE_DIR.rglob('*.json')) if RULE_DIR.exists() else []:
    data = json.loads(path.read_text(encoding='utf-8'))
    ref = data.get('reference_page')
    if not ref:
        # Older draft metadata may not have a reference page yet.
        continue
    ref_path = ROOT / ref
    if not ref_path.exists():
        errors.append(f'{path.relative_to(ROOT)}: missing reference page {ref}')
        continue
    text = ref_path.read_text(encoding='utf-8', errors='replace')
    for section in required_sections:
        if section not in text:
            errors.append(f'{ref}: missing section {section}')

test_file = ROOT / '02-Blue-Team' / 'Detection-Engineering' / 'test-cases' / 'detection-test-cases.json'
if test_file.exists():
    tests = json.loads(test_file.read_text(encoding='utf-8'))
    ids = {t.get('detection_id') for t in tests}
    for path in sorted(RULE_DIR.rglob('*.json')):
        data = json.loads(path.read_text(encoding='utf-8'))
        if data.get('reference_page') and data.get('id') not in ids:
            errors.append(f'{path.relative_to(ROOT)}: missing test case for {data.get("id")}')
else:
    errors.append('missing detection test case file')

if errors:
    print('Detection reference library validation failed:')
    for err in errors:
        print(f'- {err}')
    sys.exit(1)
print('Detection reference library validation passed.')
