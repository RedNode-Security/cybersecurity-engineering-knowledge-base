---
title: Detection Engineering Operating Model
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [detection, operating-model, metrics, quality]
difficulty: advanced
safe_publication: true
---


# Detection Engineering Operating Model

## Overview

A detection engineering operating model defines how detection ideas become
production analytics and how those analytics remain reliable. Elite teams manage
detections as a product portfolio, not as random queries.

## Operating Flow

```text
Threat Requirement → Detection Hypothesis → Data Contract → Rule → Test → Deploy → Measure → Improve
```

## Roles

| Role | Responsibility |
|---|---|
| Detection owner | Maintains the detection and reviews performance |
| Data owner | Ensures telemetry exists and fields are reliable |
| SOC analyst | Provides triage feedback and false-positive notes |
| Incident responder | Defines escalation and containment needs |
| Threat intel analyst | Supplies actor, CVE, and IOC context |
| Platform engineer | Supports SIEM, data lake, and deployment automation |

## Detection Portfolio Tiers

| Tier | Description | Review cadence |
|---|---|---|
| Tier 0 | Critical detections for identity, logging tampering, malware, cloud compromise | Monthly |
| Tier 1 | High-value behavior detections mapped to priority threats | Quarterly |
| Tier 2 | Useful coverage with manageable noise | Semiannual |
| Tier 3 | Experimental, hunt-derived, or low-confidence detections | As needed |

## Data Contracts

A detection should have a data contract:

```yaml
data_source: identity_signin_logs
required_fields:
  - timestamp
  - user_id
  - source_ip
  - device_id
  - result
  - mfa_result
freshness_sla: 15 minutes
retention: 90 days
owner: identity-platform-team
known_blind_spots:
  - shared VPN egress
  - unmanaged contractor devices
```

## Detection Definition of Done

- [ ] Hypothesis is behavior-based.
- [ ] Required telemetry is documented.
- [ ] Data owner is known.
- [ ] Test data exists.
- [ ] False positives are documented.
- [ ] Triage steps are included.
- [ ] Severity and confidence are justified.
- [ ] Owner and review date are assigned.
- [ ] Alert has enrichment requirements.
- [ ] Metrics are tracked after deployment.

## Quality Metrics

| Metric | Target behavior |
|---|---|
| Alert precision | Improve by tuning and enrichment |
| Mean time to triage | Reduce through context and playbooks |
| Detection coverage | Increase against priority behaviors |
| Stale detection count | Reduce through lifecycle review |
| Test coverage | Increase for critical detections |
| Data freshness | Maintain within SLA |

## Example Quarterly Review

```text
Detection: Password spray followed by success
Alert volume: 34 per month
True positives: 3
Benign true positives: 24
False positives: 7
Primary noise source: vulnerability scanner using domain credentials
Action: add scanner identity enrichment and suppress known maintenance window
Owner: detection-engineering
Next review: 2026-09-18
```
