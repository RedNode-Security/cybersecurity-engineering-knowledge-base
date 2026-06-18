#!/usr/bin/env python3
"""Create a new note from a Markdown template."""
from pathlib import Path
import argparse
import re
from datetime import date

ROOT = Path(__file__).resolve().parents[1]


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-') or 'new-note'


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--template', default='99-Templates/document-template.md')
    parser.add_argument('--title', required=True)
    parser.add_argument('--output', help='Output path. Defaults to ./<slug>.md')
    args = parser.parse_args()

    template_path = ROOT / args.template
    if not template_path.exists():
        raise SystemExit(f'Template not found: {args.template}')

    output = ROOT / (args.output or f'{slugify(args.title)}.md')
    if output.exists():
        raise SystemExit(f'Output already exists: {output.relative_to(ROOT)}')

    today = date.today().isoformat()
    content = template_path.read_text(encoding='utf-8')
    content = content.replace('<Topic Title>', args.title)
    content = content.replace('created: 2026-06-18', f'created: {today}')
    content = content.replace('updated: 2026-06-18', f'updated: {today}')

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(content, encoding='utf-8')
    print(f'Created {output.relative_to(ROOT)}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
