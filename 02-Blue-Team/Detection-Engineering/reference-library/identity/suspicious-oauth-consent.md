---
title: Suspicious OAuth Consent
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, identity, reference]
difficulty: advanced
safe_publication: true
---


# Suspicious OAuth Consent

## Detection ID

```text
DET-IDENTITY-SUSPICIOUS_OAUTH_CONSENT
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

OAuth consent abuse may grant high-risk scopes to an untrusted application.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `identity_audit_logs`, `application_audit_logs`

Required fields:

- `timestamp`
- `user`
- `app_id`
- `scopes`
- `publisher`

## Normalized Logic

```text
oauth_consent where high_risk_scope and unverified_publisher
```

## Positive Sample Event

```json
{
  "event_id": "evt-id-004",
  "timestamp": "2026-06-19T12:00:00Z",
  "user": "user@example.com",
  "app_publisher_verified": false,
  "scopes": [
    "Mail.Read",
    "offline_access"
  ],
  "data_access_1h": true
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-id-benign-004",
  "timestamp": "2026-06-19T12:00:00Z",
  "app_publisher_verified": true,
  "approval_id": "APP-55"
}
```

## Expected False Positives

- approved SaaS rollout
- known internal app

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

Review scopes before judging severity. offline access plus mail/files is usually high concern.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-IDENTITY-SUSPICIOUS_OAUTH_CONSENT
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
