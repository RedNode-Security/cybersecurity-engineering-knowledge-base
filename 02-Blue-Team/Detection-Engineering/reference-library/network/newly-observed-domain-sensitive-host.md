---
title: Newly Observed Domain From Sensitive Host
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, network, reference]
difficulty: advanced
safe_publication: true
---


# Newly Observed Domain From Sensitive Host

## Detection ID

```text
DET-NETWORK-NEWLY_OBSERVED_DOMAIN_SENSITIVE_HOST
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Sensitive hosts contacting newly observed domains may indicate compromise.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `dns_logs`, `asset_inventory`

Required fields:

- `timestamp`
- `host`
- `query`

## Normalized Logic

```text
dns query first_seen and asset_criticality high
```

## Positive Sample Event

```json
{
  "event_id": "evt-net-001",
  "host": "db01",
  "query": "new-domain.example.invalid",
  "first_seen_env": true
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-net-benign-001",
  "host": "dev01",
  "query": "new-package-repo.example.com",
  "business_context": "developer"
}
```

## Expected False Positives

- software updates
- developer tools

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

Internal first-seen is often more useful than global domain age.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-NETWORK-NEWLY_OBSERVED_DOMAIN_SENSITIVE_HOST
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
