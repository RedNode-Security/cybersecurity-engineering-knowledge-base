---
title: Detection Engineering
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [detection, siem, threat-hunting]
difficulty: intermediate
safe_publication: true
---


# Detection Engineering

## Overview

Detection engineering converts threat knowledge into repeatable security
analytics. A detection should be treated like an engineering artifact: documented,
reviewed, tested, tuned, owned, and retired when stale.

## Detection Lifecycle

```text
Behavior → Hypothesis → Telemetry → Logic → Test Data → Tuning → Triage → Metrics → Review
```

## Local Pages

- [Detection Engineering Methodology](detection-engineering-methodology.md)
- [Detection-as-Code Lifecycle](detection-as-code-lifecycle.md)
- [Detection Rule Examples](detection-rule-examples.md)
- [Windows Authentication Detection](windows-authentication-detection.md)
- [Sample Detection Hypothesis](sample-detection-hypothesis.md)

## Detection Artifact Standard

| Section | Required content |
|---|---|
| Hypothesis | What behavior is expected? |
| Telemetry | Which logs and fields are required? |
| Logic | Query, pseudocode, or rule behavior |
| False positives | Known benign patterns |
| Triage | What analyst should do next |
| Response | Containment or escalation options |
| Testing | Safe validation method |
| Ownership | Owner and review date |

## Example Detection Review Questions

- Does the logic actually match the hypothesis?
- Can the required logs be joined reliably?
- What legitimate business processes will trigger it?
- Does the alert include enough context for triage?
- What response action is appropriate?
- How will we know if this detection becomes stale?

## Maturity Path

1. Document detection hypotheses.
2. Build queries manually.
3. Add sample events.
4. Add peer review.
5. Add detection-as-code metadata.
6. Add automated validation.
7. Add metrics and lifecycle review.
