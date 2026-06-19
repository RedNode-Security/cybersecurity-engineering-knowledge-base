# 05 — Application Security

## Purpose

Application security reduces risk across design, implementation, testing,
deployment, and monitoring. This section emphasizes secure engineering patterns
that can be applied by developers, AppSec teams, and defenders.

## AppSec Operating Model

```text
Requirements → Threat Model → Secure Design → Implementation → Testing → Deployment → Monitoring → Feedback
```

## Detailed Pages

- [API Security Overview](API-Security/README.md)
- [API Security Checklist](API-Security/api-security-checklist.md)
- [API Threat Model Example](API-Security/api-threat-model-example.md)

## Example AppSec Question

For a multi-tenant API endpoint like:

```text
GET /api/v1/projects/{project_id}/invoices
```

Ask:

- Is the caller authenticated?
- Is the caller authorized for this specific `project_id`?
- Is tenant ownership checked server-side?
- Are failed authorization checks logged?
- Can repeated object access attempts be detected?
- Are response fields minimized?

## AppSec Quality Standard

Application security pages should include:

- Threat model
- Abuse cases
- Secure design controls
- Testing strategy
- Logging and detection opportunities
- Concrete examples
