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

Detection engineering is the structured process of turning threat knowledge into reliable, testable, and maintainable detections.

## Detection Lifecycle

1. Identify threat behavior
2. Define detection hypothesis
3. Map required telemetry
4. Build query or rule
5. Validate with safe test data
6. Tune false positives
7. Document triage and response
8. Monitor performance
9. Retire or update when obsolete

## Detection Quality Checklist

- [ ] Clear detection hypothesis
- [ ] Mapped to ATT&CK or internal behavior taxonomy
- [ ] Required log sources documented
- [ ] False positives listed
- [ ] Triage steps included
- [ ] Severity and confidence defined
- [ ] Test method documented
- [ ] Owner and review date assigned

## Starter Artifacts

- Use [`../../99-Templates/detection-rule-template.md`](../../99-Templates/detection-rule-template.md)
- Add detection notes under this directory
- Link related incident response playbooks
