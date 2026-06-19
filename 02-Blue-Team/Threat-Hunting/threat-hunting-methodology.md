---
title: Threat Hunting Methodology
domain: blue-team
category: threat-hunting
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [threat-hunting, hypothesis, detection]
difficulty: intermediate
safe_publication: true
---


# Threat Hunting Methodology

## Overview

Threat hunting is proactive investigation based on a hypothesis. It searches for
weak signals that may not yet be covered by high-confidence detections.

## Hunting Loop

```text
Question → Hypothesis → Data → Query → Pivot → Validate → Document → Improve
```

## Hunt Plan Template

| Field | Example |
|---|---|
| Hypothesis | Compromised users may access rare systems after unusual sign-in |
| Scope | Privileged users, last 14 days |
| Data sources | IdP logs, Windows logs, asset inventory |
| Query approach | Rare source and rare destination joins |
| Expected benign | Admin maintenance and travel |
| Escalation criteria | Sensitive asset access without explanation |
| Output | Detection or case |

## Example Hunt

Hypothesis:

```text
A compromised cloud identity may create access keys and enumerate storage shortly after sign-in.
```

Query approach:

1. Find `CreateAccessKey` events.
2. Join to recent sign-ins by actor.
3. Identify actors with no key creation in previous 90 days.
4. Review follow-on API calls.
5. Escalate if storage or IAM enumeration follows.

## Hunt Outcomes

- Confirmed incident
- New detection
- Detection tuning
- Logging gap
- Control improvement
- Negative finding with documented coverage

## Automation Ideas

- Store hunt hypotheses.
- Track query results and outcomes.
- Convert recurring hunts into detections.
- Generate coverage maps by data source.
