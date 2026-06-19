---
title: Password Spray Followed by Success
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, identity, reference]
difficulty: advanced
safe_publication: true
---


# Password Spray Followed by Success

## Detection ID

```text
DET-IDENTITY-PASSWORD_SPRAY_FOLLOWED_BY_SUCCESS
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Password spraying may show many users failing from one source followed by at least one success.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `identity_signin_logs`

Required fields:

- `timestamp`
- `source_ip`
- `user`
- `result`
- `mfa_result`

## Normalized Logic

```text
count_distinct(user failures by source_ip over 15m) >= 20 and success from same source within 30m
```

## Positive Sample Event

```json
{
  "event_id": "evt-id-001",
  "timestamp": "2026-06-19T08:08:00Z",
  "source_ip": "203.0.113.10",
  "user": "user2@example.com",
  "result": "success",
  "prior_failures_distinct_users_15m": 32,
  "mfa_result": "approved"
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-id-benign-001",
  "timestamp": "2026-06-19T09:00:00Z",
  "source_ip": "198.51.100.5",
  "user": "scanner@example.com",
  "result": "failure",
  "known_scanner": true
}
```

## Expected False Positives

- vulnerability scanner
- misconfigured service
- shared VPN egress

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

Do not page on failure count alone if the source is a known scanner. The success event is what changes the urgency.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-IDENTITY-PASSWORD_SPRAY_FOLLOWED_BY_SUCCESS
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
