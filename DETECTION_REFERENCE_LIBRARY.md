---
title: Detection Reference Library
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, coverage, reference-library]
difficulty: advanced
safe_publication: true
---


# Detection Reference Library

## Purpose

This repository now contains a serious platform-neutral detection reference
library. The library is not a collection of random SIEM queries. Each detection
is documented as an engineering artifact with a hypothesis, telemetry contract,
logic, sample data, false positives, triage steps, response guidance, and test
cases.

## Library Design

```text
Behavior → Detection Metadata → Reference Page → Sample Events → Test Case → Coverage Report
```

## Coverage Domains

| Domain | What it covers |
|---|---|
| Identity | Sign-ins, MFA, OAuth, roles, service accounts, session risk |
| Windows | Event logs, EDR process trees, PowerShell, services, scheduled tasks |
| Linux | SSH, sudo, authorized keys, cron, systemd, privileged users |
| Network | DNS, proxy, egress, beaconing, upload/download behavior |
| Cloud | AWS, Azure, IAM, logging, keys, public exposure, guardrails |
| Kubernetes | RBAC, secrets, pod security, exec, admission and namespace behavior |
| Application | API authorization, exports, GraphQL, webhooks, admin actions |
| AI | LLM/RAG/agent audit logs, tool calls, prompt injection signals |

## What Makes A Detection Reference-Grade

A reference-grade detection page includes:

- A behavior-based hypothesis
- Required telemetry and fields
- Normalized event assumptions
- Positive and benign sample events
- Pseudocode logic
- Tuning guidance
- False positive categories
- Triage workflow
- Response guidance
- Test case mapping
- Maintenance notes

## Production Use Warning

These detections are platform-neutral. Before production deployment:

1. Map fields to your SIEM schema.
2. Validate log availability and retention.
3. Tune false positives with local context.
4. Add sample events from your environment if allowed.
5. Assign an owner and review date.
6. Deploy first in monitor-only or low-severity mode.

## Files To Review

- `02-Blue-Team/Detection-Engineering/reference-library/`
- `02-Blue-Team/Detection-Engineering/rules/`
- `02-Blue-Team/Detection-Engineering/test-cases/`
- `02-Blue-Team/samples/detection-reference/`
- `02-Blue-Team/Detection-Engineering/DETECTION_REFERENCE_COVERAGE.md`
