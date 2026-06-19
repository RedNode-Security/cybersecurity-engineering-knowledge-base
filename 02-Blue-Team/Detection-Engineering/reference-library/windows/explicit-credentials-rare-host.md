---
title: Explicit Credentials Used on Rare Host
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, windows, reference]
difficulty: advanced
safe_publication: true
---


# Explicit Credentials Used on Rare Host

## Detection ID

```text
DET-WINDOWS-EXPLICIT_CREDENTIALS_RARE_HOST
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Lateral movement may involve explicit credential use on unusual hosts.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `windows_security_events`

Required fields:

- `timestamp`
- `event_id`
- `user`
- `host`
- `target_host`

## Normalized Logic

```text
event_id=4648 and target_host rare for user
```

## Positive Sample Event

```json
{
  "event_id": "evt-win-002",
  "windows_event_id": 4648,
  "user": "EXAMPLE\\admin",
  "target_host": "db01",
  "rare_for_user": true
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-win-benign-002",
  "windows_event_id": 4648,
  "user": "EXAMPLE\\admin",
  "target_host": "jump01",
  "approved": true
}
```

## Expected False Positives

- admin support session

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

Explicit credential use is common for admins. Rarity and destination criticality make it useful.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-WINDOWS-EXPLICIT_CREDENTIALS_RARE_HOST
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
