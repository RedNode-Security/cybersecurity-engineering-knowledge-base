---
title: Diagram — Detection Engineering Lifecycle
domain: architecture
category: diagram
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [architecture, mermaid, diagram]
difficulty: intermediate
safe_publication: true
---


# Diagram — Detection Engineering Lifecycle

## Diagram

```mermaid
flowchart LR
  B[Behavior] --> H[Hypothesis]
  H --> T[Telemetry]
  T --> L[Logic]
  L --> Test[Test Data]
  Test --> Deploy[Deploy]
  Deploy --> M[Measure]
  M --> Tune[Tune]
  Tune --> H
```

## Notes

Detection engineering is a lifecycle, not a one-time query.
