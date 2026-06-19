---
title: Archive Created Before Large Upload
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, windows, reference]
difficulty: advanced
safe_publication: true
---


# Archive Created Before Large Upload

## Detection ID

```text
DET-WINDOWS-ARCHIVE_CREATED_BEFORE_UPLOAD
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Data staging may involve archive creation followed by upload.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `edr_file_events`, `proxy_logs`

Required fields:

- `timestamp`
- `host`
- `archive_path`
- `bytes_out`

## Normalized Logic

```text
archive_created join large_upload within 30m
```

## Positive Sample Event

```json
{
  "event_id": "evt-win-011",
  "host": "file01",
  "archive_created": true,
  "bytes_out_30m": 900000000,
  "destination_rare": true
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-win-benign-011",
  "host": "file01",
  "archive_created": true,
  "backup_job": true
}
```

## Expected False Positives

- backup job
- approved export

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

This is a correlation detection. Alone, archive creation is usually not enough.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-WINDOWS-ARCHIVE_CREATED_BEFORE_UPLOAD
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
