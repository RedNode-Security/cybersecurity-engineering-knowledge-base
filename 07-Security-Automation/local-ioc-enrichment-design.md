---
title: Local IOC Enrichment Design
domain: security-automation
category: threat-intel-automation
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [ioc, automation, enrichment]
difficulty: advanced
safe_publication: true
---


# Local IOC Enrichment Design

## Overview

A local IOC enrichment workflow validates and summarizes indicators without
requiring external APIs or secrets. It is safe for public examples and useful for
building confidence before integrating commercial feeds.

## Workflow

```text
IOC JSON → Schema Validation → Age Check → Confidence Check → Handling Decision → Markdown Report
```

## Input Requirements

- report_id
- source
- TLP
- confidence
- created date
- indicators with type, value, confidence, context, expiration

## Handling Logic

| Condition | Suggested handling |
|---|---|
| Missing context | Reject or mark incomplete |
| Low confidence | Enrichment only |
| Expired | Review or remove |
| Medium confidence | Hunt or alert after review |
| High confidence | Alert or block after impact review |

## Example Output

```text
Report: ioc-sample-001
Indicators: 2
Expired: 0
High confidence: 0
Recommended action: use for training and enrichment only
```

## Safety Requirements

- No API keys required by default.
- No external lookups unless explicitly enabled.
- No secrets written to logs.
- Synthetic values clearly labeled.
- Blocking lists require manual approval.

## Future Enhancements

- JSON schema validation in CI.
- Markdown report generation.
- Expiration warnings.
- SIEM watchlist export.
- Analyst feedback tracking.
