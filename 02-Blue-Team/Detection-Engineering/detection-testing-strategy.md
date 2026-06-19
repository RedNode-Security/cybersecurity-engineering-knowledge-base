---
title: Detection Testing Strategy
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [testing, detection-as-code, quality]
difficulty: advanced
safe_publication: true
---


# Detection Testing Strategy

## Overview

Detection testing proves that detections still work after query changes, parser
changes, log-source changes, and SIEM migrations. Elite teams test detections the
way software teams test code.

## Test Types

| Test type | Purpose | Example |
|---|---|---|
| Positive test | Rule catches expected behavior | Password spray sample event triggers alert |
| Negative test | Rule ignores benign behavior | Single failed login does not alert |
| Boundary test | Threshold works correctly | 19 users no alert, 20 users alert |
| Missing-field test | Rule fails safely | Missing source IP does not create high-confidence alert |
| Regression test | Prior bug stays fixed | Scanner allowlist no longer pages SOC |

## Sample Positive Event

```json
{
  "timestamp": "2026-06-18T10:00:00Z",
  "source_ip": "203.0.113.50",
  "user": "user01@example.com",
  "result": "failure",
  "event_category": "authentication"
}
```

## Test Case Format

```yaml
test_id: TEST-DET-IDENTITY-0001-positive
rule_id: DET-IDENTITY-0001
input: samples/password-spray-positive.json
expected:
  alert: true
  severity: high
  confidence: medium
```

## Test Data Safety

Use synthetic or sanitized data:

- Documentation IPs from RFC 5737
- `example.com` identities
- `.invalid` domains
- Placeholder hashes
- Redacted hostnames

Do not use real customer data, secrets, or private incident details in public test
fixtures.

## CI/CD Quality Gates

- [ ] Metadata validates against schema.
- [ ] Required fields are present.
- [ ] Positive tests trigger.
- [ ] Negative tests do not trigger.
- [ ] Markdown documentation exists.
- [ ] Owner and review date are present.
- [ ] Links to playbooks are valid.

## Example Regression Scenario

Problem:

```text
The password spray detection fired repeatedly for a scheduled vulnerability scanner.
```

Fix:

```text
Add enrichment that marks approved scanner identity and suppresses only during approved scan windows.
```

Regression test:

```text
Scanner activity during approved window should not page SOC. Scanner activity outside the window should still alert.
```
