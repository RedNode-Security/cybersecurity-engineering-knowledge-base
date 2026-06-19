#!/usr/bin/env python3
"""Parse every JSON file in the repository."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
for path in sorted(ROOT.rglob('*.json')):
    if '.git' in path.parts:
        continue
    try:
        json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'{path.relative_to(ROOT)}: {exc}')

if errors:
    print('JSON sample validation failed:')
    for err in errors:
        print(f'- {err}')
    sys.exit(1)
print('JSON sample validation passed.')
