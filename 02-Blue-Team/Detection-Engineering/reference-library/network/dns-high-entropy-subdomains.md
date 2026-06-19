---
title: High Entropy DNS Subdomains
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, network, reference]
difficulty: advanced
safe_publication: true
---


# High Entropy DNS Subdomains

## Detection ID

```text
DET-NETWORK-DNS_HIGH_ENTROPY_SUBDOMAINS
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

DNS tunneling suspicion may show high entropy or long labels.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `dns_logs`

Required fields:

- `timestamp`
- `client`
- `query`

## Normalized Logic

```text
long_or_high_entropy_labels and high_query_volume
```

## Positive Sample Event

```json
{
  "event_id": "evt-net-002",
  "client": "host01",
  "query": "a8f3k2l9s0.example.invalid",
  "label_entropy": "high",
  "query_count_10m": 300
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-net-benign-002",
  "client": "host02",
  "query": "cdn-shard-123.example.com",
  "known_service": true
}
```

## Expected False Positives

- CDN
- telemetry agents

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

This needs careful tuning. CDNs and telemetry can look strange.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-NETWORK-DNS_HIGH_ENTROPY_SUBDOMAINS
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
