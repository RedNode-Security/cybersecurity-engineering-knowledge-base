---
title: SSH Failures Followed by Success
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, linux, reference]
difficulty: advanced
safe_publication: true
---


# SSH Failures Followed by Success

## Detection ID

```text
DET-LINUX-SSH_FAILURES_FOLLOWED_BY_SUCCESS
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

SSH brute force or spraying may show failures followed by success.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `linux_auth_logs`

Required fields:

- `timestamp`
- `source_ip`
- `user`
- `result`

## Normalized Logic

```text
ssh failures from source >= threshold and success from same source
```

## Positive Sample Event

```json
{
  "event_id": "evt-linux-001",
  "source_ip": "203.0.113.20",
  "failed_users_15m": 18,
  "success_user": "deploy"
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-linux-benign-001",
  "source_ip": "198.51.100.10",
  "known_bastion": true,
  "result": "success"
}
```

## Expected False Positives

- bastion host
- mistyped deployment credential

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

A success after failures changes the investigation from noise to account review.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-LINUX-SSH_FAILURES_FOLLOWED_BY_SUCCESS
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
