#!/usr/bin/env python3
"""Validate detection metadata JSON files without external dependencies."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
RULE_DIR = ROOT / '02-Blue-Team' / 'Detection-Engineering' / 'rules'
REQUIRED = {
    'id', 'name', 'status', 'hypothesis', 'severity', 'confidence',
    'data_sources', 'required_fields', 'owner', 'review_date'
}
SEVERITIES = {'low', 'medium', 'high', 'critical'}
CONFIDENCE = {'low', 'medium', 'high'}
STATUS = {'experimental', 'production', 'deprecated'}

errors = []
for path in sorted(RULE_DIR.rglob('*.json')) if RULE_DIR.exists() else []:
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'{path.relative_to(ROOT)}: invalid JSON: {exc}')
        continue
    missing = REQUIRED - set(data)
    if missing:
        errors.append(f'{path.relative_to(ROOT)}: missing {sorted(missing)}')
    if data.get('severity') not in SEVERITIES:
        errors.append(f'{path.relative_to(ROOT)}: invalid severity {data.get("severity")!r}')
    if data.get('confidence') not in CONFIDENCE:
        errors.append(f'{path.relative_to(ROOT)}: invalid confidence {data.get("confidence")!r}')
    if data.get('status') not in STATUS:
        errors.append(f'{path.relative_to(ROOT)}: invalid status {data.get("status")!r}')
    for field in ['data_sources', 'required_fields']:
        if not isinstance(data.get(field), list) or not data.get(field):
            errors.append(f'{path.relative_to(ROOT)}: {field} must be a non-empty list')

if errors:
    print('Detection metadata validation failed:')
    for err in errors:
        print(f'- {err}')
    sys.exit(1)
print('Detection metadata validation passed.')
