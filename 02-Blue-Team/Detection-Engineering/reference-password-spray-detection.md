---
title: Reference — Password Spray Detection
domain: blue-team
category: detection-engineering
status: published
created: 2026-06-18
updated: 2026-06-19
tags: [password-spray, identity, detection, reference]
difficulty: advanced
safe_publication: true
---


# Reference — Password Spray Detection

## Scope

This page covers defensive detection and triage of password spraying. It does not
cover offensive execution, tooling, or evasion.

## What Password Spraying Looks Like

Password spraying is different from a classic brute-force attack. Instead of many
passwords against one account, the actor tries a small number of common or reused
passwords against many accounts. The goal is to avoid lockout thresholds while
finding one valid credential.

## Detection Hypothesis

If password spraying occurs, authentication logs may show many distinct users
with failed logons from a shared source over a short time window, often with a
low number of failures per user. A successful authentication from the same source
after the failures increases severity.

## Required Telemetry

| Source | Required fields |
|---|---|
| IdP sign-in logs | timestamp, user, source IP, result, application, MFA result |
| VPN logs | source IP, username, result, user agent if available |
| Windows domain logs | event ID, user, source workstation/IP, result |
| Asset and identity context | privileged status, department, account type |

## Detection Logic

Pseudocode:

```text
GROUP authentication failures BY source_ip OVER 15 minutes
WHERE distinct(user) >= 20
AND failures_per_user <= 3
OPTIONALLY JOIN successful_logon FROM same source_ip WITHIN 30 minutes
```

## Severity Model

| Condition | Severity |
|---|---|
| Many failures, no success, non-privileged users | Medium |
| Many failures, success for any user | High |
| Success for privileged user | Critical or High depending on follow-on activity |
| Success followed by sensitive access | Critical |

## False Positives

Common benign causes:

- Vulnerability scanners using domain credentials
- Misconfigured service accounts
- Shared VPN or proxy egress
- Password change rollout issues
- Legacy application retry storms
- Identity migration testing

## Triage Workflow

1. Identify the source IP, user count, and time window.
2. Check whether the source is a known scanner, VPN, proxy, or corporate service.
3. Identify whether any authentication succeeded.
4. Check whether affected users include privileged accounts.
5. Review MFA results for successful logons.
6. Review activity after any success: mailbox access, admin actions, cloud actions, endpoint activity.
7. Escalate if success occurred and business context does not explain it.

## Example Analyst Note

```text
Source 203.0.113.50 generated failed logons for 42 users in 12 minutes. One user, b.user@example.com, successfully authenticated after failures. Source is not a known scanner or VPN egress. MFA was satisfied by push notification. User does not recognize the login. Escalated as suspected account compromise.
```

## Response Actions

- Reset affected account credentials if compromise is confirmed.
- Revoke sessions for successful accounts.
- Require MFA re-registration when MFA compromise is suspected.
- Block or challenge source only after confirming business impact.
- Hunt for the same source across other applications.
- Review targeted users for shared attributes such as department or role.

## Automation Guidance

Automate enrichment:

- Source IP ownership
- User privilege level
- MFA result
- Recent successful sign-ins
- Known scanner or VPN classification

Do not automatically disable accounts from failure-only detections unless the
policy has been tested and approved.

## References

- MITRE ATT&CK T1110.003 Password Spraying: https://attack.mitre.org/techniques/T1110/003/
- Microsoft identity monitoring guidance: https://learn.microsoft.com/security/operations/identity-management-accounts-overview
