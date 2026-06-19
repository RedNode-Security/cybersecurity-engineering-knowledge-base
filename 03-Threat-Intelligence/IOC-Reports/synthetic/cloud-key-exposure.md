---
title: IOC Report — Synthetic Cloud Key Exposure
domain: threat-intelligence
category: ioc-report
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [ioc, synthetic, training]
difficulty: beginner
safe_publication: true
---


# IOC Report — Synthetic Cloud Key Exposure

## Summary

Demonstrates cloud-focused indicator context.

This is a synthetic TLP:CLEAR training report. Values are documentation-safe and
must not be treated as real malicious infrastructure.

## Handling

| Field | Value |
|---|---|
| TLP | TLP:CLEAR |
| Source | synthetic training data |
| Confidence | low |
| Recommended use | enrichment, parser testing, and training only |
| Expiration | 2026-09-19 |

## Indicators

| Type | Value | Confidence | Context |
|---|---|---|---|
| domain | `training-cloud-key-exposure.example.invalid` | low | Synthetic domain |
| ip | `198.51.100.10` | low | Documentation IP range |
| sha256 | `0000000000000000000000000000000000000000000000000000000000000000` | low | Placeholder hash |

## Defensive Use

- Validate IOC parsing.
- Test enrichment workflows.
- Train analysts on confidence and expiration.
- Do not block production traffic based on these values.
