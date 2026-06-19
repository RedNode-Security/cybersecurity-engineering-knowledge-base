---
title: SOAR Human Approval Patterns
domain: security-automation
category: soar
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [soar, automation, approval, incident-response]
difficulty: advanced
safe_publication: true
---


# SOAR Human Approval Patterns

## Overview

SOAR workflows should automate enrichment and low-risk actions first. High-impact
containment needs human approval, auditability, and rollback.

## Approval Levels

| Level | Approver | Example action |
|---|---|---|
| Analyst | Tier 2 analyst | Add account to watchlist |
| Incident lead | IR lead | Revoke sessions |
| Service owner | Application owner | Disable production integration |
| Incident commander | Incident commander | Isolate production segment |

## Workflow Pattern

```text
Alert → Enrich → Recommend → Approval Request → Execute → Verify → Audit → Rollback if needed
```

## Approval Request Template

```text
Case: IR-2026-001
Recommended action: Revoke sessions for alex.admin@example.com
Reason: Unusual sign-in followed by unauthorized admin action
Expected impact: User must re-authenticate
Rollback: User can authenticate after password reset and MFA verification
Approver: Incident lead
Expiration: Approval valid for 30 minutes
```

## Safety Controls

- Approval expires.
- Tool arguments are visible to approver.
- Execution result is logged.
- Failed execution does not retry endlessly.
- Rollback instructions are included.
- Business impact is shown.

## Anti-Patterns

- Auto-disabling accounts from low-confidence alerts.
- Blocking shared IP ranges without review.
- Running tools with global admin permissions.
- No audit record of who approved an action.
- No rollback plan.
