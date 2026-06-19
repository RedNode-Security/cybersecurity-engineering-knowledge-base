# 00 — Fundamentals

## Purpose

The fundamentals section builds the mental models needed for every other part of
security engineering. A strong defender should understand not only definitions,
but also how systems fail, how attackers chain weak points, what evidence proves
a control is working, and what can be automated safely.

## Operating Model

```text
Asset → Trust Boundary → Control → Telemetry → Detection → Response → Improvement
```

## Core Learning Objectives

By the end of this section you should be able to:

- Draw a system boundary and identify assets, identities, and privileged actions.
- Explain why least privilege and secure defaults reduce blast radius.
- Identify useful logs for authentication, authorization, network, and endpoint events.
- Convert a security principle into an implementation checklist.
- Write a detection hypothesis for a realistic misuse scenario.
- Propose safe automation for validation, enrichment, or reporting.

## Detailed Pages

- [Security Engineering Principles](security-engineering-principles.md)
- [Network Security Foundations](Network-Security/network-security-foundations.md)
- [Windows Event Logging](Windows-Security/windows-event-logging.md)
- [Linux Hardening and Logging](Linux-Security/linux-hardening-and-logging.md)

## Example Learning Workflow

Scenario: you are reviewing a small internal web application.

1. Identify assets: user accounts, database, API, admin console, logs.
2. Identify identities: users, admins, service accounts, CI/CD pipeline.
3. Identify privileged actions: create admin, export data, change configuration.
4. Identify controls: authentication, authorization, network restrictions, audit logs.
5. Identify evidence: login logs, admin action logs, database access logs, deployment logs.
6. Write one detection: admin role assigned outside normal change window.
7. Write one automation: daily report of new privileged users and stale service accounts.

## Practical Output

Every fundamentals note should help produce at least one artifact:

- A diagram
- A checklist
- A detection hypothesis
- A log-source map
- A hardening baseline
- A risk decision record
