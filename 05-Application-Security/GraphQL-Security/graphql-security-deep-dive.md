---
title: GraphQL Security Deep Dive
domain: application-security
category: graphql-security
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [graphql, api-security, appsec]
difficulty: advanced
safe_publication: true
---


# GraphQL Security Deep Dive

## Scope

This page covers GraphQL security concerns from a defensive engineering point of
view: authorization, query complexity, introspection, batching, and logging.

## Key Risks

| Risk | Defensive concern |
|---|---|
| Field-level authorization | User can request fields UI does not show |
| Object-level authorization | Resolver returns object from another tenant |
| Query complexity | Expensive nested queries affect availability |
| Batching abuse | Many operations in one request |
| Introspection exposure | Schema reveals sensitive operations |
| Logging gaps | Operation name without resolver/object context is insufficient |

## Authorization Rule

Every resolver that returns sensitive data must enforce authorization for the
specific object and field, not only the top-level query.

## Detection Ideas

- High query depth.
- High resolver count.
- Repeated authorization failures.
- Sensitive fields requested by unusual clients.
- Batch request volume anomalies.

## Logging Fields

- Request ID
- Actor ID
- Operation name
- Resolver names or categories
- Object IDs where safe
- Decision and denial reason
- Query depth and complexity score

## Safe Testing

- Test cross-tenant object access.
- Test unauthorized sensitive fields.
- Test query depth limits.
- Test batching limits.
- Verify denial logging.
