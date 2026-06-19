---
title: SOC Reference Architecture
domain: architecture
category: soc-architecture
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [soc, architecture, detection, incident-response]
difficulty: intermediate
safe_publication: true
---


# SOC Reference Architecture

## Overview

A Security Operations Center combines telemetry, detection, enrichment, triage,
response, threat intelligence, automation, and metrics.

## Reference Flow

```text
Telemetry → Collection → Normalization → Detection → Enrichment → Triage → Response → Lessons Learned
```

## Components

| Component | Purpose |
|---|---|
| Telemetry sources | Identity, endpoint, network, cloud, app, email |
| SIEM/data lake | Search, correlation, retention |
| Detection content | Alerts, hunts, analytics |
| Case management | Evidence and decisions |
| Automation | Enrichment and workflow orchestration |
| Threat intelligence | IOC, CVE, and actor context |
| Metrics | Quality and improvement tracking |

## Failure Modes

- Missing logs
- Noisy detections
- No asset context
- No response owner
- Manual bottlenecks
- Lessons learned not implemented

## Metrics

- Mean time to detect
- Mean time to triage
- Mean time to contain
- False positive rate
- Log source health
- Case backlog
