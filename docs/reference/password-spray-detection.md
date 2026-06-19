---
title: Password Spray Detection
description: A practical reference for detecting and triaging password spraying.
status: published
created: 2026-06-19
updated: 2026-06-19
tags: [detection, identity, password-spray]
safe_publication: true
---

# Password Spray Detection

## What it is

Password spraying is an authentication attack pattern where the same small set of
passwords is tried across many accounts. It is different from a classic brute
force attack, where many passwords are tried against one account.

The defensive problem is that spraying often tries to stay below account lockout
thresholds. That means a simple “many failures for one user” alert may miss it.

## Detection hypothesis

If password spraying occurs, authentication logs may show many distinct users
with failed logons from a shared source over a short time window. A successful
login from the same source after the failures makes the case more urgent.

## Required telemetry

| Source | Required fields |
|---|---|
| Identity provider sign-ins | timestamp, user, source IP, result, application, MFA result |
| VPN logs | source IP, username, result, user agent if available |
| Windows authentication logs | event ID, user, source workstation or IP, result |
| Identity inventory | privileged status, account type, department |

## Platform-neutral logic

```text
Group failed authentication events by source IP over 15 minutes.
Alert when distinct users >= 20 and failures per user remain low.
Raise severity if a successful login appears from the same source within 30 minutes.
```

## Positive example

```json
{
  "timestamp": "2026-06-19T08:08:00Z",
  "source_ip": "203.0.113.10",
  "user": "user2@example.com",
  "result": "success",
  "prior_failures_distinct_users_15m": 32,
  "mfa_result": "approved"
}
```

## Common false positives

- Vulnerability scanners using domain credentials
- Misconfigured services retrying authentication
- Shared VPN or proxy egress
- Password rollout or identity migration issues
- Legacy applications with retry behavior

## Triage workflow

1. Identify the source IP, user count, and time window.
2. Check whether the source is a known scanner, VPN, proxy, or corporate service.
3. Identify whether any authentication succeeded.
4. Check whether affected users include privileged accounts.
5. Review MFA results for successful logons.
6. Review activity after any success: mailbox access, admin actions, cloud actions, or endpoint activity.
7. Escalate if a success occurred and business context does not explain it.

## Response guidance

- Revoke sessions for confirmed compromised users.
- Reset credentials if compromise is confirmed.
- Require MFA re-registration if MFA abuse is suspected.
- Hunt for the same source across other applications.
- Review targeted users for shared traits such as department or role.

## Analyst note

Do not page on failure volume alone if the source is a known scanner. The moment
a failure pattern is followed by a successful login, the priority changes.

## Related source files

- [Detection reference page](https://github.com/RedNode-Security/cybersecurity-engineering-handbook/blob/main/02-Blue-Team/Detection-Engineering/reference-library/identity/password-spray-followed-by-success.md)
- [Detection metadata](https://github.com/RedNode-Security/cybersecurity-engineering-handbook/blob/main/02-Blue-Team/Detection-Engineering/rules/identity/password-spray-followed-by-success.json)
- [Detection test cases](https://github.com/RedNode-Security/cybersecurity-engineering-handbook/blob/main/02-Blue-Team/Detection-Engineering/test-cases/detection-test-cases.json)
