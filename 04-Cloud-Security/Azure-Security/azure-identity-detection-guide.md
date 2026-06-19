---
title: Azure Identity Detection Guide
domain: cloud-security
category: azure-security
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [azure, identity, detection, cloud]
difficulty: advanced
safe_publication: true
---


# Azure Identity Detection Guide

## Overview

Azure and Entra ID identity logs reveal risky sign-ins, privilege changes,
application consent, role assignments, and tenant-level configuration changes.

## Important Data Sources

| Source | Use |
|---|---|
| Sign-in logs | User and service principal authentication |
| Audit logs | Directory, application, and policy changes |
| Risky users | Identity protection risk context |
| Service principal sign-ins | Workload identity activity |
| Azure activity logs | Subscription control-plane actions |

## Detection Ideas

| Behavior | Example signal |
|---|---|
| Privileged role assignment | directory role assignment added |
| Suspicious app consent | high-risk OAuth permissions granted |
| MFA method change | authentication method updated |
| Risky sign-in followed by admin action | sign-in risk joined to audit log |
| Service principal credential added | new password or certificate credential |

## Example Correlation

```text
risky_signin(user)
JOIN audit_logs(actor=user) WITHIN 60 minutes
WHERE action IN privileged_directory_actions
```

## Triage Questions

- Was the user expected to perform the action?
- Was MFA satisfied?
- Was the device compliant?
- Was the app publisher verified?
- Which permissions were granted?
- Did the actor access sensitive resources afterward?

## Response Actions

- Revoke sessions.
- Reset password.
- Require MFA re-registration.
- Remove unauthorized role assignment.
- Revoke suspicious app consent.
- Review service principal credentials.

## Automation Ideas

- Enrich alerts with role criticality.
- Alert on new app consent requiring high-risk scopes.
- Create weekly report of new service principal credentials.
- Track privileged role assignments without ticket IDs.
