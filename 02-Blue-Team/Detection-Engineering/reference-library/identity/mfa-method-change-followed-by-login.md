---
title: MFA Method Change Followed by New Login
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, identity, reference]
difficulty: advanced
safe_publication: true
---


# MFA Method Change Followed by New Login

## Detection ID

```text
DET-IDENTITY-MFA_METHOD_CHANGE_FOLLOWED_BY_LOGIN
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Account takeover may involve MFA method change followed by login from a new source.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `identity_audit_logs`, `identity_signin_logs`

Required fields:

- `timestamp`
- `user`
- `action`
- `source_ip`

## Normalized Logic

```text
mfa_method_change(user) join signin(user, source_is_new=true) within 24h
```

## Positive Sample Event

```json
{
  "event_id": "evt-id-003",
  "timestamp": "2026-06-19T11:00:00Z",
  "user": "user@example.com",
  "action": "mfa_method_added",
  "followed_by_new_source_login": true
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-id-benign-003",
  "timestamp": "2026-06-19T11:00:00Z",
  "user": "user@example.com",
  "action": "mfa_method_added",
  "ticket_id": "HD-123"
}
```

## Expected False Positives

- helpdesk reset
- new phone enrollment

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

The helpdesk ticket is usually the deciding context.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-IDENTITY-MFA_METHOD_CHANGE_FOLLOWED_BY_LOGIN
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
