---
title: Diagram — XDR Correlation Chain
domain: architecture
category: diagram
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [architecture, mermaid, diagram]
difficulty: intermediate
safe_publication: true
---


# Diagram — XDR Correlation Chain

## Diagram

```mermaid
flowchart LR
  Email[Phishing Email] --> Click[URL Click]
  Click --> Login[Risky Sign-in]
  Login --> Endpoint[Endpoint Script]
  Endpoint --> Cloud[Cloud Key Created]
  Cloud --> Case[High-Confidence Case]
```

## Notes

XDR value comes from correlating weak signals into an explainable sequence.
