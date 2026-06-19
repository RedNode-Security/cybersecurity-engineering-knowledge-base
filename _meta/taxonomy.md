# Repository Taxonomy

This taxonomy defines how content is named, classified, reviewed, and expanded.
It keeps the repository useful as it grows from a personal knowledge base into a
professional security engineering reference.

## Domain Taxonomy

| Domain | Purpose | Example artifacts |
|---|---|---|
| `fundamentals` | Core security concepts and mental models | Principles, networking, OS security, risk, cryptography |
| `red-team` | Authorized adversary-simulation methodology | ROE, scope, attack-surface maps, lab plans, reporting models |
| `blue-team` | Defensive operations and detection | SOC triage, IR playbooks, detections, hunts, log strategy |
| `threat-intelligence` | Vulnerability, IOC, and threat context | CVE triage, IOC reports, actor profiles, OSINT notes |
| `cloud-security` | Cloud control-plane and workload security | IAM, CloudTrail, Kubernetes, cloud IR, posture management |
| `application-security` | Secure software and API engineering | API authz, JWT, OAuth, secure SDLC, threat models |
| `ai-security` | LLM, RAG, agent, and AI SOC security | Prompt injection, retrieval security, tool-use controls |
| `security-automation` | Repeatable enrichment and response workflows | SIEM helpers, SOAR patterns, pipeline designs, scripts |
| `architecture` | Security capability design | SOC, Zero Trust, XDR, autonomous security systems |
| `resources` | Learning support and references | Labs, standards, datasets, reading paths, tools |

## Content Types

| Type | Definition | Minimum expectation |
|---|---|---|
| `concept` | Explains a security idea | Overview, why it matters, examples, references |
| `methodology` | Repeatable process | Inputs, steps, outputs, examples, safety boundary |
| `checklist` | Review or implementation aid | Action items, evidence, owner, review cadence |
| `playbook` | Response or operational workflow | Triggers, severity, triage, response, evidence, comms |
| `detection` | Detection logic or hypothesis | Telemetry, logic, false positives, triage, test plan |
| `cve-analysis` | Vulnerability triage writeup | Impact, exposure, mitigation, detection, decision record |
| `ioc-report` | Indicator report | Source, confidence, context, expiration, handling |
| `threat-profile` | Actor/campaign behavior summary | Confidence, TTPs, defensive guidance, references |
| `lab` | Controlled practice environment | Scope, safety, setup, expected evidence, cleanup |
| `architecture-decision-record` | Security design decision | Context, options, decision, consequences, review date |
| `reference` | Curated supporting material | Link, why it matters, related sections |

## Status Values

| Status | Meaning | Who should use it |
|---|---|---|
| `draft` | Content is useful but still being expanded | Personal learning and review |
| `reviewed` | Checked for safety, clarity, and basic accuracy | Public reference |
| `published` | Portfolio-grade and reference-backed | Public sharing |
| `archived` | Kept for history but not maintained | Historical context |

## Difficulty Values

- `beginner`: explains the basics and avoids assuming operational experience.
- `intermediate`: assumes comfort with logs, systems, and security concepts.
- `advanced`: assumes engineering, incident response, detection, or architecture experience.

## Metadata Requirements

Most Markdown pages should include YAML front matter:

```yaml
title: Windows Authentication Detection
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [windows, authentication, detection]
difficulty: intermediate
safe_publication: true
```

## Naming Rules

Use lowercase kebab-case for files:

```text
windows-event-logging.md
account-compromise-playbook.md
api-threat-model-example.md
```

Use directories to show domain and operational context:

```text
02-Blue-Team/Detection-Engineering/
03-Threat-Intelligence/CVE-Intelligence/
06-AI-Security/RAG-Security/
```

## Intelligence Confidence

| Confidence | Meaning | Operational use |
|---|---|---|
| `low` | Single weak source, old observation, or little context | Enrichment or hunting only |
| `medium` | Credible source with partial context | Alerting or scoped review |
| `high` | Strong source, recent context, and corroboration | Alerting, response, or blocking after risk review |

## Safe Publication Checklist

Before marking content as safe to publish:

- [ ] No secrets, tokens, keys, cookies, private customer data, or internal-only context.
- [ ] No weaponized exploit chain or destructive payload.
- [ ] No stealth, evasion, persistence, or unauthorized access guidance.
- [ ] Public examples use `example.com`, `.invalid`, RFC 5737 IP ranges, or synthetic values.
- [ ] Red-team content is authorization-first and methodology-focused.
- [ ] CVE content emphasizes mitigation, detection, and responsible validation.
- [ ] IOCs include confidence, context, and expiration.
