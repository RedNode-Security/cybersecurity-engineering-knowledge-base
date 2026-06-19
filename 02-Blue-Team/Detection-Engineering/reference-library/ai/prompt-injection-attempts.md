---
title: Prompt Injection Attempt Pattern
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, ai, reference]
difficulty: advanced
safe_publication: true
---


# Prompt Injection Attempt Pattern

## Detection ID

```text
DET-AI-PROMPT_INJECTION_ATTEMPTS
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Repeated prompt injection attempts may indicate abuse or testing.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `llm_audit_logs`

Required fields:

- `timestamp`
- `user`
- `prompt_category`
- `policy_result`

## Normalized Logic

```text
instruction_override attempts exceed threshold
```

## Positive Sample Event

```json
{
  "event_id": "evt-ai-004",
  "user": "user@example.com",
  "prompt_category": "instruction_override",
  "count_1h": 12
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-ai-benign-004",
  "user": "security-tester@example.com",
  "prompt_category": "instruction_override",
  "approved_test": true
}
```

## Expected False Positives

- approved AI red-team test

## Triage Workflow

1. Confirm affected entity and timestamp
2. Review surrounding events for 24 hours
3. Check approved change or expected business activity
4. Escalate if behavior remains unexplained

## Response Guidance

- Preserve relevant logs
- Open an incident case if suspicious
- Contain affected identity, host, or resource if compromise is confirmed

## Analyst Note

Do not store raw prompts unnecessarily. Store categories and safe excerpts.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-AI-PROMPT_INJECTION_ATTEMPTS
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
