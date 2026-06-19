---
title: Diagram — RAG Trust Boundary
domain: architecture
category: diagram
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [architecture, mermaid, diagram]
difficulty: intermediate
safe_publication: true
---


# Diagram — RAG Trust Boundary

## Diagram

```mermaid
flowchart LR
  U[User Query] --> R[Retriever]
  R --> ACL[Authorization Filter]
  ACL --> C[Context Builder]
  C --> LLM[LLM]
  LLM --> O[Output Filter]
  O --> User[User]
  C --> Audit[Audit Log]
```

## Notes

Retrieved content is data, not instruction. Authorization must happen before retrieval output is used.
