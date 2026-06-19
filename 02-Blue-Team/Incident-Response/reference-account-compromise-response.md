---
title: Reference — Account Compromise Response
domain: blue-team
category: incident-response
status: published
created: 2026-06-18
updated: 2026-06-19
tags: [account-compromise, identity, incident-response, reference]
difficulty: advanced
safe_publication: true
---


# Reference — Account Compromise Response

## Scope

This page covers defensive response to suspected account compromise. It focuses
on identity evidence, containment decisions, recovery, and lessons learned.

## Incident Pattern

Account compromise usually becomes visible through a chain of events:

```text
Suspicious sign-in → MFA event → token/session use → sensitive access → privilege or configuration change
```

The sign-in alone may not prove impact. The response team needs to determine what
the account did after access.

## Initial Questions

- Which account is involved?
- Is the account privileged?
- What source, device, and application were used?
- Was MFA challenged and satisfied?
- What actions happened after sign-in?
- Was data accessed, changed, exported, or deleted?
- Are other accounts affected?

## Evidence Matrix

| Evidence | Why it matters |
|---|---|
| Sign-in logs | Establish access timeline |
| MFA logs | Show challenge and method behavior |
| Session/token logs | Show continued access after login |
| Admin audit logs | Reveal privilege and configuration changes |
| Mailbox or file audit logs | Reveal data access or forwarding |
| Endpoint telemetry | Shows source device compromise or tooling |
| User interview | Confirms whether activity is expected |

## Containment Decision Model

| Finding | Suggested action |
|---|---|
| Suspicious login only, no impact | Monitor, verify user, increase watch |
| Suspicious login and user denies activity | Revoke sessions and reset password |
| MFA method changed unexpectedly | Reset password and require MFA re-registration |
| Privilege changed | Remove unauthorized privilege and preserve audit logs |
| OAuth grant suspicious | Revoke grant and review data accessed |
| Endpoint compromise suspected | Isolate endpoint and start endpoint IR |

## Response Timeline Example

```text
09:12 suspicious sign-in from new source
09:13 MFA push approved
09:18 admin role activated
09:21 access key created
09:31 detection fires
09:40 sessions revoked
09:43 password reset
09:50 suspicious access key disabled
10:15 scope review finds no additional accounts
```

## Recovery Criteria

An account can return to normal use when:

- Password or credential reset is complete.
- MFA methods are verified.
- Unauthorized sessions and tokens are revoked.
- Unauthorized privileges are removed.
- Suspicious grants, keys, or mailbox rules are removed.
- Scope review is complete or risk accepted.

## Lessons Learned

Good post-incident questions:

- Why was the account exposed?
- Was MFA effective?
- Were privileges excessive?
- Did the detection fire early enough?
- Were logs sufficient to determine impact?
- Which response step was manual and repeatable?

## References

- NIST SP 800-61 Computer Security Incident Handling Guide: https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final
- Microsoft identity security operations: https://learn.microsoft.com/security/operations/identity-management-accounts-overview
