---
title: Cloud Detection References
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, cloud, index]
difficulty: advanced
safe_publication: true
---


# Cloud Detection References

## Purpose

This folder contains platform-neutral reference detections for the `cloud`
domain. Each page includes a hypothesis, telemetry contract, sample data, false
positives, triage, response guidance, and test case mapping.

## Detections

- [AWS Access Key Created for Rare User](aws-rare-access-key-created.md)
- [AWS Administrator Policy Attachment](aws-admin-policy-attachment.md)
- [AWS CloudTrail Logging Tampering](aws-cloudtrail-tampering.md)
- [AWS GuardDuty Disabled](aws-guardduty-disabled.md)
- [AWS KMS Key Policy Changed](aws-kms-key-policy-changed.md)
- [AWS Root Account Use](aws-root-account-use.md)
- [AWS S3 Public Access Block Disabled](aws-s3-public-access-block-disabled.md)
- [AWS Security Group Admin Port Opened Publicly](aws-public-security-group-admin-port.md)
- [Azure Conditional Access Policy Disabled](azure-conditional-access-disabled.md)
- [Azure High-Risk App Consent](azure-high-risk-app-consent.md)
- [Azure Privileged Role Assignment](azure-privileged-role-assignment.md)
- [Azure Service Principal Credential Added](azure-service-principal-credential-added.md)
