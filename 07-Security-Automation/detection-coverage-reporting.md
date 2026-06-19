---
title: Detection Coverage Reporting
domain: security-automation
category: coverage-reporting
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, coverage, automation]
difficulty: advanced
safe_publication: true
---


# Detection Coverage Reporting

## Scope

Detection coverage reporting shows which behaviors, assets, and data sources are
covered by detection content. It should not claim that a covered behavior is
impossible to miss.

## Coverage Dimensions

| Dimension | Example |
|---|---|
| Data source | identity_signin_logs, aws_cloudtrail |
| Entity | user, host, cloud account, application |
| Behavior | password spray, key creation, privilege change |
| Severity | low, medium, high, critical |
| Status | experimental, production, deprecated |
| Owner | detection-engineering |

## Useful Questions

- Which critical data sources have no detections?
- Which detections lack test data?
- Which behaviors have only low-confidence coverage?
- Which detections are past review date?
- Which domains rely on one fragile data source?

## Automation

Use `scripts/generate_detection_coverage.py` to summarize detection metadata.
