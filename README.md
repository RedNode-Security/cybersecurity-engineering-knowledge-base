# Cybersecurity Engineering Knowledge Base

[![Validate repository](https://github.com/RedNode-Security/cybersecurity-engineering-knowledge-base/actions/workflows/validate.yml/badge.svg)](https://github.com/RedNode-Security/cybersecurity-engineering-knowledge-base/actions/workflows/validate.yml)
[![Markdown Validation](https://github.com/RedNode-Security/cybersecurity-engineering-knowledge-base/actions/workflows/markdown-check.yml/badge.svg)](https://github.com/RedNode-Security/cybersecurity-engineering-knowledge-base/actions/workflows/markdown-check.yml)

A practical cybersecurity engineering knowledge base covering security fundamentals, detection engineering, incident response, threat intelligence, cloud security, application security, AI security, automation, and security architecture.

> **Core philosophy:** Understand → Model → Detect → Automate → Improve

## Purpose

This repository is designed to serve as:

- A personal cybersecurity knowledge base
- A public portfolio of security engineering thinking
- A research repository for CVEs, IOCs, detections, and threat intelligence
- A documentation system for defensive and adversary-informed security engineering
- A foundation for future autonomous security systems

## Scope

The repository focuses on defensive, educational, and research-oriented content:

- Security fundamentals and architecture
- Blue team operations, incident response, threat hunting, and detection engineering
- Authorized red-team methodology and attacker mental models
- Threat intelligence, IOC management, and CVE tracking
- Cloud, application, and AI security
- Automation patterns for SIEM, SOAR, enrichment, and security workflows

For publication boundaries, see [`_meta/content-safety-policy.md`](_meta/content-safety-policy.md).

## Repository Map

| Area | Purpose |
|---|---|
| [`00-Fundamentals`](00-Fundamentals/) | Core concepts, principles, operating systems, networks, crypto, risk |
| [`01-Red-Team`](01-Red-Team/) | Authorized adversary simulation methodology and assessment planning |
| [`02-Blue-Team`](02-Blue-Team/) | SOC operations, IR, threat hunting, detection engineering, malware triage |
| [`03-Threat-Intelligence`](03-Threat-Intelligence/) | IOCs, threat profiles, OSINT, malware tracking, CVE intelligence |
| [`04-Cloud-Security`](04-Cloud-Security/) | AWS, Azure, Kubernetes, cloud IR, identity and posture management |
| [`05-Application-Security`](05-Application-Security/) | API, JWT, OAuth, secure coding, SDLC, application security testing |
| [`06-AI-Security`](06-AI-Security/) | LLM security, prompt injection, RAG security, AI SOC architecture |
| [`07-Security-Automation`](07-Security-Automation/) | Mini SIEM, SOAR workflows, enrichment pipelines, automation patterns |
| [`08-Architecture`](08-Architecture/) | Zero Trust, XDR, SOC, autonomous security systems, design patterns |
| [`09-Resources`](09-Resources/) | Books, tools, references, labs, datasets, checklists |
| [`99-Templates`](99-Templates/) | Templates for notes, CVEs, IOCs, detections, playbooks, labs, ADRs |
| [`schemas`](schemas/) | Lightweight schemas for structured samples |
| [`scripts`](scripts/) | Helper scripts for validation and index generation |

## Featured Starting Points

- [`Security Engineering Principles`](00-Fundamentals/security-engineering-principles.md)
- [`Detection Engineering Methodology`](02-Blue-Team/Detection-Engineering/detection-engineering-methodology.md)
- [`Windows Authentication Detection`](02-Blue-Team/Detection-Engineering/windows-authentication-detection.md)
- [`Account Compromise IR Playbook`](02-Blue-Team/Incident-Response/account-compromise-playbook.md)
- [`CVE Triage Workflow`](03-Threat-Intelligence/CVE-Intelligence/cve-triage-workflow.md)
- [`IOC Lifecycle and Scoring`](03-Threat-Intelligence/IOC-Management/ioc-lifecycle-and-scoring.md)
- [`API Security Checklist`](05-Application-Security/API-Security/api-security-checklist.md)
- [`Prompt Injection Threat Model`](06-AI-Security/LLM-Security/prompt-injection-threat-model.md)

## Documentation Standard

Every substantial document should answer:

1. What is it?
2. Why does it matter?
3. How does it work?
4. How can an attacker abuse it? *(authorized and educational context only)*
5. How can a defender detect it?
6. How can it be automated or operationalized?

Recommended sections:

- Overview
- Architecture or mental model
- Attack perspective
- Defense perspective
- Detection strategy
- Automation strategy
- Tools
- References

## Metadata Standard

Use YAML front matter for notes and analyses:

```yaml
title: Example Topic
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [detection, siem]
difficulty: beginner
safe_publication: true
```

## Quick Start

Create a new note from a template:

```bash
python scripts/new_note.py \
  --template 99-Templates/document-template.md \
  --title "Windows Event Logging" \
  --output 00-Fundamentals/Windows-Security/windows-event-logging.md
```

Regenerate the repository index:

```bash
python scripts/generate_index.py
```

Validate repository hygiene:

```bash
python scripts/validate_repository.py
python scripts/generate_index.py --check
```

## Roadmap

- **Phase 1:** Foundation, taxonomy, templates, contribution workflow
- **Phase 2:** Blue team and detection engineering
- **Phase 3:** Red team methodologies
- **Phase 4:** Threat intelligence and automation
- **Phase 5:** AI security
- **Phase 6:** Autonomous security systems

See [`ROADMAP.md`](ROADMAP.md) and [`BACKLOG.md`](BACKLOG.md).

## Contribution Model

Contributions should be:

- Accurate and reference-backed
- Defensive or educational in intent
- Safe to publish publicly
- Clearly labeled as draft, reviewed, published, or archived
- Sanitized of secrets, customer data, internal-only hostnames, and live-target details

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

This repository uses a dual-license model:

- Documentation, notes, templates, and diagrams: **CC BY-SA 4.0**
- Scripts, schemas, detection logic, automation examples, and code snippets: **MIT**

See [`LICENSE.md`](LICENSE.md), [`LICENSE-DOCS.md`](LICENSE-DOCS.md), and [`LICENSE-CODE.md`](LICENSE-CODE.md).
