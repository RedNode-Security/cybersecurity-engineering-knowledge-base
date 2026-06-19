---
title: SOC Alert Triage Workflow
domain: blue-team
category: soc-operations
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [soc, triage, alerting]
difficulty: beginner
safe_publication: true
---


# SOC Alert Triage Workflow

## Overview

Alert triage determines whether an alert is benign, suspicious, duplicate, or a
confirmed incident. Good triage is evidence-driven and repeatable.

## Workflow

1. Read alert hypothesis and logic.
2. Identify affected user, asset, application, and data source.
3. Build a timeline before and after the alert.
4. Enrich with asset criticality and user role.
5. Check related alerts and threat intelligence.
6. Compare against known false positives.
7. Classify and route.
8. Document evidence and decision.

## Classification

| Classification | Meaning | Example action |
|---|---|---|
| False positive | Rule matched incorrectly | Tune rule |
| Benign true positive | Expected activity matched rule | Close with reason |
| Suspicious | Needs investigation | Escalate to Tier 2 |
| Confirmed incident | Malicious or policy violation | Start playbook |
| Duplicate | Already handled | Link to parent case |

## Example Triage Note

```text
Alert: Privileged group membership change
Actor: EXAMPLE\helpdesk01
Target: EXAMPLE\temp.admin
Group: Domain Admins
Finding: No change ticket found. Actor does not normally modify Domain Admins.
Decision: Suspicious. Escalated to incident response.
```

## Escalation Criteria

Escalate if:

- Privileged identity is involved.
- Sensitive asset is involved.
- Activity is unexplained.
- Multiple related alerts exist.
- Possible data access or malware execution occurred.

## Automation Ideas

- Auto-populate case template.
- Enrich user and asset context.
- Pull recent sign-ins and recent alerts.
- Link related cases.
- Suggest playbook based on alert type.
