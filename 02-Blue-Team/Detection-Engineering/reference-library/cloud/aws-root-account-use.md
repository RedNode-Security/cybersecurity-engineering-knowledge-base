---
title: AWS Root Account Use
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, cloud, reference]
difficulty: advanced
safe_publication: true
---


# AWS Root Account Use

## Detection ID

```text
DET-CLOUD-AWS_ROOT_ACCOUNT_USE
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Root account usage should be rare and emergency-only.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `aws_cloudtrail`

Required fields:

- `eventTime`
- `eventName`
- `userIdentity.type`

## Normalized Logic

```text
userIdentity.type=Root
```

## Positive Sample Event

```json
{
  "event_id": "evt-cloud-001",
  "eventName": "ConsoleLogin",
  "userIdentity": {
    "type": "Root"
  },
  "mfaAuthenticated": true
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-cloud-benign-001",
  "eventName": "ConsoleLogin",
  "userIdentity": {
    "type": "Root"
  },
  "break_glass_test": true
}
```

## Expected False Positives

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

Root use should create a case even if expected.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-CLOUD-AWS_ROOT_ACCOUNT_USE
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
