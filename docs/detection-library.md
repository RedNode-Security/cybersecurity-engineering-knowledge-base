---
title: Detection Library
description: Detection engineering entry points for the Cybersecurity Engineering Handbook.
status: published
created: 2026-06-19
updated: 2026-06-19
tags: [detection, detection-engineering, reference-library]
safe_publication: true
---

# Detection Library

The detection library is the strongest technical section of the handbook. It is
platform-neutral: the detections describe behavior, telemetry, sample events,
triage, response, and testing rather than locking into one SIEM query language.

## What the library contains

- Detection metadata
- Human-readable reference pages
- Positive sample events
- Benign sample events
- Test case mappings
- Coverage reports
- Validation scripts

## Main source pages

- [Detection Reference Library](https://github.com/RedNode-Security/cybersecurity-engineering-handbook/blob/main/DETECTION_REFERENCE_LIBRARY.md)
- [Serious Detection Library Status](https://github.com/RedNode-Security/cybersecurity-engineering-handbook/blob/main/SERIOUS_DETECTION_LIBRARY_STATUS.md)
- [Detection Reference Coverage](https://github.com/RedNode-Security/cybersecurity-engineering-handbook/blob/main/02-Blue-Team/Detection-Engineering/DETECTION_REFERENCE_COVERAGE.md)
- [Detection Rules](https://github.com/RedNode-Security/cybersecurity-engineering-handbook/tree/main/02-Blue-Team/Detection-Engineering/rules)
- [Detection Reference Pages](https://github.com/RedNode-Security/cybersecurity-engineering-handbook/tree/main/02-Blue-Team/Detection-Engineering/reference-library)
- [Detection Test Cases](https://github.com/RedNode-Security/cybersecurity-engineering-handbook/blob/main/02-Blue-Team/Detection-Engineering/test-cases/detection-test-cases.json)

## Domains covered

| Domain | Examples |
|---|---|
| Identity | password spray, risky sign-in, MFA changes, OAuth consent, service accounts |
| Windows | PowerShell, LSASS access, local admin changes, scheduled tasks, WMI |
| Linux | SSH, sudoers, authorized keys, systemd, cron |
| Network | DNS, proxy, beaconing, rare destinations, large uploads |
| Cloud | AWS IAM, CloudTrail, S3, GuardDuty, Azure roles and consent |
| Kubernetes | RBAC, secrets, privileged pods, exec, admission denials |
| Application | API authorization, exports, GraphQL, admin actions, webhooks |
| AI | tool calls, RAG access, prompt injection, sensitive output redaction |

## Production use

Before using a detection in production:

1. Map fields to your SIEM schema.
2. Validate log availability.
3. Test positive and benign samples.
4. Tune false positives.
5. Assign an owner and review date.
6. Deploy first in monitor-only or low-severity mode.
