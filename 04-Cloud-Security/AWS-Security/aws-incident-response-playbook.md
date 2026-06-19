---
title: AWS Incident Response Playbook
domain: cloud-security
category: aws-security
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [aws, incident-response, cloudtrail]
difficulty: advanced
safe_publication: true
---


# AWS Incident Response Playbook

## Objective

Guide responders through investigation and containment of suspected AWS account
or IAM compromise.

## Trigger Conditions

- Root account use
- New access key for unusual identity
- Admin policy attachment
- CloudTrail stopped or modified
- Unusual role assumption
- Public exposure change
- GuardDuty or SIEM high-severity alert

## Initial Triage

1. Identify account ID, region, actor ARN, source IP, and event name.
2. Review CloudTrail events 24 hours before and after.
3. Determine whether actor is human, role, service, or workload.
4. Check for new keys, policies, users, roles, and trust policy changes.
5. Review logging, security tooling, and network changes.
6. Identify affected resources and data.

## Containment Options

- Disable suspicious access key.
- Revoke or restrict role trust policy.
- Detach unauthorized policy.
- Restore CloudTrail configuration.
- Restrict public security group or bucket policy.
- Rotate exposed secrets.
- Preserve logs in a secure account.

## Evidence Sources

| Evidence | Use |
|---|---|
| CloudTrail | Control-plane timeline |
| IAM credential report | Key age and usage |
| GuardDuty | Threat findings |
| VPC Flow Logs | Network activity |
| S3 access logs | Object access |
| Config history | Resource configuration changes |

## Post-Incident Improvements

- Add SCP guardrails.
- Reduce standing privilege.
- Add CloudTrail tampering alerts.
- Monitor new access keys.
- Require ticket ID for admin role activation.
- Improve account and resource tagging.
