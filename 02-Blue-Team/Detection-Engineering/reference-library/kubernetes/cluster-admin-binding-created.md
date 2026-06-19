---
title: Kubernetes Cluster Admin Binding Created
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, kubernetes, reference]
difficulty: advanced
safe_publication: true
---


# Kubernetes Cluster Admin Binding Created

## Detection ID

```text
DET-KUBERNETES-CLUSTER_ADMIN_BINDING_CREATED
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Privilege escalation may involve creating cluster-admin role bindings.

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
- `role`

## Normalized Logic

```text
create rolebinding/clusterrolebinding with cluster-admin
```

## Positive Sample Event

```json
{
  "event_id": "evt-k8s-001",
  "verb": "create",
  "resource": "clusterrolebinding",
  "role": "cluster-admin",
  "actor": "user@example.com"
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-k8s-benign-001",
  "verb": "create",
  "resource": "clusterrolebinding",
  "role": "view",
  "actor": "cluster-bootstrap",
  "approved": true
}
```

## Expected False Positives

- cluster bootstrap

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

Namespace and actor determine urgency.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-KUBERNETES-CLUSTER_ADMIN_BINDING_CREATED
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
