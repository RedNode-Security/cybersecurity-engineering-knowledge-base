---
title: Cybersecurity Engineering Coverage Matrix
domain: resources
category: coverage
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [coverage, maturity, roadmap]
difficulty: advanced
safe_publication: true
---


# Cybersecurity Engineering Coverage Matrix

## Overview

This matrix shows how much of the cybersecurity engineering domain the repository
covers and what needs deeper work.

## Domain Coverage

| Domain | Current coverage | Next depth target |
|---|---|---|
| Fundamentals | Strong | Add cryptography and risk examples |
| Identity security | Strong | Add more IdP, OAuth, and PAM case studies |
| Windows detection | Strong | Add Sysmon and PowerShell datasets |
| Linux detection | Moderate | Add sudo, SSH, systemd, auditd examples |
| Network detection | Moderate | Add DNS, proxy, firewall, and flow examples |
| Endpoint triage | Moderate | Add EDR process-tree case studies |
| Threat intelligence | Strong process | Add more sourced CVE and actor notes |
| Cloud AWS | Strong foundation | Add organization, SCP, S3, GuardDuty depth |
| Cloud Azure | Started | Add Entra, Activity Logs, app consent depth |
| Kubernetes | Started | Add audit policy, RBAC, secrets, admission depth |
| AppSec API | Strong | Add GraphQL, webhooks, rate limiting depth |
| OAuth/JWT | Good | Add token lifecycle and consent examples |
| AI security | Strong | Add evaluations, agent tools, RAG audit datasets |
| Automation | Good | Add runnable report generators |
| Architecture | Strong | Add capability maturity and metrics packs |

## Artifact Coverage

| Artifact type | Current state | Target state |
|---|---|---|
| Reference pages | Strong core | 100+ reviewed pages |
| Detection metadata | 20+ rules | 50+ rules |
| CVE pages | 10+ pages | 30+ pages |
| IOC reports | 10 synthetic | 30 synthetic/sourced |
| Playbooks | 10+ playbooks | 20+ exercised playbooks |
| Diagrams | 10+ diagrams | 25+ diagrams |
| JSON samples | Good start | Full dataset per major domain |
| Scripts | Validators | Validators plus generators |

## Maturity Interpretation

```text
The repository now has broad coverage and strong structure. The next maturity jump comes from deeper domain datasets, reviewed pages, and realistic case studies.
```
