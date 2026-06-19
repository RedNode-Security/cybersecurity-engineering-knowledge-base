---
title: Diagram — SOAR Human Approval Workflow
domain: architecture
category: diagram
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [architecture, mermaid, diagram]
difficulty: intermediate
safe_publication: true
---


# Diagram — SOAR Human Approval Workflow

## Diagram

```mermaid
flowchart LR
  A[Alert] --> E[Enrichment]
  E --> Rec[Recommendation]
  Rec --> P[Approval Gate]
  P -->|Approved| X[Execute Action]
  P -->|Denied| C[Continue Investigation]
  X --> Audit[Audit Log]
```

## Notes

High-risk containment should require approval and audit evidence.
