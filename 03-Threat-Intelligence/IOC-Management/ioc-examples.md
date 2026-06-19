---
title: IOC Examples
domain: threat-intelligence
category: ioc-management
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [ioc, examples, threat-intelligence]
difficulty: beginner
safe_publication: true
---


# IOC Examples

## Overview

This page shows how to document indicators with context, confidence, and handling
guidance. Examples use synthetic values.

## Example IOC Table

| Type | Value | Confidence | Context | Expiration | Handling |
|---|---|---|---|---|---|
| domain | `login-update.example.invalid` | medium | Synthetic phishing domain example | 2026-09-18 | Hunt and alert |
| ip | `198.51.100.25` | low | Documentation IP, not real malicious infrastructure | 2026-07-18 | Enrichment only |
| sha256 | `0000000000000000000000000000000000000000000000000000000000000000` | low | Placeholder hash | 2026-09-18 | Do not block |

## Example IOC Report Summary

```text
Report ID: ioc-training-001
TLP: TLP:CLEAR
Source: synthetic training example
Confidence: medium
Summary: Demonstrates IOC documentation fields and handling guidance.
Recommended use: hunting and enrichment only.
```

## Handling Guidance

- Low confidence: enrichment or hunt only.
- Medium confidence: scoped alerting after false-positive review.
- High confidence: alerting or blocking after business impact review.

## Bad IOC Example

```text
bad-domain.com
```

Problems:

- No source
- No confidence
- No first-seen or last-seen
- No context
- No expiration
- No handling recommendation

## Better IOC Example

```text
Type: domain
Value: login-update.example.invalid
Source: internal phishing simulation
Confidence: medium
First seen: 2026-06-18
Last seen: 2026-06-18
Expiration: 2026-09-18
Context: synthetic phishing domain used for training
Handling: alert in test environment only
```
