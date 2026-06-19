---
title: CloudTrail IAM Detection
description: Defensive detection patterns for suspicious AWS IAM activity.
status: published
created: 2026-06-19
updated: 2026-06-19
tags: [aws, cloudtrail, iam, detection]
safe_publication: true
---

# CloudTrail IAM Detection

## What it is

AWS CloudTrail records control-plane activity. For IAM and cloud incident
response, it is one of the most important evidence sources.

In AWS, identity is the control plane. A compromised principal can create access
keys, attach policies, assume roles, change trust relationships, modify logging,
or access data.

## High-value IAM events

| Event | Why it matters |
|---|---|
| `CreateAccessKey` | Long-lived credential creation |
| `AttachUserPolicy` | Privilege expansion |
| `AttachRolePolicy` | Role privilege expansion |
| `PutUserPolicy` | Inline privilege grant |
| `UpdateAssumeRolePolicy` | Trust relationship change |
| `CreateUser` | New identity creation |
| `CreateLoginProfile` | Console password enabled |
| `StopLogging` | CloudTrail tampering |
| `DeleteTrail` | Logging removal |

## Detection pattern: new access key for rare identity

```text
WHERE eventName = "CreateAccessKey"
JOIN identity_profile ON userIdentity.arn
WHERE key_creation_count_90d = 0 OR last_activity_age_days > 90
```

## Detection pattern: admin policy attachment

```text
WHERE eventName IN ("AttachUserPolicy", "AttachRolePolicy", "PutUserPolicy", "PutRolePolicy")
AND policy indicates broad administrative permission
AND actor is not approved automation
```

## Triage questions

- Which AWS account and region were involved?
- Which principal performed the action?
- Was MFA present for human activity?
- Was there an approved change?
- Was the source IP expected?
- Did follow-on actions occur?
- Did the actor modify logging or security controls?

## Response actions

- Deactivate suspicious access keys.
- Remove unauthorized policies.
- Restore trust policy if changed.
- Preserve CloudTrail logs.
- Review follow-on API activity.
- Hunt across accounts for the same source, user agent, and principal.

## Related source file

- [CloudTrail IAM Detection Reference](https://github.com/RedNode-Security/cybersecurity-engineering-handbook/blob/main/04-Cloud-Security/AWS-Security/reference-cloudtrail-iam-detection.md)
