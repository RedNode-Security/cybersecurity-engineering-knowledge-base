---
title: Practical Lab Roadmap
domain: resources
category: labs
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [learning, labs, practice]
difficulty: beginner
safe_publication: true
---


# Practical Lab Roadmap

## Overview

This roadmap turns repository topics into safe, hands-on practice. Labs should be
run only in owned, isolated, or explicitly authorized environments.

## Lab Safety Rules

- Use local VMs, private cloud sandboxes, or intentionally designed lab systems.
- Do not connect vulnerable lab systems directly to the public internet.
- Do not use real customer data.
- Tear down cloud resources after completion.
- Record expected evidence and cleanup steps.

## Lab 1 — Windows Authentication Logs

Goal:

```text
Understand Windows authentication event IDs and triage questions.
```

Tasks:

1. Review sample Windows authentication events.
2. Identify successful and failed logons.
3. Identify a privileged group change.
4. Write a detection hypothesis.
5. Document false positives.

Output:

- Event ID notes
- Detection hypothesis
- Triage checklist

## Lab 2 — IOC Lifecycle

Goal:

```text
Practice structured IOC documentation and expiration.
```

Tasks:

1. Review sample IOC JSON.
2. Add confidence and context.
3. Decide handling: enrich, hunt, alert, or block.
4. Set expiration date.
5. Write a short IOC report.

Output:

- IOC report
- Handling decision
- Expiration plan

## Lab 3 — CloudTrail Detection

Goal:

```text
Practice cloud control-plane detection with synthetic events.
```

Tasks:

1. Review `CreateAccessKey` and `AttachUserPolicy` examples.
2. Write pseudocode detection.
3. Define false positives.
4. Write response actions.

Output:

- Detection logic
- Triage workflow
- Response checklist

## Lab 4 — API Authorization Threat Model

Goal:

```text
Threat-model object-level authorization.
```

Tasks:

1. Pick a sample endpoint.
2. Identify assets and trust boundaries.
3. Write an abuse case.
4. Define secure authorization checks.
5. Define logging and detection.

Output:

- Threat model table
- Authorization checklist
- Detection idea

## Lab 5 — Prompt Injection Evaluation

Goal:

```text
Design safe tests for LLM trust boundaries.
```

Tasks:

1. Define system instructions and untrusted content.
2. Create direct and indirect injection test cases.
3. Define expected safe behavior.
4. Track pass/fail results.

Output:

- Evaluation table
- Control gaps
- Monitoring ideas
