---
title: Secure SDLC Operating Model
domain: application-security
category: secure-sdlc
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [sdlc, appsec, secure-design]
difficulty: advanced
safe_publication: true
---


# Secure SDLC Operating Model

## Overview

A secure SDLC embeds security into engineering flow instead of relying only on
late-stage testing. The goal is to reduce defects before deployment and improve
runtime detection after deployment.

## Lifecycle

```text
Requirements → Threat Model → Design Review → Secure Coding → Testing → Deployment → Monitoring → Feedback
```

## Security Gates

| Stage | Security activity | Evidence |
|---|---|---|
| Requirements | Abuse cases and security requirements | User stories and acceptance criteria |
| Design | Threat model | Diagram and risk decisions |
| Build | Secure coding and dependency checks | PR checks and scan results |
| Test | Security test cases | Test results |
| Deploy | IaC and config review | Pipeline evidence |
| Operate | Logging and monitoring | Alerts and dashboards |

## Example Security Requirement

```text
The API must enforce object-level authorization for all project resources and log denied cross-tenant access attempts with request ID, actor ID, tenant ID, and object ID.
```

## Pull Request Checklist

- [ ] Does this change affect authentication or authorization?
- [ ] Does it expose sensitive data?
- [ ] Are new endpoints logged?
- [ ] Are error messages safe?
- [ ] Are dependencies updated safely?
- [ ] Are secrets excluded from code and logs?
- [ ] Are abuse cases tested?

## Metrics

- Security defects found before production
- Critical dependency remediation time
- Secret scan findings
- Threat models completed for high-risk changes
- Authorization test coverage
- Runtime security alerts from applications
