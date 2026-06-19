---
title: AI Agent Repeated Tool Failure
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, ai, reference]
difficulty: advanced
safe_publication: true
---


# AI Agent Repeated Tool Failure

## Detection ID

```text
DET-AI-AGENT_REPEATED_TOOL_FAILURE
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Repeated tool failures may indicate prompt injection, misuse, or broken automation.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `ai_agent_audit_logs`

Required fields:

- `timestamp`
- `agent`
- `tool`
- `result`

## Normalized Logic

```text
tool failures exceed threshold for high risk tool
```

## Positive Sample Event

```json
{
  "event_id": "evt-ai-003",
  "agent": "soc-assistant",
  "tool": "revoke_session",
  "failures_10m": 8
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-ai-benign-003",
  "agent": "soc-assistant",
  "tool": "lookup_asset",
  "failures_10m": 2,
  "service_outage": true
}
```

## Expected False Positives

- service outage

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

Repeated failures against high-risk tools should pause the workflow.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-AI-AGENT_REPEATED_TOOL_FAILURE
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
