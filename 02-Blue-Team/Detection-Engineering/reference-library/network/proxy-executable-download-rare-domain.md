---
title: Executable Download From Rare Domain
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, network, reference]
difficulty: advanced
safe_publication: true
---


# Executable Download From Rare Domain

## Detection ID

```text
DET-NETWORK-PROXY_EXECUTABLE_DOWNLOAD_RARE_DOMAIN
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Malware staging may involve executable download from rare domain.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `proxy_logs`, `dns_logs`

Required fields:

- `timestamp`
- `user`
- `url`
- `file_type`

## Normalized Logic

```text
file_type executable and domain_prevalence low
```

## Positive Sample Event

```json
{
  "event_id": "evt-net-003",
  "user": "user@example.com",
  "url": "https://rare.example.invalid/update.exe",
  "file_type": "exe",
  "domain_prevalence": "low"
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-net-benign-003",
  "user": "admin@example.com",
  "url": "https://vendor.example.com/agent.msi",
  "approved_vendor": true
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

Join with endpoint process execution to reduce noise.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-NETWORK-PROXY_EXECUTABLE_DOWNLOAD_RARE_DOMAIN
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
