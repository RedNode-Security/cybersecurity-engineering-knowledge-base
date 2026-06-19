---
title: API Logging and Detection Standard
domain: application-security
category: api-security
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [api, logging, detection, standard]
difficulty: advanced
safe_publication: true
---


# API Logging and Detection Standard

## Scope

This page defines the minimum audit logging needed to detect and investigate API
misuse without storing unnecessary sensitive data.

## Required Fields

| Field | Why it matters |
|---|---|
| timestamp | Timeline construction |
| request_id | Cross-service correlation |
| actor_id | User or client identity |
| tenant_id | Tenant boundary checks |
| endpoint | Action context |
| method | Read vs write behavior |
| object_id | Object-level authorization analysis |
| decision | Allowed or denied |
| denial_reason | Detection and debugging |
| source_ip | Source context |
| user_agent | Client context |

## Do Not Log

- Passwords
- Full tokens
- Secrets
- Payment data
- Sensitive payloads unless explicitly approved
- Full personal data when an identifier is enough

## Detection Use Cases

| Use case | Required fields |
|---|---|
| Cross-tenant access attempts | actor_id, tenant_id, object_id, denial_reason |
| Sensitive export spike | actor_id, endpoint, record_count, bytes |
| Admin action anomaly | actor_id, endpoint, method, decision |
| Token abuse | client_id, actor_id, token audience, result |

## Example Event

```json
{
  "timestamp": "2026-06-19T10:00:00Z",
  "request_id": "req-001",
  "actor_id": "user-123",
  "tenant_id": "tenant-a",
  "endpoint": "/api/v1/projects/project-999/invoices",
  "method": "GET",
  "decision": "deny",
  "denial_reason": "cross_tenant_access_attempt"
}
```

## Engineering Requirement

Every sensitive endpoint should have a logging test that verifies denial events
include enough context for detection and investigation.
