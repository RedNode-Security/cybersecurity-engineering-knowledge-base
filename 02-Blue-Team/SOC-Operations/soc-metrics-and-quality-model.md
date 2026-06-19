---
title: SOC Metrics and Quality Model
domain: blue-team
category: soc-operations
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [soc, metrics, quality]
difficulty: advanced
safe_publication: true
---


# SOC Metrics and Quality Model

## Overview

SOC metrics should measure decision quality, response speed, coverage, and
learning. Counting alerts alone is not enough. Elite SOCs measure whether alerts
lead to correct decisions and improved controls.

## Metric Categories

| Category | Example metrics |
|---|---|
| Speed | MTTD, MTTT, MTTC, MTTR |
| Quality | True positive rate, false positive rate, escalation accuracy |
| Coverage | Detection coverage by tactic, asset, data source |
| Reliability | Log source uptime, parser failure count, enrichment success rate |
| Learning | Post-incident action closure, detections improved from incidents |
| Workload | Case backlog, alert volume, analyst load |

## Definitions

| Metric | Meaning |
|---|---|
| MTTD | Mean time to detect |
| MTTT | Mean time to triage |
| MTTC | Mean time to contain |
| MTTR | Mean time to recover |

## Example Monthly SOC Report

```text
Total alerts: 1,240
Cases opened: 88
Confirmed incidents: 6
Top noisy detection: impossible travel from VPN egress
Critical log source uptime: 99.4 percent
Mean time to triage high alerts: 18 minutes
Post-incident actions closed: 7 of 10
Top improvement: identity enrichment reduced false positives by 22 percent
```

## Quality Questions

- Which detections create the most analyst waste?
- Which incidents were detected late?
- Which critical assets lack telemetry?
- Which playbooks are missing or outdated?
- Which automated enrichments fail most often?
- Which post-incident actions are overdue?

## Executive Dashboard Sections

- Top risks
- Incident summary
- Detection coverage
- Log source health
- Vulnerability exposure
- Identity risk
- Cloud posture
- Open exceptions
- Roadmap blockers

## Anti-Patterns

- Reporting only alert volume.
- Treating every closed case as equal.
- Ignoring false positive categories.
- Tracking MTTD without timestamp quality.
- Measuring automation count instead of automation value.
