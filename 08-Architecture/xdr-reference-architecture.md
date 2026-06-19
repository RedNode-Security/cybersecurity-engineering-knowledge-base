---
title: XDR Reference Architecture
domain: architecture
category: xdr-architecture
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [xdr, architecture, correlation]
difficulty: advanced
safe_publication: true
---


# XDR Reference Architecture

## Overview

Extended Detection and Response, or XDR, correlates signals across endpoint,
identity, network, cloud, email, and application telemetry. The value is not the
label; the value is cross-domain context that improves detection and response.

## XDR Data Domains

| Domain | Example signals |
|---|---|
| Identity | sign-ins, MFA, role changes |
| Endpoint | process, file, registry, network |
| Network | DNS, proxy, firewall, flow logs |
| Cloud | CloudTrail, Azure activity, Kubernetes audit |
| Email | delivery, URL clicks, attachments |
| Application | sensitive actions, authz failures, data access |

## Correlation Example

```text
Phishing email delivered → user clicks URL → risky sign-in → endpoint script execution → cloud access key created
```

A single domain may look weak. The sequence is high confidence.

## Architecture Requirements

- Common entity model for users, devices, IPs, and resources.
- Time synchronization.
- Stable asset and identity inventory.
- Data quality monitoring.
- Correlation rules with explainable evidence.
- Case management integration.

## Entity Model

| Entity | Required context |
|---|---|
| User | department, role, privilege, MFA status |
| Device | owner, management status, criticality |
| IP | internal/external, VPN/proxy, reputation |
| Cloud resource | account, region, owner, environment |
| Application | owner, data sensitivity, business criticality |

## Anti-Patterns

- Buying XDR without data quality.
- Correlating everything with no hypothesis.
- Missing identity normalization.
- Ignoring application logs.
- No analyst explanation for correlation chains.
