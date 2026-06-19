---
title: Detection Metadata Standard
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [detection-as-code, metadata, schema]
difficulty: advanced
safe_publication: true
---


# Detection Metadata Standard

## Overview

Detection metadata makes detections searchable, reviewable, testable, and
maintainable. Without metadata, a SIEM rule becomes tribal knowledge.

## Required Fields

| Field | Required | Description |
|---|---|---|
| `id` | Yes | Stable detection identifier |
| `name` | Yes | Human-readable name |
| `status` | Yes | experimental, production, deprecated |
| `hypothesis` | Yes | Behavior being detected |
| `severity` | Yes | low, medium, high, critical |
| `confidence` | Yes | low, medium, high |
| `data_sources` | Yes | Required logs |
| `required_fields` | Yes | Required normalized fields |
| `false_positives` | Yes | Expected benign triggers |
| `triage_steps` | Yes | Analyst workflow |
| `response_actions` | Yes | Possible response actions |
| `owner` | Yes | Team or person maintaining detection |
| `review_date` | Yes | Next review date |

## Example Detection Metadata

```json
{
  "id": "DET-IDENTITY-0001",
  "name": "Password Spray Followed by Success",
  "status": "production",
  "hypothesis": "Password spraying may show many failed logons across users from one source followed by a success.",
  "severity": "high",
  "confidence": "medium",
  "data_sources": ["identity_signin_logs"],
  "required_fields": ["timestamp", "source_ip", "user", "result"],
  "false_positives": ["vulnerability scanner", "misconfigured service", "shared VPN egress"],
  "triage_steps": [
    "Identify source IP and affected users",
    "Check for successful authentication after failures",
    "Review MFA results and user risk",
    "Escalate if privileged users succeeded"
  ],
  "owner": "detection-engineering",
  "review_date": "2026-09-18"
}
```

## Severity Guidance

| Severity | Use when |
|---|---|
| Low | Suspicious but low impact or weak signal |
| Medium | Requires review but no immediate containment |
| High | Possible compromise, privilege, or sensitive asset involved |
| Critical | Active compromise, broad impact, destructive action, or confirmed exfiltration |

## Confidence Guidance

| Confidence | Use when |
|---|---|
| Low | Experimental, weak telemetry, many false positives |
| Medium | Reasonable signal but needs analyst context |
| High | Strong behavior match with reliable telemetry and low noise |

## Review Questions

- Is the detection still mapped to a relevant threat?
- Are required fields still available?
- Has alert volume changed significantly?
- Are false positives documented and tuned?
- Is triage guidance still accurate?
- Has incident response feedback been incorporated?
