---
title: Account Compromise Response
description: A practical reference for investigating and containing suspected account compromise.
status: published
created: 2026-06-19
updated: 2026-06-19
tags: [incident-response, identity, account-compromise]
safe_publication: true
---

# Account Compromise Response

## What it is

Account compromise means an identity is being used by someone who should not have
control of it. The account may be a normal user, privileged user, cloud identity,
service account, or SaaS identity.

The sign-in event is only the beginning of the investigation. The real question
is what the account did after access.

## Common incident pattern

```text
Suspicious sign-in → MFA event → token/session use → sensitive access → privilege or configuration change
```

## Initial questions

- Which account is involved?
- Is the account privileged?
- What source, device, and application were used?
- Was MFA challenged and satisfied?
- What actions happened after sign-in?
- Was data accessed, changed, exported, or deleted?
- Are other accounts affected?

## Evidence matrix

| Evidence | Why it matters |
|---|---|
| Sign-in logs | Establish access timeline and source context |
| MFA logs | Show challenge, approval, denial, or method changes |
| Session and token logs | Show continued access after login |
| Admin audit logs | Reveal privilege and configuration changes |
| Mailbox or file audit logs | Reveal data access or forwarding |
| Endpoint telemetry | Shows whether the source device is compromised |
| User interview | Confirms whether activity was expected |

## Containment decision model

| Finding | Suggested action |
|---|---|
| Suspicious login only, no impact | Monitor, verify user, increase watch |
| Suspicious login and user denies activity | Revoke sessions and reset password |
| MFA method changed unexpectedly | Reset password and require MFA re-registration |
| Privilege changed | Remove unauthorized privilege and preserve audit logs |
| OAuth grant suspicious | Revoke grant and review data accessed |
| Endpoint compromise suspected | Isolate endpoint and start endpoint IR |

## Example timeline

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

## Recovery criteria

An account can return to normal use when:

- Password or credential reset is complete.
- MFA methods are verified.
- Unauthorized sessions and tokens are revoked.
- Unauthorized privileges are removed.
- Suspicious grants, keys, or mailbox rules are removed.
- Scope review is complete or residual risk is accepted.

## Related source files

- [Full account compromise playbook](https://github.com/RedNode-Security/cybersecurity-engineering-handbook/blob/main/02-Blue-Team/Incident-Response/account-compromise-playbook.md)
- [Example account compromise case](https://github.com/RedNode-Security/cybersecurity-engineering-handbook/blob/main/02-Blue-Team/Incident-Response/example-account-compromise-case.md)
