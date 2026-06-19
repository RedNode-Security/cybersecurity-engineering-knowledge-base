---
title: Service Account Interactive Login
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, identity, reference]
difficulty: advanced
safe_publication: true
---


# Service Account Interactive Login

## Detection ID

```text
DET-IDENTITY-SERVICE_ACCOUNT_INTERACTIVE_LOGIN
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Service accounts should not perform interactive logins.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `identity_signin_logs`, `directory_inventory`

Required fields:

- `timestamp`
- `user`
- `account_type`
- `logon_type`

## Normalized Logic

```text
account_type=service and logon_type=interactive
```

## Positive Sample Event

```json
{
  "event_id": "evt-id-010",
  "user": "svc-backup@example.com",
  "account_type": "service",
  "logon_type": "interactive",
  "result": "success"
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-id-benign-010",
  "user": "svc-backup@example.com",
  "account_type": "service",
  "logon_type": "service",
  "result": "success"
}
```

## Expected False Positives

- misclassified account
- legacy admin script

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

Inventory accuracy matters. Fix classification if the account is not really a service account.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-IDENTITY-SERVICE_ACCOUNT_INTERACTIVE_LOGIN
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
