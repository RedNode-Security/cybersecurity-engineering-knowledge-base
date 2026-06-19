---
title: OAuth and JWT Security Deep Dive
domain: application-security
category: oauth-jwt-security
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [oauth, jwt, api-security, identity]
difficulty: advanced
safe_publication: true
---


# OAuth and JWT Security Deep Dive

## Overview

OAuth and JWT security failures often come from incorrect assumptions: trusting
client input, accepting wrong audiences, skipping issuer checks, confusing
authentication with authorization, or over-scoping tokens.

## JWT Validation Checklist

- [ ] Signature is verified.
- [ ] Algorithm is restricted to expected algorithms.
- [ ] Issuer is trusted.
- [ ] Audience matches this API.
- [ ] Expiration is enforced.
- [ ] Not-before is enforced if used.
- [ ] Scopes or roles are checked for the action.
- [ ] Tenant or organization boundary is validated.
- [ ] Token is not logged in full.

## Common Failure Modes

| Failure | Impact |
|---|---|
| Missing audience validation | Token for one API accepted by another |
| Missing issuer validation | Token from untrusted issuer accepted |
| Scope confusion | User can perform unintended action |
| Tenant confusion | Cross-tenant data exposure |
| Long-lived tokens | Higher impact after theft |
| Logging tokens | Secrets exposed in logs |

## API Authorization Example

```text
Token says: scope=invoice.read tenant=tenant-a
Request says: GET /tenants/tenant-b/invoices
Expected result: deny and log cross-tenant attempt
```

## OAuth Consent Risks

Watch for:

- Unverified app publisher
- High-risk scopes
- Consent granted by privileged user
- App accessing many users' data
- Consent followed by unusual data access

## Detection Ideas

- Token validation failures by issuer or audience.
- Repeated authorization failures across tenants.
- New OAuth grant with high-risk scopes.
- Sensitive API access from unusual client.
- Admin consent outside change window.

## Logging Fields

- Request ID
- Client ID
- User ID
- Tenant ID
- Token issuer
- Token audience
- Scopes used
- Authorization decision
- Denial reason

## References

- OAuth 2.0 Security Best Current Practice: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics
- OWASP API Security: https://owasp.org/API-Security/
