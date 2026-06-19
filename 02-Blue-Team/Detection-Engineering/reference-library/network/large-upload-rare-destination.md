---
title: Large Upload to Rare Destination
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, network, reference]
difficulty: advanced
safe_publication: true
---


# Large Upload to Rare Destination

## Detection ID

```text
DET-NETWORK-LARGE_UPLOAD_RARE_DESTINATION
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Data exfiltration may show large uploads to rare destinations.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `proxy_logs`, `network_flow_logs`

Required fields:

- `timestamp`
- `host`
- `destination`
- `bytes_out`

## Normalized Logic

```text
bytes_out > baseline_p95 and destination rare
```

## Positive Sample Event

```json
{
  "event_id": "evt-net-004",
  "host": "file01",
  "destination": "198.51.100.80",
  "bytes_out": 1200000000,
  "rare_destination": true
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-net-benign-004",
  "host": "file01",
  "destination": "backup.example.com",
  "backup_job": true
}
```

## Expected False Positives

- backup
- approved data transfer

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

Volume only matters when compared to host role and destination history.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-NETWORK-LARGE_UPLOAD_RARE_DESTINATION
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
