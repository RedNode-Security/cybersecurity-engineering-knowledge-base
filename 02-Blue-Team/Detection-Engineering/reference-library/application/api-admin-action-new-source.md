---
title: API Admin Action from New Source
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, application, reference]
difficulty: advanced
safe_publication: true
---


# API Admin Action from New Source

## Detection ID

```text
DET-APPLICATION-API_ADMIN_ACTION_NEW_SOURCE
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Admin API actions from new sources may indicate account misuse.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `application_audit_logs`

Required fields:

- `timestamp`
- `actor`
- `source_ip`
- `action`

## Normalized Logic

```text
admin action and source first_seen for actor
```

## Positive Sample Event

```json
{
  "event_id": "evt-app-003",
  "actor": "admin@example.com",
  "source_seen_first_time": true,
  "action": "Create API token"
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-app-benign-003",
  "actor": "admin@example.com",
  "source_seen_first_time": true,
  "vpn_change": true
}
```

## Expected False Positives

- VPN egress change

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

The first sensitive action after login is often more important than the login itself.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-APPLICATION-API_ADMIN_ACTION_NEW_SOURCE
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
