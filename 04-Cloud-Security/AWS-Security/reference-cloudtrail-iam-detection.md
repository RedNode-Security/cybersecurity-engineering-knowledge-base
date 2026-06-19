---
title: Reference — CloudTrail IAM Detection
domain: cloud-security
category: aws-security
status: published
created: 2026-06-18
updated: 2026-06-19
tags: [aws, cloudtrail, iam, detection, reference]
difficulty: advanced
safe_publication: true
---


# Reference — CloudTrail IAM Detection

## Scope

This page covers defensive detection of suspicious IAM activity using AWS
CloudTrail. It focuses on control-plane events, not workload runtime monitoring.

## Why IAM Detection Matters

In AWS, identity is the control plane. A compromised principal can create access
keys, attach policies, assume roles, change trust relationships, disable logging,
modify network exposure, or access data. CloudTrail is the primary evidence
source for many of these actions.

## High-Value IAM Events

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

## Detection Pattern — New Access Key for Rare Identity

Hypothesis:

```text
If an actor creates persistence or prepares API access, CloudTrail may show CreateAccessKey for a user that rarely or never creates keys.
```

Pseudocode:

```text
WHERE eventName = "CreateAccessKey"
JOIN identity_profile ON userIdentity.arn
WHERE identity_profile.key_creation_count_90d = 0
OR identity_profile.last_activity_age_days > 90
```

## Detection Pattern — Admin Policy Attachment

Pseudocode:

```text
WHERE eventName IN ("AttachUserPolicy", "AttachRolePolicy", "PutUserPolicy", "PutRolePolicy")
AND policy indicates broad administrative permission
AND actor NOT IN approved_identity_automation
```

## Triage Questions

- Which account and region were involved?
- Which principal performed the action?
- Was MFA present for human activity?
- Was there an approved change?
- Was the source IP expected?
- Did follow-on actions occur after the IAM change?
- Did the actor modify logging or security controls?

## Response Actions

- Deactivate suspicious access keys.
- Remove unauthorized policies.
- Restore trust policy if changed.
- Preserve CloudTrail logs.
- Review follow-on API activity.
- Hunt across accounts for the same source, user agent, and principal.

## Automation Guidance

Automate enrichment with:

- Account owner
- Environment
- Principal type
- MFA context
- Historical activity
- Known automation roles
- Change ticket metadata

Require approval before disabling production credentials unless incident severity
and business impact are clear.

## References

- AWS CloudTrail documentation: https://docs.aws.amazon.com/cloudtrail/
- AWS IAM documentation: https://docs.aws.amazon.com/iam/
- AWS security incident response guide: https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/welcome.html
