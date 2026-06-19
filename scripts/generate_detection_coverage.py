#!/usr/bin/env python3
"""Generate a simple Markdown coverage report from detection metadata."""
from pathlib import Path
import json
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parents[1]
RULE_DIR = ROOT / '02-Blue-Team' / 'Detection-Engineering' / 'rules'
OUT = ROOT / '02-Blue-Team' / 'Detection-Engineering' / 'DETECTION_COVERAGE.generated.md'

rules = []
for path in sorted(RULE_DIR.rglob('*.json')) if RULE_DIR.exists() else []:
    rules.append(json.loads(path.read_text(encoding='utf-8')))

by_source = Counter()
by_severity = Counter()
by_status = Counter()
by_owner = Counter()
for rule in rules:
    by_severity[rule.get('severity', 'unknown')] += 1
    by_status[rule.get('status', 'unknown')] += 1
    by_owner[rule.get('owner', 'unknown')] += 1
    for source in rule.get('data_sources', []):
        by_source[source] += 1

lines = ['# Detection Coverage Report', '', f'Total rules: {len(rules)}', '']
for title, counter in [('By Severity', by_severity), ('By Status', by_status), ('By Data Source', by_source), ('By Owner', by_owner)]:
    lines.extend([f'## {title}', ''])
    for key, count in sorted(counter.items()):
        lines.append(f'- {key}: {count}')
    lines.append('')
OUT.write_text('\n'.join(lines), encoding='utf-8')
print(f'Wrote {OUT.relative_to(ROOT)}')
