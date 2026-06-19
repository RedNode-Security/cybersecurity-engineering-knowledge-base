---
title: Identity Security Detection Deep Dive
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [identity, detection, correlation, deep-dive]
difficulty: advanced
safe_publication: true
---


# Identity Security Detection Deep Dive

## Scope

This page covers identity-centric detection for enterprise environments: sign-ins,
MFA, sessions, OAuth consent, role changes, service principals, and privileged
access. It is defensive and assumes authorized monitoring.

## Core Idea

Identity compromise is rarely proven by one event. It is usually a sequence:

```text
Unusual sign-in → MFA behavior → Token/session use → Privilege or consent change → Sensitive access
```

The best detections correlate weak signals into a stronger story.

## Identity Data Sources

| Source | Useful fields | Common gap |
|---|---|---|
| Sign-in logs | user, source, device, result, MFA, app | Original IP hidden behind VPN |
| MFA logs | method, result, prompt count, registration changes | MFA method not joined to sign-in |
| Audit logs | role changes, app consent, policy changes | Actor and target fields inconsistent |
| Session logs | token creation, revocation, refresh | Not retained long enough |
| Directory data | department, manager, privilege, account type | Stale user attributes |
| PAM logs | role activation, approval, ticket ID | Missing reason or change ID |

## Correlation Patterns

### Risky Sign-in Followed by Privileged Action

```text
risky_signin(user)
JOIN privileged_action(actor=user) WITHIN 60 minutes
WHERE source_is_new = true OR device_unmanaged = true
```

This should be high priority when the action affects identity, logging, cloud
control plane, or sensitive data.

### MFA Reset Followed by New Source Login

```text
mfa_method_changed(user)
JOIN successful_signin(user) WITHIN 24 hours
WHERE source_ip NOT IN user.previous_sources_90d
```

This catches helpdesk abuse, social engineering, or account recovery compromise.

### OAuth Consent Followed by Data Access

```text
oauth_consent_created(user, app)
JOIN data_access(actor=app OR user) WITHIN 24 hours
WHERE scopes include mail, files, directory, or offline_access
```

Investigate app publisher, consent granularity, and whether the user intended the
action.

## False Positive Patterns

| Pattern | How to verify |
|---|---|
| User travel | Confirm travel, VPN, device, and MFA method |
| New phone | Check helpdesk ticket and MFA registration logs |
| Admin maintenance | Check change window and privileged access approval |
| SaaS rollout | Check app owner and consent approval |
| VPN egress change | Compare multiple users from same source |

## Triage Questions

- Is the account privileged?
- Is the device managed?
- Was MFA satisfied or modified?
- What application was accessed first?
- What sensitive action occurred next?
- Was there an approved change?
- Did similar activity affect peer users?

## Response Actions

- Revoke sessions.
- Reset credentials.
- Require MFA re-registration.
- Remove unauthorized role assignments.
- Revoke suspicious app consent.
- Disable suspicious service principal credentials.
- Hunt for similar source, app, or role activity.

## Example Analyst Decision

```text
The alert is suspicious because the user signed in from a new source, approved MFA, created an OAuth grant for an unverified app, and the app accessed mail within 10 minutes. No SaaS rollout or user request exists. Escalate as suspected OAuth consent abuse.
```
