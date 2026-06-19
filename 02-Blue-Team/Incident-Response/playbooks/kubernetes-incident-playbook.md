---
title: IR Playbook — Kubernetes Incident
domain: blue-team
category: incident-response
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [incident-response, playbook]
difficulty: advanced
safe_publication: true
---


# IR Playbook — Kubernetes Incident

## Objective

Provide a repeatable defensive workflow for triage, evidence collection,
containment, recovery, and lessons learned.

## Trigger Conditions

- Cluster-admin binding
- Secret read anomaly
- Privileged pod creation

## Evidence to Collect

- Kubernetes audit logs
- Pod specs
- RBAC changes
- Node telemetry

## Triage Steps

1. Confirm alert source and detection logic.
2. Identify affected users, assets, applications, and time range.
3. Build a timeline of related events.
4. Check business context and approved changes.
5. Determine scope and severity.
6. Decide containment with the incident lead.

## Containment Options

- Revoke service account token
- Remove role binding
- Quarantine workload

## Recovery

- Restore trusted state.
- Verify access and monitoring.
- Confirm no recurrence.
- Communicate closure to stakeholders.

## Lessons Learned

- What detected the incident?
- What was missing?
- Which control failed or was absent?
- Which detection, playbook, or architecture page should change?
