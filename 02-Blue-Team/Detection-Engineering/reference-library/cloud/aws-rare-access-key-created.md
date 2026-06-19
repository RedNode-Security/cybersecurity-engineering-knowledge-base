---
title: AWS Access Key Created for Rare User
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, cloud, reference]
difficulty: advanced
safe_publication: true
---


# AWS Access Key Created for Rare User

## Detection ID

```text
DET-CLOUD-AWS_RARE_ACCESS_KEY_CREATED
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Persistence may involve new access key creation for a rarely used identity.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `aws_cloudtrail`, `identity_inventory`

Required fields:

- `eventTime`
- `eventName`
- `userIdentity.arn`

## Normalized Logic

```text
CreateAccessKey and rare_for_identity
```

## Positive Sample Event

```json
{
  "event_id": "evt-cloud-002",
  "eventName": "CreateAccessKey",
  "user": "example-user",
  "key_creation_count_90d": 0
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-cloud-benign-002",
  "eventName": "CreateAccessKey",
  "user": "deploy-svc",
  "rotation_ticket": "CHG-10"
}
```

## Expected False Positives

- key rotation
- new workload

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

Review what the key did after creation.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-CLOUD-AWS_RARE_ACCESS_KEY_CREATED
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
