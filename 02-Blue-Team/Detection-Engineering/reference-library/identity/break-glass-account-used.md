---
title: Break-Glass Account Used
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, identity, reference]
difficulty: advanced
safe_publication: true
---


# Break-Glass Account Used

## Detection ID

```text
DET-IDENTITY-BREAK_GLASS_ACCOUNT_USED
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Break-glass account usage should be rare and explicitly approved.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `identity_signin_logs`, `admin_audit_logs`

Required fields:

- `timestamp`
- `user`
- `application`
- `action`

## Normalized Logic

```text
signin where user in break_glass_accounts
```

## Positive Sample Event

```json
{
  "event_id": "evt-id-007",
  "user": "breakglass-admin@example.com",
  "result": "success",
  "approval_id": null
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-id-benign-007",
  "user": "breakglass-admin@example.com",
  "result": "success",
  "approval_id": "BG-TEST-1",
  "test_window": true
}
```

## Expected False Positives

- scheduled emergency access test

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

Break-glass accounts should be noisy by design. Treat every use as worth review.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-IDENTITY-BREAK_GLASS_ACCOUNT_USED
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
