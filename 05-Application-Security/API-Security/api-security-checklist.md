---
title: API Security Checklist
domain: application-security
category: api-security
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [api-security, appsec, secure-design]
difficulty: intermediate
safe_publication: true
---


# API Security Checklist

## Authentication

- [ ] Sensitive endpoints require authentication.
- [ ] Tokens are validated server-side.
- [ ] Issuer, audience, expiry, signature, and algorithm are checked.
- [ ] Administrative actions require strong authentication.
- [ ] Service-to-service credentials are scoped and rotated.

## Authorization

- [ ] Object-level authorization is enforced.
- [ ] Function-level authorization is enforced.
- [ ] Tenant boundaries are tested.
- [ ] Authorization is server-side.
- [ ] Admin APIs are monitored.

## Input and Output

- [ ] Input validation is consistent.
- [ ] Errors do not expose stack traces or secrets.
- [ ] Sensitive fields are minimized.
- [ ] Pagination cannot leak unauthorized records.
- [ ] File uploads are restricted.

## Logging

Log:

- Request ID
- Actor
- Endpoint
- Target object
- Result
- Reason for denial
- Source context

Do not log full tokens, passwords, secrets, or sensitive payloads.

## Detection Ideas

- Repeated 401 or 403 responses.
- Many object IDs accessed by one user.
- Cross-tenant access attempts.
- Sudden export volume increase.
- Admin action outside normal pattern.

## Example Test Case

```text
User from tenant A requests /projects/{tenant-b-project}/invoices.
Expected: 403 or 404, audit log with cross_tenant_access_attempt, no invoice data returned.
```
