---
title: Serious Detection Library Status
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, coverage, status]
difficulty: advanced
safe_publication: true
---


# Serious Detection Library Status

## Current State

The repository now contains a serious detection reference library with **66**
platform-neutral detections. Each reference detection has metadata, sample data,
logic, triage, response guidance, and test case mapping.

## Coverage

| Domain | Count |
|---|---|
| ai | 6 |
| application | 6 |
| cloud | 12 |
| identity | 12 |
| kubernetes | 6 |
| linux | 6 |
| network | 6 |
| windows | 12 |

## What Makes It Serious

- Every major telemetry domain has coverage.
- Each detection has positive and benign sample data.
- Each detection has a test case ID.
- Metadata and reference pages are linked.
- Validation checks confirm metadata and reference pages exist.
- Coverage reports summarize domains, severities, and data sources.

## Remaining Work

- Convert selected detections into SIEM-specific implementations.
- Add real environment-specific tuning notes after deployment.
- Promote detections in small reviewed batches.
- Add more sample events as new false positives are discovered.
