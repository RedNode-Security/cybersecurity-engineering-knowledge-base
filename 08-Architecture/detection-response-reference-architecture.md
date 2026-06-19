---
title: Detection and Response Reference Architecture
domain: architecture
category: detection-response
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [architecture, detection, incident-response]
difficulty: advanced
safe_publication: true
---


# Detection and Response Reference Architecture

## Overview

Detection and response architecture connects telemetry, analytics, enrichment,
case management, response actions, evidence, and lessons learned.

## Architecture

```text
Data Sources → Collection → Normalization → Analytics → Enrichment → Case → Response → Evidence → Improvement
```

## Components

| Component | Responsibility |
|---|---|
| Data sources | Identity, endpoint, network, cloud, application logs |
| Collector | Reliable ingestion and buffering |
| Normalization | Common field names and event categories |
| Analytics | Detections, correlations, baselines |
| Enrichment | Asset, identity, threat, vulnerability context |
| Case management | Evidence, decisions, ownership |
| Response executor | Approved containment and recovery actions |
| Metrics | Quality and improvement measurement |

## Design Requirements

- Critical logs have health monitoring.
- Detections map to playbooks.
- Alerts include context needed for triage.
- High-risk response actions require approval.
- Evidence is preserved with retention and access controls.
- Lessons learned create backlog items.

## Example Data Flow

```text
Risky sign-in event enters SIEM.
Detection correlates sign-in with privileged group change.
Enrichment adds user role and asset criticality.
Case is created with account compromise playbook.
Analyst approves session revocation.
SOAR executes action and records audit evidence.
Post-incident review creates MFA hardening task.
```

## Failure Modes

- Detection fires but no playbook exists.
- Enrichment fails silently.
- Response action lacks approval record.
- Logs expire before investigation.
- Metrics do not show false positive burden.
