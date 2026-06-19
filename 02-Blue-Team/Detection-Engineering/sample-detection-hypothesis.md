---
title: Sample Detection Hypothesis
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [detection, hypothesis]
difficulty: beginner
safe_publication: true
---


# Sample Detection Hypothesis

## Scenario

A user account may be compromised and used to perform sensitive activity after an
unusual sign-in.

## Hypothesis

If an account is misused after credential theft, identity and audit logs may show
unusual authentication context followed by privileged or sensitive actions.

## Required Telemetry

| Source | Required fields |
|---|---|
| IdP sign-in logs | user, source IP, device, MFA, result, application |
| Admin audit logs | actor, action, target, result, timestamp |
| Asset inventory | asset, owner, criticality, environment |
| User directory | department, role, privileged status |

## Logic Sketch

```text
WHERE sign_in.source_is_new_for_user = true
AND sign_in.result = success
JOIN admin_audit ON user WITHIN 30 minutes
WHERE admin_audit.action IN privileged_actions
```

## Example Synthetic Timeline

| Time | Event |
|---|---|
| 09:12 | User signs in from new source IP |
| 09:13 | MFA approved |
| 09:18 | User activates admin role |
| 09:21 | User creates access key |
| 09:31 | Detection fires |

## False Positives

- Travel
- VPN egress change
- New device
- Planned admin maintenance
- Emergency access test
- Role change or onboarding

## Triage Steps

1. Confirm user and source context.
2. Check MFA method and device health.
3. Review privileged actions.
4. Check change ticket.
5. Contact user through approved channel if needed.
6. Escalate if unexplained.

## Response Options

- Revoke sessions.
- Reset password.
- Require MFA re-registration.
- Remove unauthorized privilege.
- Disable newly created keys.
- Preserve logs.
