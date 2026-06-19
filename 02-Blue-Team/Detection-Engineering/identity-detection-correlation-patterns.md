---
title: Identity Detection Correlation Patterns
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [identity, correlation, detection]
difficulty: advanced
safe_publication: true
---


# Identity Detection Correlation Patterns

## Overview

Identity attacks rarely appear as one perfect event. They appear as sequences:
failed logons, MFA changes, role activations, token grants, device changes, and
sensitive access. Correlation raises confidence.

## Core Correlation Windows

| Pattern | Window | Example |
|---|---|---|
| Failed logons followed by success | 30 minutes | Password spray succeeds |
| Risky sign-in followed by privilege | 60 minutes | Account misuse |
| MFA reset followed by sign-in | 24 hours | Helpdesk abuse or account takeover |
| OAuth grant followed by mailbox access | 24 hours | Malicious app consent |
| New device followed by sensitive access | 24 hours | Session hijack or unmanaged device |

## Pattern 1 — Risky Sign-In → Privileged Action

```text
sign_in.risk = high
JOIN admin_audit.actor = sign_in.user WITHIN 60 minutes
WHERE admin_audit.action IN privileged_actions
```

Triage:

- Was MFA satisfied?
- Is device managed?
- Is source expected?
- Is action approved?
- Is target sensitive?

## Pattern 2 — MFA Method Change → Successful Sign-In

```text
mfa_method_changed(user)
JOIN successful_signin(user) WITHIN 24 hours
WHERE signin.source_is_new = true
```

False positives:

- New phone enrollment
- Helpdesk reset
- Planned authenticator migration

## Pattern 3 — OAuth Consent → Data Access

```text
oauth_grant_created(user, app)
JOIN mailbox_or_file_access(user, app) WITHIN 24 hours
WHERE app.publisher_unverified = true OR scopes_high_risk = true
```

Response:

- Review app scopes.
- Revoke grant if unauthorized.
- Review data accessed by app.
- Search for same app across users.

## Pattern 4 — Password Spray → Privileged User Success

```text
COUNT distinct users failed from source_ip >= 20 WITHIN 15 minutes
JOIN success from same source_ip WITHIN 30 minutes
WHERE success.user_privileged = true
```

Severity:

- Medium if no success.
- High if any success.
- Critical if privileged success and follow-on sensitive action.

## Enrichment Requirements

- User privilege level
- MFA status
- Device compliance
- Source IP reputation and ownership
- Asset criticality
- Change ticket context
- Historical baseline

## Metrics

Track correlation detections separately from single-event detections because they
usually have higher fidelity but more data dependencies.
