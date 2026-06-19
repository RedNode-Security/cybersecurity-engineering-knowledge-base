---
title: New Device Sensitive Access
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, identity, reference]
difficulty: advanced
safe_publication: true
---


# New Device Sensitive Access

## Detection ID

```text
DET-IDENTITY-NEW_DEVICE_SENSITIVE_ACCESS
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

New device access to sensitive applications can indicate account misuse.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `identity_signin_logs`, `device_inventory`

Required fields:

- `timestamp`
- `user`
- `device_id`
- `application`

## Normalized Logic

```text
new_device and application in sensitive_apps
```

## Positive Sample Event

```json
{
  "event_id": "evt-id-011",
  "user": "payroll@example.com",
  "device_seen_first_time": true,
  "application": "Payroll Admin"
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-id-benign-011",
  "user": "payroll@example.com",
  "device_seen_first_time": true,
  "device_enrollment_ticket": "IT-500"
}
```

## Expected False Positives

- device replacement
- new hire onboarding

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

Device enrollment data often turns a noisy alert into a useful one.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-IDENTITY-NEW_DEVICE_SENSITIVE_ACCESS
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
