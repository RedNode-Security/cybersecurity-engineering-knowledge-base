---
title: Reference — Broken Object Level Authorization
domain: application-security
category: api-security
status: published
created: 2026-06-18
updated: 2026-06-19
tags: [api-security, bola, authorization, reference]
difficulty: advanced
safe_publication: true
---


# Reference — Broken Object Level Authorization

## Scope

This page covers defensive design, testing, logging, and detection for Broken
Object Level Authorization, often abbreviated BOLA. It is aligned with OWASP API
Security API1:2023.

## What BOLA Means

BOLA occurs when an API verifies that a caller is authenticated but fails to
verify that the caller is allowed to access the specific object requested.

Example pattern:

```text
GET /api/v1/projects/{project_id}/invoices
```

The caller may be a valid user, but the server still needs to verify that the
requested `project_id` belongs to the caller's tenant or permission boundary.

## Why Authentication Is Not Enough

Authentication answers:

```text
Who are you?
```

Object-level authorization answers:

```text
Are you allowed to perform this action on this object?
```

A valid token does not prove object access.

## Secure Authorization Pattern

```text
caller = authenticate(request)
project = load_project(project_id)

if project.tenant_id != caller.tenant_id:
    deny_and_log("cross_tenant_access_attempt")

if not allowed(caller, "invoice.read", project):
    deny_and_log("missing_permission")

return invoices
```

## Testing Strategy

Test with at least two users and two tenants:

| Test | Expected result |
|---|---|
| User A accesses own object | Allowed |
| User A accesses User B object in same tenant without permission | Denied |
| User A accesses Tenant B object | Denied |
| Admin accesses authorized tenant object | Allowed if policy permits |
| Disabled user accesses any object | Denied |

## Logging Requirements

Log authorization denials with:

- Request ID
- Actor ID
- Tenant ID
- Object ID or safe object reference
- Action
- Decision
- Denial reason
- Source context

Do not log full tokens, secrets, or sensitive payloads.

## Detection Ideas

- Many denied object accesses by one user.
- Sequential or high-volume object ID probing.
- Cross-tenant denial patterns.
- Denied access followed by successful access to a sensitive object.
- High-volume export from a rarely used account.

## References

- OWASP API1:2023 Broken Object Level Authorization: https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/
- OWASP Authorization Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html
- CWE-639 Authorization Bypass Through User-Controlled Key: https://cwe.mitre.org/data/definitions/639.html
