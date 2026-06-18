#!/usr/bin/env python3
"""Generate INDEX.md from repository markdown files."""
from pathlib import Path
import argparse
import sys

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / 'INDEX.md'
SKIP_DIRS = {'.git'}


def title_from_markdown(path: Path) -> str:
    for line in path.read_text(encoding='utf-8', errors='replace').splitlines():
        if line.startswith('# '):
            return line[2:].strip()
    return path.stem.replace('-', ' ').title()


def build_index() -> str:
    files = []
    for path in ROOT.rglob('*.md'):
        rel = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if rel.name == 'INDEX.md':
            continue
        files.append(rel)

    files.sort(key=lambda p: str(p).lower())
    lines = [
        '# Repository Index',
        '',
        'Generated from Markdown files.',
        '',
    ]
    current_top = None
    for rel in files:
        top = rel.parts[0] if len(rel.parts) > 1 else 'Root'
        if top != current_top:
            current_top = top
            lines.extend(['', f'## {top}', ''])
        title = title_from_markdown(ROOT / rel)
        lines.append(f'- [{title}]({rel.as_posix()})')
    lines.append('')
    return '\n'.join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true', help='fail if INDEX.md is not current')
    args = parser.parse_args()

    content = build_index()
    if args.check:
        existing = INDEX.read_text(encoding='utf-8') if INDEX.exists() else ''
        if existing != content:
            print('INDEX.md is out of date. Run: python scripts/generate_index.py')
            return 1
        print('INDEX.md is current.')
        return 0

    INDEX.write_text(content, encoding='utf-8')
    print(f'Wrote {INDEX.relative_to(ROOT)}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
