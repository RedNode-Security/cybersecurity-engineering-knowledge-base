---
title: IR Playbook — Phishing Triage
domain: blue-team
category: incident-response
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [incident-response, playbook]
difficulty: advanced
safe_publication: true
---


# IR Playbook — Phishing Triage

## Objective

Provide a repeatable defensive workflow for triage, evidence collection,
containment, recovery, and lessons learned.

## Trigger Conditions

- User reports suspicious email
- Email gateway alert
- URL click alert

## Evidence to Collect

- Message headers
- URL and attachment metadata
- Recipient list
- Click logs

## Triage Steps

1. Confirm alert source and detection logic.
2. Identify affected users, assets, applications, and time range.
3. Build a timeline of related events.
4. Check business context and approved changes.
5. Determine scope and severity.
6. Decide containment with the incident lead.

## Containment Options

- Quarantine message
- Block URL if high confidence
- Reset credentials if submitted

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
