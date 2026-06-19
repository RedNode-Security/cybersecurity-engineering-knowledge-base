---
title: IOC Lifecycle and Scoring
domain: threat-intelligence
category: ioc-management
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [ioc, threat-intelligence, enrichment]
difficulty: beginner
safe_publication: true
---


# IOC Lifecycle and Scoring

## Overview

IOC lifecycle management prevents stale, noisy, or low-confidence indicators from
hurting operations. Every IOC should move from collection to expiration.

## Lifecycle

```text
Collect → Sanitize → Enrich → Score → Approve Use → Deploy → Monitor → Expire
```

## Confidence Factors

| Factor | Questions |
|---|---|
| Source reliability | Is the source trusted? |
| Context | Is there campaign, malware, or case context? |
| Recency | Was it observed recently? |
| Corroboration | Do multiple sources agree? |
| Indicator stability | Is it likely to remain useful? |
| False-positive risk | Could it match legitimate services? |

## Example Scoring

```text
Indicator: login-update.example.invalid
Source: internal phishing simulation
Context: credential harvesting simulation
Recency: observed today
Corroboration: internal email report and proxy log
False-positive risk: low in lab environment
Confidence: medium
Handling: alert in test environment; do not block globally
```

## Expiration Guidance

| Type | Review window |
|---|---|
| IP address | 7 to 30 days |
| Domain | 30 to 90 days |
| URL | 30 to 90 days |
| File hash | Review for relevance quarterly |
| Email sender | Short-lived unless tied to infrastructure |

## Automation Ideas

- Validate IOC JSON schema.
- Flag missing source or confidence.
- Flag expired indicators.
- Generate SIEM watchlists from approved IOCs.
- Track false positive feedback.
