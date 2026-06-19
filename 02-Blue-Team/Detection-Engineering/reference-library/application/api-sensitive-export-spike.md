---
title: API Sensitive Data Export Spike
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, application, reference]
difficulty: advanced
safe_publication: true
---


# API Sensitive Data Export Spike

## Detection ID

```text
DET-APPLICATION-API_SENSITIVE_EXPORT_SPIKE
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Account misuse may produce unusual sensitive data export volume.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `application_audit_logs`

Required fields:

- `timestamp`
- `user`
- `endpoint`
- `record_count`

## Normalized Logic

```text
record_count > baseline_p95 and endpoint sensitive
```

## Positive Sample Event

```json
{
  "event_id": "evt-app-002",
  "user": "analyst@example.com",
  "endpoint": "/export/customers",
  "record_count": 50000,
  "baseline_p95": 1000
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-app-benign-002",
  "user": "reporting-svc",
  "record_count": 60000,
  "scheduled_report": true
}
```

## Expected False Positives

- scheduled reporting

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

Use business calendar context before escalating.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-APPLICATION-API_SENSITIVE_EXPORT_SPIKE
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
