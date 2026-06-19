---
title: Azure Conditional Access Policy Disabled
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, cloud, reference]
difficulty: advanced
safe_publication: true
---


# Azure Conditional Access Policy Disabled

## Detection ID

```text
DET-CLOUD-AZURE_CONDITIONAL_ACCESS_DISABLED
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Identity defense impairment may involve disabling conditional access.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `azure_audit_logs`

Required fields:

- `timestamp`
- `actor`
- `policy`
- `action`

## Normalized Logic

```text
conditional_access disabled by unexpected actor
```

## Positive Sample Event

```json
{
  "event_id": "evt-cloud-012",
  "actor": "user@example.com",
  "action": "Disable conditional access policy",
  "policy": "Require MFA for admins"
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-cloud-benign-012",
  "actor": "identity-admin",
  "action": "Update conditional access policy",
  "change_id": "CHG-17"
}
```

## Expected False Positives

- policy migration

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

This can quickly change tenant risk. Review sign-ins after the change.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-CLOUD-AZURE_CONDITIONAL_ACCESS_DISABLED
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
