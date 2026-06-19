---
title: New Service on Sensitive Host
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, windows, reference]
difficulty: advanced
safe_publication: true
---


# New Service on Sensitive Host

## Detection ID

```text
DET-WINDOWS-NEW_SERVICE_SENSITIVE_HOST
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Persistence may involve service creation on sensitive hosts.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `windows_system_events`, `edr_process_events`

Required fields:

- `timestamp`
- `host`
- `service_name`
- `actor`

## Normalized Logic

```text
new_service and host_criticality high and actor not deployment_system
```

## Positive Sample Event

```json
{
  "event_id": "evt-win-004",
  "host": "dc01",
  "service_name": "ExampleSvc",
  "actor": "EXAMPLE\\user",
  "host_criticality": "high"
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-win-benign-004",
  "host": "app01",
  "service_name": "ApprovedAgent",
  "actor": "deploy-svc",
  "change_id": "CHG-3"
}
```

## Expected False Positives

- software deployment

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

Service creation on domain controllers and security servers should be uncommon.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-WINDOWS-NEW_SERVICE_SENSITIVE_HOST
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
