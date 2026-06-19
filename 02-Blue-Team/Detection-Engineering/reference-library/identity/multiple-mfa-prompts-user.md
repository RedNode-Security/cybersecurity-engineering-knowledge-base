---
title: Multiple MFA Prompts for User
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, identity, reference]
difficulty: advanced
safe_publication: true
---


# Multiple MFA Prompts for User

## Detection ID

```text
DET-IDENTITY-MULTIPLE_MFA_PROMPTS_USER
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

MFA fatigue attempts may show repeated prompts before approval.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `mfa_logs`

Required fields:

- `timestamp`
- `user`
- `method`
- `result`

## Normalized Logic

```text
mfa_prompt_count(user,10m) >= threshold and final approval
```

## Positive Sample Event

```json
{
  "event_id": "evt-id-009",
  "user": "user@example.com",
  "prompt_count_10m": 9,
  "final_result": "approved"
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-id-benign-009",
  "user": "user@example.com",
  "prompt_count_10m": 2,
  "final_result": "approved"
}
```

## Expected False Positives

- user retrying login
- mobile network issues

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

Repeated prompts become more serious when followed by a new source or sensitive app access.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-IDENTITY-MULTIPLE_MFA_PROMPTS_USER
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
