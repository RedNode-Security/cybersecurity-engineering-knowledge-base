---
title: Kubernetes Admission Denied Spike
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, kubernetes, reference]
difficulty: advanced
safe_publication: true
---


# Kubernetes Admission Denied Spike

## Detection ID

```text
DET-KUBERNETES-ADMISSION_DENIED_SPIKE
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Repeated denied deployments may indicate probing or misconfigured automation.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `kubernetes_audit_logs`, `admission_controller_logs`

Required fields:

- `timestamp`
- `actor`
- `policy`
- `result`

## Normalized Logic

```text
admission denials by actor exceed baseline
```

## Positive Sample Event

```json
{
  "event_id": "evt-k8s-006",
  "actor": "builder",
  "denied_count_10m": 20,
  "policy": "restricted-pod-security"
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-k8s-benign-006",
  "actor": "ci-system",
  "denied_count_10m": 5,
  "deployment_test": true
}
```

## Expected False Positives

- developer testing
- policy rollout

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

Denials are useful because they show what controls prevented.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-KUBERNETES-ADMISSION_DENIED_SPIKE
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
