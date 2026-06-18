#!/usr/bin/env python3
"""Lightweight repository hygiene checks.

Checks:
- Markdown files are not empty.
- Markdown notes outside top-level docs/templates have YAML-like front matter.
- JSON files parse successfully.
- IOC samples contain required top-level fields.
"""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {'.git'}
REQUIRED_IOC_FIELDS = {'report_id', 'tlp', 'source', 'confidence', 'created', 'indicators'}
TOP_LEVEL_MD_WITHOUT_FRONTMATTER = {
    'README.md', 'ROADMAP.md', 'CONTRIBUTING.md', 'SECURITY.md', 'LICENSE-OPTIONS.md',
    'LICENSE.md', 'LICENSE-DOCS.md', 'LICENSE-CODE.md', 'NOTICE.md',
    'INDEX.md', 'BACKLOG.md', 'PROJECT_STATUS.md'
}
TEMPLATE_DIRS = {'99-Templates', '_meta'}

errors = []

for path in ROOT.rglob('*'):
    if not path.is_file():
        continue
    rel = path.relative_to(ROOT)
    if any(part in SKIP_PARTS for part in rel.parts):
        continue

    if path.suffix.lower() == '.md':
        text = path.read_text(encoding='utf-8', errors='replace')
        if not text.strip():
            errors.append(f'Empty markdown file: {rel}')
            continue
        needs_frontmatter = (
            rel.name not in TOP_LEVEL_MD_WITHOUT_FRONTMATTER
            and rel.parts[0] not in TEMPLATE_DIRS
            and rel.name != 'README.md'
        )
        if needs_frontmatter and not text.startswith('---\n'):
            errors.append(f'Missing front matter: {rel}')

    if path.suffix.lower() == '.json':
        try:
            data = json.loads(path.read_text(encoding='utf-8'))
        except Exception as exc:
            errors.append(f'Invalid JSON: {rel}: {exc}')
            continue
        if 'ioc' in str(rel).lower() and rel.name != 'ioc.schema.json':
            missing = REQUIRED_IOC_FIELDS - set(data)
            if missing:
                errors.append(f'IOC JSON missing {sorted(missing)}: {rel}')

if errors:
    print('Repository validation failed:')
    for err in errors:
        print(f'- {err}')
    sys.exit(1)

print('Repository validation passed.')
