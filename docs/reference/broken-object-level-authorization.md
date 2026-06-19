---
title: Broken Object Level Authorization
description: Defensive design, testing, logging, and detection for BOLA.
status: published
created: 2026-06-19
updated: 2026-06-19
tags: [api-security, authorization, bola]
safe_publication: true
---

# Broken Object Level Authorization

## What it is

Broken Object Level Authorization, or BOLA, happens when an API verifies that a
caller is authenticated but fails to verify that the caller is allowed to access
the specific object requested.

Authentication answers:

```text
Who are you?
```

Object-level authorization answers:

```text
Are you allowed to perform this action on this object?
```

A valid token does not prove object access.

## Example endpoint

```text
GET /api/v1/projects/{project_id}/invoices
```

The server must verify that the authenticated caller is allowed to access that
specific `project_id` and invoice set.

## Secure pattern

```text
caller = authenticate(request)
project = load_project(project_id)

if project.tenant_id != caller.tenant_id:
    deny_and_log("cross_tenant_access_attempt")

if not allowed(caller, "invoice.read", project):
    deny_and_log("missing_permission")

return invoices
```

## Detection ideas

- Many denied object accesses by one user.
- Sequential or high-volume object ID probing.
- Cross-tenant denial patterns.
- Denied access followed by successful access to a sensitive object.
- High-volume export from a rarely used account.

## Logging requirements

Log authorization denials with:

- request ID,
- actor ID,
- tenant ID,
- object ID or safe object reference,
- action,
- decision,
- denial reason,
- source context.

Do not log full tokens, secrets, or sensitive payloads.

## Related source file

- [Broken Object Level Authorization Reference](https://github.com/RedNode-Security/cybersecurity-engineering-handbook/blob/main/05-Application-Security/API-Security/reference-broken-object-level-authorization.md)
