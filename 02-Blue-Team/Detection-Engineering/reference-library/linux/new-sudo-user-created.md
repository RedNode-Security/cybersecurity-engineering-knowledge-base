---
title: New Sudo-Capable User Created
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, linux, reference]
difficulty: advanced
safe_publication: true
---


# New Sudo-Capable User Created

## Detection ID

```text
DET-LINUX-NEW_SUDO_USER_CREATED
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Privilege escalation may involve creating a sudo-capable user.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `linux_auth_logs`, `linux_audit_logs`

Required fields:

- `timestamp`
- `host`
- `actor`
- `target_user`
- `group`

## Normalized Logic

```text
user_created join group_add group in sudo_groups
```

## Positive Sample Event

```json
{
  "event_id": "evt-linux-006",
  "actor": "user",
  "target_user": "tempadmin",
  "group": "sudo",
  "change_id": null
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-linux-benign-006",
  "actor": "provisioning",
  "target_user": "newadmin",
  "group": "sudo",
  "ticket_id": "HR-9"
}
```

## Expected False Positives

- onboarding
- break-glass test

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

Check whether the new user logged in immediately after creation.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-LINUX-NEW_SUDO_USER_CREATED
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
