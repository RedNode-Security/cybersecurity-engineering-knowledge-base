---
title: API Threat Model Example
domain: application-security
category: api-security
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [api-security, threat-modeling, authorization]
difficulty: intermediate
safe_publication: true
---


# API Threat Model Example

## Scenario

A multi-tenant project management API allows users to view projects, invoices,
and team members.

Example endpoint:

```text
GET /api/v1/projects/{project_id}/invoices
```

## Assets

| Asset | Sensitivity |
|---|---|
| Project data | Internal business data |
| Invoices | Financial data |
| User profiles | Personal data |
| Admin settings | High impact configuration |
| API tokens | Authentication secrets |

## Trust Boundaries

```text
Client → API Gateway → Application Service → Authorization Layer → Database
```

## Abuse Case — Broken Object Level Authorization

Risk:

```text
A user changes project_id in the URL and accesses another tenant's invoices.
```

Secure design:

- Authenticate the caller.
- Resolve caller tenant and role server-side.
- Check whether `project_id` belongs to caller tenant.
- Check whether caller role can view invoices.
- Log allowed and denied sensitive access.

## Authorization Pseudocode

```text
caller = authenticate(request)
project = get_project(project_id)

if project.tenant_id != caller.tenant_id:
    deny_and_log("cross_tenant_access_attempt")

if not caller.has_permission("invoice:read", project_id):
    deny_and_log("missing_invoice_permission")

return invoices
```

## Detection Ideas

- Many 403 responses across different object IDs.
- Sequential object ID access attempts.
- Cross-tenant authorization failures.
- High-volume invoice export.
- Admin action from unusual source.

## Example Log Event

```json
{
  "timestamp": "2026-06-18T13:00:00Z",
  "request_id": "req-example-001",
  "user_id": "user-123",
  "tenant_id": "tenant-a",
  "endpoint": "/api/v1/projects/project-999/invoices",
  "action": "invoice.read",
  "result": "denied",
  "reason": "cross_tenant_access_attempt",
  "source_ip": "198.51.100.10"
}
```

## Security Requirements

- [ ] Object-level authorization enforced server-side.
- [ ] Tenant ID never trusted from client input alone.
- [ ] Sensitive access is logged.
- [ ] API tokens are scoped.
- [ ] Rate limits exist for sensitive endpoints.
- [ ] Tests cover cross-tenant access attempts.

## References

- OWASP API Security Top 10: https://owasp.org/API-Security/
