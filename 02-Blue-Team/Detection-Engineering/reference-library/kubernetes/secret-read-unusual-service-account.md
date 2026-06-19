---
title: Kubernetes Secret Read by Unusual Service Account
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, kubernetes, reference]
difficulty: advanced
safe_publication: true
---


# Kubernetes Secret Read by Unusual Service Account

## Detection ID

```text
DET-KUBERNETES-SECRET_READ_UNUSUAL_SERVICE_ACCOUNT
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Credential access may involve unusual secret reads.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `kubernetes_audit_logs`

Required fields:

- `timestamp`
- `verb`
- `resource`
- `actor`
- `namespace`

## Normalized Logic

```text
get secrets by actor not approved for namespace
```

## Positive Sample Event

```json
{
  "event_id": "evt-k8s-002",
  "verb": "get",
  "resource": "secrets",
  "actor": "system:serviceaccount:default:builder",
  "namespace": "prod"
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-k8s-benign-002",
  "verb": "get",
  "resource": "secrets",
  "actor": "external-secrets-controller",
  "namespace": "prod"
}
```

## Expected False Positives

- secret controller

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

Do not alert on every secret read. Use namespace and service account baseline.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-KUBERNETES-SECRET_READ_UNUSUAL_SERVICE_ACCOUNT
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
