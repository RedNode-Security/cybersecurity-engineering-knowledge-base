---
title: IOC Management
domain: threat-intelligence
category: ioc-management
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [ioc, threat-intelligence]
difficulty: beginner
safe_publication: true
---


# IOC Management

## Overview

Indicators of compromise are observable values associated with suspicious or
malicious activity. They are useful only when they include source, context,
confidence, handling guidance, and expiration.

## Local Pages

- [IOC Lifecycle and Scoring](ioc-lifecycle-and-scoring.md)
- [IOC Examples](ioc-examples.md)
- [Sample IOC JSON](../samples/ioc-sample.json)

## IOC Fields

| Field | Purpose |
|---|---|
| Type | IP, domain, URL, hash, email, user agent, etc. |
| Value | Observable value |
| Source | Where it came from |
| Confidence | Low, medium, or high |
| Context | Why it matters |
| First seen | Initial observation |
| Last seen | Most recent observation |
| Expiration | Review or removal date |
| Handling | Enrich, hunt, alert, block, or correlate |

## Handling Decision

| Confidence | Suggested use |
|---|---|
| Low | Enrichment or hunting only |
| Medium | Alerting after false-positive review |
| High | Alerting or blocking after business impact review |

## Example Decision

```text
A domain from a trusted phishing report with recent sightings and low false-positive risk can be used for alerting. A shared hosting IP with unclear context should be enrichment-only.
```
