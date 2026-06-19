---
title: API Security
domain: application-security
category: api-security
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [api-security, appsec]
difficulty: intermediate
safe_publication: true
---


# API Security

## Overview

API security protects application interfaces from unauthorized access, data
exposure, business logic abuse, and insecure integrations.

## Local Pages

- [API Security Checklist](api-security-checklist.md)
- [API Threat Model Example](api-threat-model-example.md)

## API Security Model

```text
Client → Authentication → Authorization → Business Logic → Data Access → Audit Logging
```

## Key Risks

| Risk | Example |
|---|---|
| Broken object authorization | User accesses another tenant's object |
| Broken function authorization | Normal user performs admin action |
| Excessive data exposure | API returns sensitive fields not required by UI |
| Token validation failure | API accepts wrong audience or unsigned token |
| Abuse and automation | High-volume scraping or brute force |

## Defensive Questions

- Who is the caller?
- What object is being accessed?
- Who owns the object?
- What action is being performed?
- Is this action logged?
- Can abuse be detected?
