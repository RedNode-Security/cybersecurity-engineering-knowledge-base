---
title: AWS Organization Security Deep Dive
domain: cloud-security
category: aws-security
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [aws, organizations, scp, cloud-security]
difficulty: advanced
safe_publication: true
---


# AWS Organization Security Deep Dive

## Scope

This page covers AWS Organizations, multi-account governance, service control
policies, central logging, and security account patterns.

## Multi-Account Model

```text
Management Account → Security Account → Log Archive Account → Workload Accounts
```

## Core Controls

| Control | Purpose |
|---|---|
| Service Control Policies | Set account-level guardrails |
| Central CloudTrail | Preserve control-plane evidence |
| Log Archive Account | Restrict log modification |
| Security Account | Central security tooling |
| Account vending | Consistent baseline for new accounts |
| Tagging policy | Ownership and criticality context |

## High-Value SCP Ideas

- Restrict disabling CloudTrail.
- Restrict leaving the organization.
- Restrict root account usage where feasible.
- Restrict public S3 configuration changes except approved roles.
- Restrict security tooling tampering.

## Detection Ideas

- New account without baseline controls.
- CloudTrail stopped in any member account.
- SCP changed by unexpected principal.
- GuardDuty disabled.
- Security hub standards disabled.
- Log archive bucket policy changed.

## Response

- Identify account and principal.
- Preserve organization CloudTrail.
- Restore guardrail or baseline.
- Review related IAM activity.
- Check whether workload data was accessed.
