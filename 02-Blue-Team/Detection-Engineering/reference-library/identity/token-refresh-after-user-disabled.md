---
title: Token Refresh After User Disabled
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, identity, reference]
difficulty: advanced
safe_publication: true
---


# Token Refresh After User Disabled

## Detection ID

```text
DET-IDENTITY-TOKEN_REFRESH_AFTER_USER_DISABLED
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Compromised or stale sessions may continue after account disablement.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `identity_token_logs`, `directory_audit_logs`

Required fields:

- `timestamp`
- `user`
- `token_event`
- `account_status`

## Normalized Logic

```text
token_refresh where account_status=disabled
```

## Positive Sample Event

```json
{
  "event_id": "evt-id-012",
  "user": "disabled.user@example.com",
  "token_event": "refresh",
  "account_status": "disabled"
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-id-benign-012",
  "user": "disabled.user@example.com",
  "token_event": "revoked",
  "account_status": "disabled"
}
```

## Expected False Positives

- replication delay
- application session caching

## Triage Workflow

1. Confirm affected entity and timestamp
2. Review surrounding events for 24 hours
3. Check approved change or expected business activity
4. Escalate if behavior remains unexplained

## Response Guidance

- Preserve relevant logs
- Open an incident case if suspicious
- Contain affected identity, host, or resource if compromise is confirmed

## Analyst Note

This is often an identity architecture issue, not just a detection issue.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-IDENTITY-TOKEN_REFRESH_AFTER_USER_DISABLED
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
