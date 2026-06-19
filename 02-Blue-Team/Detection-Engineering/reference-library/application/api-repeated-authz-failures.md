---
title: Repeated API Authorization Failures
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, application, reference]
difficulty: advanced
safe_publication: true
---


# Repeated API Authorization Failures

## Detection ID

```text
DET-APPLICATION-API_REPEATED_AUTHZ_FAILURES
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Authorization probing may produce repeated denials across objects or actions.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `application_audit_logs`

Required fields:

- `timestamp`
- `actor`
- `endpoint`
- `result`
- `reason`

## Normalized Logic

```text
denials by actor and distinct_object_ids exceed threshold
```

## Positive Sample Event

```json
{
  "event_id": "evt-app-006",
  "actor": "user@example.com",
  "denials_10m": 75,
  "distinct_object_ids": 70
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-app-benign-006",
  "actor": "qa-automation",
  "denials_10m": 100,
  "test_run": true
}
```

## Expected False Positives

- automated tests

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

Distinct object count is better than raw denial count.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-APPLICATION-API_REPEATED_AUTHZ_FAILURES
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
