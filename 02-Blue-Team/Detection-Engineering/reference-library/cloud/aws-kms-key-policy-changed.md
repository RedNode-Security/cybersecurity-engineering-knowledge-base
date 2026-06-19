---
title: AWS KMS Key Policy Changed
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, cloud, reference]
difficulty: advanced
safe_publication: true
---


# AWS KMS Key Policy Changed

## Detection ID

```text
DET-CLOUD-AWS_KMS_KEY_POLICY_CHANGED
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Key policy changes can affect access to encrypted data.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `aws_cloudtrail`

Required fields:

- `eventTime`
- `eventName`
- `keyId`
- `actor`

## Normalized Logic

```text
PutKeyPolicy on sensitive key by unexpected actor
```

## Positive Sample Event

```json
{
  "event_id": "evt-cloud-007",
  "eventName": "PutKeyPolicy",
  "key_classification": "sensitive",
  "actor": "user"
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-cloud-benign-007",
  "eventName": "PutKeyPolicy",
  "actor": "kms-admin",
  "change_id": "CHG-14"
}
```

## Expected False Positives

- key administration

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

Look for new external principals in the policy.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-CLOUD-AWS_KMS_KEY_POLICY_CHANGED
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
