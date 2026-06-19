---
title: AWS IAM Hardening Checklist
domain: cloud-security
category: aws-security
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [aws, iam, cloud, hardening]
difficulty: intermediate
safe_publication: true
---


# AWS IAM Hardening Checklist

## Overview

AWS IAM is the control plane for AWS permissions. Weak IAM design can lead to
unauthorized infrastructure changes, data access, persistence, logging changes,
and cross-account impact.

## Root Account

- [ ] Root account MFA is enabled.
- [ ] Root access keys do not exist.
- [ ] Root usage is monitored.
- [ ] Emergency root access process is documented.
- [ ] Root credentials are not used for daily administration.

## Human Access

- [ ] Federation is used instead of long-lived IAM users.
- [ ] MFA is required for privileged roles.
- [ ] Privileged role assumption is logged.
- [ ] Roles have owners and review dates.
- [ ] Temporary access is preferred over standing admin access.

## Workload Access

- [ ] Workloads use IAM roles, not embedded keys.
- [ ] Trust policies are scoped to expected principals.
- [ ] Cross-account role access is documented.
- [ ] Unused roles are removed.
- [ ] Permission boundaries are used where appropriate.

## Policy Review

Review policies for:

- `Action: *`
- `Resource: *`
- IAM write permissions
- Policy attachment permissions
- Role assumption permissions
- Logging modification permissions
- KMS key administration permissions

## Detection Ideas

| Behavior | Example event |
|---|---|
| Root account used | `ConsoleLogin` with root identity |
| New access key created | `CreateAccessKey` |
| Admin policy attached | `AttachUserPolicy`, `AttachRolePolicy` |
| Trust policy changed | `UpdateAssumeRolePolicy` |
| Logging disabled | `StopLogging`, `DeleteTrail`, `PutEventSelectors` |
| Public access changed | S3 public access block or bucket policy change |

## Response Example — Suspicious Access Key

1. Identify key, user, source IP, and creation time.
2. Confirm whether a deployment or change request explains it.
3. If unauthorized, deactivate the key.
4. Review actions performed with the key.
5. Rotate related secrets if exposure is suspected.
6. Hunt for similar key creation across accounts.

## References

- AWS IAM: https://docs.aws.amazon.com/iam/
- AWS CloudTrail: https://docs.aws.amazon.com/cloudtrail/
- CIS AWS Foundations Benchmark: https://www.cisecurity.org/benchmark/amazon_web_services
