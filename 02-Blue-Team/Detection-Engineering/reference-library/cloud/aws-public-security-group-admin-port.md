---
title: AWS Security Group Admin Port Opened Publicly
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, cloud, reference]
difficulty: advanced
safe_publication: true
---


# AWS Security Group Admin Port Opened Publicly

## Detection ID

```text
DET-CLOUD-AWS_PUBLIC_SECURITY_GROUP_ADMIN_PORT
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Public admin port exposure increases attack surface.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `aws_cloudtrail`, `cloud_asset_inventory`

Required fields:

- `eventTime`
- `eventName`
- `groupId`
- `cidr`
- `port`

## Normalized Logic

```text
security_group ingress cidr public and port in admin_ports
```

## Positive Sample Event

```json
{
  "event_id": "evt-cloud-008",
  "eventName": "AuthorizeSecurityGroupIngress",
  "cidr": "0.0.0.0/0",
  "port": 22,
  "asset": "prod-admin"
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-cloud-benign-008",
  "eventName": "AuthorizeSecurityGroupIngress",
  "cidr": "198.51.100.0/24",
  "port": 443,
  "change_id": "CHG-15"
}
```

## Expected False Positives

- temporary admin access
- public web service

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

Even short-lived exposure should have an owner and expiration.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-CLOUD-AWS_PUBLIC_SECURITY_GROUP_ADMIN_PORT
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
