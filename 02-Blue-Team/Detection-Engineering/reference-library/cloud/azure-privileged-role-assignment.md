---
title: Azure Privileged Role Assignment
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, cloud, reference]
difficulty: advanced
safe_publication: true
---


# Azure Privileged Role Assignment

## Detection ID

```text
DET-CLOUD-AZURE_PRIVILEGED_ROLE_ASSIGNMENT
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Privilege escalation may involve Azure role assignment.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `azure_audit_logs`

Required fields:

- `timestamp`
- `actor`
- `target`
- `role`

## Normalized Logic

```text
privileged role assignment and missing approval
```

## Positive Sample Event

```json
{
  "event_id": "evt-cloud-011",
  "actor": "user@example.com",
  "target": "temp@example.com",
  "role": "Global Administrator",
  "change_id": null
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-cloud-benign-011",
  "actor": "pim-service",
  "target": "admin@example.com",
  "role": "Reader",
  "approval_id": "PIM-1"
}
```

## Expected False Positives

- PIM activation

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

PIM approval context is the key tuning field.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-CLOUD-AZURE_PRIVILEGED_ROLE_ASSIGNMENT
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
