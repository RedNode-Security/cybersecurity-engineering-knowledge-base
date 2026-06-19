---
title: Azure Service Principal Credential Added
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, cloud, reference]
difficulty: advanced
safe_publication: true
---


# Azure Service Principal Credential Added

## Detection ID

```text
DET-CLOUD-AZURE_SERVICE_PRINCIPAL_CREDENTIAL_ADDED
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Persistence may involve adding credentials to service principals.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `azure_audit_logs`

Required fields:

- `timestamp`
- `actor`
- `service_principal`
- `action`

## Normalized Logic

```text
service_principal credential added by unexpected actor
```

## Positive Sample Event

```json
{
  "event_id": "evt-cloud-009",
  "action": "Add service principal credential",
  "actor": "user@example.com",
  "app": "prod-app"
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-cloud-benign-009",
  "action": "Add service principal credential",
  "actor": "automation",
  "rotation_ticket": "CHG-16"
}
```

## Expected False Positives

- credential rotation

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

Check whether the service principal has high privileges.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-CLOUD-AZURE_SERVICE_PRINCIPAL_CREDENTIAL_ADDED
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
