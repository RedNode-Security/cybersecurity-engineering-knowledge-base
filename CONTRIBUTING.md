# Contributing Guide

This repository is a cybersecurity engineering knowledge base. Contributions should improve accuracy, clarity, operational usefulness, or safe defensive practice.

## Content Rules

Acceptable content:

- Defensive security notes
- Threat intelligence summaries
- Sanitized IOC samples
- CVE analysis focused on impact, mitigation, detection, and safe validation
- Authorized security testing methodology
- Detection engineering and incident response workflows
- Security architecture patterns

Do not publish:

- Real credentials, tokens, private keys, customer data, or internal-only details
- Weaponized exploit code or instructions to compromise third-party systems
- Malware binaries or live destructive payloads
- Instructions focused on stealth, evasion, persistence, or unauthorized access
- Unverified accusations or unsupported attribution claims

## Writing Standard

Every substantial document should include:

1. Overview
2. Why it matters
3. Technical model
4. Attack perspective
5. Defense perspective
6. Detection strategy
7. Automation strategy
8. References

Use templates from [`99-Templates`](99-Templates/).

## File Naming

Use lowercase kebab-case where possible:

```text
windows-event-logging.md
cve-2026-0000-product-name.md
aws-iam-risk-patterns.md
```

Directory names may retain numeric prefixes for domain ordering.

## Metadata

Add YAML front matter to notes:

```yaml
title: Topic Name
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [soc, detection]
difficulty: intermediate
safe_publication: true
```

Recommended status values:

- `draft`
- `reviewed`
- `published`
- `archived`

## References

Prefer primary sources:

- Vendor advisories
- Official documentation
- Standards bodies
- Peer-reviewed or reputable research
- Public detection engineering references

Cite links directly in the References section.

## Review Checklist

Before submitting or publishing:

- [ ] No secrets or sensitive data
- [ ] No unsafe exploit instructions
- [ ] Sources are linked
- [ ] Claims are separated from assumptions
- [ ] Detection guidance includes likely false positives
- [ ] Defensive value is clear
- [ ] Markdown renders correctly
- [ ] JSON samples validate

## Local Validation

```bash
python scripts/validate_repository.py
python scripts/generate_index.py
```
