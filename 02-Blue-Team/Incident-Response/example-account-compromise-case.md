---
title: Example Account Compromise Case
domain: blue-team
category: incident-response
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [incident-response, case-study, identity]
difficulty: intermediate
safe_publication: true
---


# Example Account Compromise Case

## Scenario

This is a synthetic training case showing how to document an account compromise
investigation. All values are examples.

## Alert

```text
Alert: Unusual sign-in followed by privileged action
User: alex.admin@example.com
Source IP: 203.0.113.77
Application: Cloud Admin Portal
Time: 2026-06-18T09:12:00Z
Severity: High
```

## Timeline

| Time UTC | Event | Notes |
|---|---|---|
| 09:12 | Successful sign-in | New source IP and unmanaged device |
| 09:13 | MFA satisfied | Push notification approved |
| 09:18 | Admin role activated | No change ticket found |
| 09:21 | New access key created | Key ID recorded in case evidence |
| 09:25 | Storage bucket listing | Sensitive project bucket accessed |
| 09:31 | Alert triggered | Detection correlated sign-in and privileged action |
| 09:40 | Sessions revoked | Approved by incident lead |
| 09:43 | Password reset | User notified through verified channel |
| 09:50 | Access key disabled | No further API use observed |

## Triage Notes

Findings:

- Source IP was not seen for this user in the previous 90 days.
- Device was not managed.
- Admin role activation had no approved change request.
- User confirmed they were not working at the time.
- New access key performed read-only enumeration before containment.

## Classification

```text
Confirmed incident — account compromise with limited cloud control-plane activity.
```

## Containment Actions

- Revoked active sessions.
- Reset password.
- Required MFA re-registration.
- Disabled newly created access key.
- Removed temporary admin role activation.
- Preserved sign-in and cloud audit logs.

## Scope Review

Hunts performed:

- Same source IP across all users.
- Same user across all applications.
- Access key activity across all regions.
- Privileged role activations in same time window.
- Storage access after suspicious sign-in.

Result:

```text
No additional compromised accounts found. One storage bucket listing occurred; no object download observed in available logs.
```

## Lessons Learned

| Gap | Improvement |
|---|---|
| MFA push could be approved without number matching | Enable stronger MFA method |
| Admin activation lacked ticket correlation | Require ticket ID in privileged access workflow |
| Access key creation did not trigger immediate case | Add high-priority detection |
| User context not auto-enriched | Add identity enrichment to alert pipeline |

## Example Final Summary

```text
On 2026-06-18, alex.admin@example.com experienced account compromise. The actor authenticated from a new unmanaged source, activated an admin role, created an access key, and listed storage resources. The security team revoked sessions, reset credentials, disabled the key, removed unauthorized privilege, and preserved evidence. No additional compromised accounts were identified. Follow-up actions include MFA hardening, privileged access workflow updates, and new access-key detection.
```
