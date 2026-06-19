---
title: Detection — <Behavior Name>
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection]
difficulty: intermediate
safe_publication: true
---

# Detection — <Behavior Name>

## Detection ID

```text
DET-<DOMAIN>-<NUMBER>
```

## Hypothesis

If <threat behavior> occurs, then <telemetry source> should show <observable pattern>.

## Required Telemetry

| Source | Required fields |
|---|---|
|  |  |

## Normalized Logic

```text
<Platform-neutral pseudocode>
```

## Severity and Confidence

| Field | Value |
|---|---|
| Severity | low / medium / high / critical |
| Confidence | low / medium / high |

## Positive Sample Event

```json
{
  "sample_type": "positive",
  "expected_result": "alert"
}
```

## Benign Sample Event

```json
{
  "sample_type": "benign",
  "expected_result": "no_alert"
}
```

## False Positives

-

## Triage Workflow

1. Identify affected entities.
2. Review timeline.
3. Check approved business context.
4. Review related alerts.
5. Escalate if unexplained.

## Response Guidance

- Preserve evidence.
- Open an incident case if suspicious.
- Contain affected identity, host, or resource if confirmed.

## Test Plan

Describe how to test the detection with synthetic positive and benign events.

## Maintenance

| Field | Value |
|---|---|
| Owner |  |
| Review date | YYYY-MM-DD |
| Review cadence | quarterly |

## References

-
