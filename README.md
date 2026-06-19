# Cybersecurity Engineering Handbook

[![Validate repository](https://github.com/RedNode-Security/cybersecurity-engineering-knowledge-base/actions/workflows/validate.yml/badge.svg)](https://github.com/RedNode-Security/cybersecurity-engineering-knowledge-base/actions/workflows/validate.yml)
[![Markdown Validation](https://github.com/RedNode-Security/cybersecurity-engineering-knowledge-base/actions/workflows/markdown-check.yml/badge.svg)](https://github.com/RedNode-Security/cybersecurity-engineering-knowledge-base/actions/workflows/markdown-check.yml)

A professional cybersecurity engineering knowledge base for security notes, CVE
analysis, IOC samples, detection engineering, incident response, architecture
patterns, and automation ideas.

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
| [`00-Fundamentals`](00-Fundamentals/) | Core concepts, principles, OS security, networking, crypto, risk |
| [`01-Red-Team`](01-Red-Team/) | Authorized adversary-simulation methodology and assessment planning |
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

## Featured Detailed Starting Points

### Fundamentals

- [`Security Engineering Principles`](00-Fundamentals/security-engineering-principles.md)
- [`Network Security Foundations`](00-Fundamentals/Network-Security/network-security-foundations.md)
- [`Windows Event Logging`](00-Fundamentals/Windows-Security/windows-event-logging.md)
- [`Linux Hardening and Logging`](00-Fundamentals/Linux-Security/linux-hardening-and-logging.md)

### Blue Team and Detection Engineering

- [`Detection Engineering Methodology`](02-Blue-Team/Detection-Engineering/detection-engineering-methodology.md)
- [`Detection Rule Examples`](02-Blue-Team/Detection-Engineering/detection-rule-examples.md)
- [`Windows Authentication Detection`](02-Blue-Team/Detection-Engineering/windows-authentication-detection.md)
- [`SOC Alert Triage Workflow`](02-Blue-Team/SOC-Operations/soc-alert-triage.md)
- [`Account Compromise IR Playbook`](02-Blue-Team/Incident-Response/account-compromise-playbook.md)
- [`Example Account Compromise Case`](02-Blue-Team/Incident-Response/example-account-compromise-case.md)

### Threat Intelligence, Cloud, AppSec, AI, and Automation

- [`CVE Triage Workflow`](03-Threat-Intelligence/CVE-Intelligence/cve-triage-workflow.md)
- [`CVE Scoring Worksheet`](03-Threat-Intelligence/CVE-Intelligence/cve-scoring-worksheet.md)
- [`AWS CloudTrail Detection Examples`](04-Cloud-Security/AWS-Security/aws-cloudtrail-detection-examples.md)
- [`API Threat Model Example`](05-Application-Security/API-Security/api-threat-model-example.md)
- [`Prompt Injection Evaluation Examples`](06-AI-Security/LLM-Security/prompt-injection-evaluation-examples.md)
- [`RAG Security Checklist`](06-AI-Security/RAG-Security/rag-security-checklist.md)
- [`Example Enrichment Workflow`](07-Security-Automation/example-enrichment-workflow.md)
- [`Autonomous SOC Reference Model`](08-Architecture/autonomous-soc-reference-model.md)


## Elite Engineering Tracks

These tracks are intended to make the repository portfolio-grade and operationally useful.

| Track | Start here | Output |
|---|---|---|
| Detection-as-code | [`Detection Engineering Operating Model`](02-Blue-Team/Detection-Engineering/detection-engineering-operating-model.md) | Tested detection portfolio |
| SOC quality | [`SOC Metrics and Quality Model`](02-Blue-Team/SOC-Operations/soc-metrics-and-quality-model.md) | Monthly SOC quality report |
| Cloud IR | [`AWS Incident Response Playbook`](04-Cloud-Security/AWS-Security/aws-incident-response-playbook.md) | Cloud compromise response workflow |
| AppSec architecture | [`OAuth and JWT Security Deep Dive`](05-Application-Security/OAuth-JWT/oauth-jwt-security-deep-dive.md) | API auth review checklist |
| AI agent security | [`Agent Tool-Use Control Model`](06-AI-Security/Agent-Security/agent-tool-use-control-model.md) | Tool approval and audit model |
| Security architecture | [`Detection and Response Reference Architecture`](08-Architecture/detection-response-reference-architecture.md) | End-to-end security operating design |


## Publication Program

The repository is being developed toward a reference-grade encyclopedia. The
publication system is documented here:

- [`PUBLISHING.md`](PUBLISHING.md)
- [`REFERENCE_GRADE_ROADMAP.md`](REFERENCE_GRADE_ROADMAP.md)
- [`Reference-Grade Content Standard`](_meta/reference-grade-standard.md)
- [`Editorial Style Guide`](_meta/editorial-style-guide.md)
- [`Source and Citation Policy`](_meta/source-and-citation-policy.md)
- [`Human Review Checklist`](_meta/human-review-checklist.md)

Model reference pages:

- [`Password Spray Detection`](02-Blue-Team/Detection-Engineering/reference-password-spray-detection.md)
- [`Account Compromise Response`](02-Blue-Team/Incident-Response/reference-account-compromise-response.md)
- [`CVE-2021-44228 Log4Shell`](03-Threat-Intelligence/CVE-Intelligence/cve-2021-44228-log4shell-reference.md)
- [`CloudTrail IAM Detection`](04-Cloud-Security/AWS-Security/reference-cloudtrail-iam-detection.md)
- [`Broken Object Level Authorization`](05-Application-Security/API-Security/reference-broken-object-level-authorization.md)
- [`Prompt Injection Defense`](06-AI-Security/LLM-Security/reference-prompt-injection-defense.md)

## Documentation Standard

Every substantial document should answer:

1. What is it?
2. Why does it matter?
3. How does it work?
4. How can an attacker abuse it? *(authorized and educational context only)*
5. How can a defender detect it?
6. How can it be automated or operationalized?
7. What examples, sample logs, pseudocode, or checklists make it practical?

Recommended sections:

- Overview
- Architecture or mental model
- Attack perspective
- Defense perspective
- Detection strategy
- Automation strategy
- Worked example
- Tools
- References




## Serious Detection Reference Library

The detection library now includes platform-neutral reference pages, metadata,
sample events, and test cases across identity, Windows, Linux, network, cloud,
Kubernetes, application, and AI domains.

Start here:

- [`DETECTION_REFERENCE_LIBRARY.md`](DETECTION_REFERENCE_LIBRARY.md)
- [`Detection Reference Library Index`](02-Blue-Team/Detection-Engineering/reference-library/README.md)
- [`Detection Reference Coverage`](02-Blue-Team/Detection-Engineering/DETECTION_REFERENCE_COVERAGE.md)
- [`Detection Test Cases`](02-Blue-Team/Detection-Engineering/test-cases/detection-test-cases.json)

## Super Deep Dive Coverage

The repository now includes deeper practitioner coverage in these areas:

- Identity security detection
- Windows endpoint detection
- PowerShell detection
- Linux authentication detection
- DNS and proxy detection
- OSINT and malware tracking models
- AWS organization and S3 exposure security
- API logging and GraphQL security
- AI SOC operating model
- Detection coverage reporting
- Expanded sample datasets and detection metadata

See [`SUPER_DEEP_DIVE_ROADMAP.md`](SUPER_DEEP_DIVE_ROADMAP.md), [`COVERAGE_MATRIX.md`](COVERAGE_MATRIX.md), and [`SUPER_DEEP_DIVE_STATUS.md`](SUPER_DEEP_DIVE_STATUS.md).

## Reference Libraries

The repository now includes draft libraries that support the published reference material:

- [`Detection Rule Library`](02-Blue-Team/Detection-Engineering/rules/README.md)
- [`CVE Reference Library`](03-Threat-Intelligence/CVE-Intelligence/library/README.md)
- [`Synthetic IOC Reports`](03-Threat-Intelligence/IOC-Reports/synthetic/)
- [`IR Playbook Library`](02-Blue-Team/Incident-Response/playbooks/README.md)
- [`Architecture Diagrams`](08-Architecture/Diagrams/README.md)
- [`Published Index`](PUBLISHED_INDEX.md)
- [`Review Status`](REVIEW_STATUS.md)

## Quick Start

Create a new note from a template:

```bash
python scripts/new_note.py   --template 99-Templates/document-template.md   --title "Windows Event Logging"   --output 00-Fundamentals/Windows-Security/windows-event-logging.md
```

Regenerate the repository index:

```bash
python scripts/generate_index.py
```

Validate repository hygiene:

```bash
python scripts/validate_repository.py
python scripts/generate_index.py --check
npm_config_update_notifier=false npx --yes markdownlint-cli2 "**/*.md"
```

## Roadmap

- **Phase 1:** Foundation, taxonomy, templates, contribution workflow
- **Phase 2:** Blue team and detection engineering
- **Phase 3:** Red team methodologies
- **Phase 4:** Threat intelligence and automation
- **Phase 5:** AI security
- **Phase 6:** Autonomous security systems

See [`ROADMAP.md`](ROADMAP.md) and [`BACKLOG.md`](BACKLOG.md).

## License

This repository uses a dual-license model:

- Documentation, notes, templates, and diagrams: **CC BY-SA 4.0**
- Scripts, schemas, detection logic, automation examples, and code snippets: **MIT**

See [`LICENSE.md`](LICENSE.md), [`LICENSE-DOCS.md`](LICENSE-DOCS.md), and [`LICENSE-CODE.md`](LICENSE-CODE.md).
