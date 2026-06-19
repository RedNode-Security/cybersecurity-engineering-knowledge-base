---
title: AWS CloudTrail Detection Examples
domain: cloud-security
category: aws-security
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [aws, cloudtrail, detection, iam]
difficulty: intermediate
safe_publication: true
---


# AWS CloudTrail Detection Examples

## Overview

CloudTrail records AWS control-plane activity. It is one of the most important
sources for detecting IAM misuse, logging tampering, privilege escalation, and
cloud persistence.

## Example 1 — Root Account Usage

### Hypothesis

Root account activity should be rare and emergency-only. Any root use should be
reviewed.

### Event Pattern

```text
userIdentity.type = "Root"
```

### Triage

- What action was performed?
- Was it during an approved emergency procedure?
- What source IP and user agent were used?
- Were any keys created or policies changed afterward?

## Example 2 — Access Key Created

### Hypothesis

Unexpected access key creation can indicate persistence or misuse.

### Event Pattern

```text
eventName = "CreateAccessKey"
```

### Synthetic CloudTrail Event

```json
{
  "eventTime": "2026-06-18T12:00:00Z",
  "eventName": "CreateAccessKey",
  "userIdentity": {
    "type": "IAMUser",
    "arn": "arn:aws:iam::123456789012:user/example-user"
  },
  "sourceIPAddress": "203.0.113.44",
  "userAgent": "signin.amazonaws.com"
}
```

### Triage

- Is this identity expected to create keys?
- Was there a change request?
- Was the source IP normal?
- Did the key perform API calls after creation?
- Does the identity have excessive permissions?

## Example 3 — CloudTrail Tampering

### Hypothesis

An actor may attempt to reduce visibility by modifying CloudTrail.

### Event Names

- `StopLogging`
- `DeleteTrail`
- `UpdateTrail`
- `PutEventSelectors`

### Response

- Preserve existing logs.
- Confirm who performed the change.
- Restore logging.
- Review surrounding IAM and API activity.
- Escalate if unauthorized.

## Example 4 — Privileged Policy Attachment

### Event Names

- `AttachUserPolicy`
- `AttachRolePolicy`
- `PutUserPolicy`
- `PutRolePolicy`

### Detection Logic

```text
WHERE eventName IN privileged_policy_change_events
AND policy_arn CONTAINS "AdministratorAccess"
OR inline_policy grants broad IAM or organization permissions
```

## Automation Ideas

- Enrich events with account owner and environment.
- Compare actor against approved admin list.
- Create cases for root use and logging tampering.
- Auto-tag findings by account criticality.
- Generate weekly report of new keys and admin policy changes.
