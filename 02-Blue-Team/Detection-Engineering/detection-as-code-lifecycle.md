---
title: Detection-as-Code Lifecycle
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [detection-as-code, siem, ci-cd, automation]
difficulty: intermediate
safe_publication: true
---


# Detection-as-Code Lifecycle

## Overview

Detection-as-code treats detection logic, metadata, tests, and triage guidance as
version-controlled security engineering assets. This improves quality,
repeatability, and change control.

## Lifecycle

```text
Idea → Draft Rule → Metadata → Test Event → Review → Deploy → Monitor → Tune → Retire
```

## Example Metadata

```yaml
id: det-identity-0001
name: Password spray followed by successful authentication
status: experimental
severity: high
confidence: medium
domain: identity
required_data_sources:
  - identity_signin_logs
required_fields:
  - timestamp
  - source_ip
  - user
  - result
false_positives:
  - vulnerability scanner
  - misconfigured service
  - shared VPN egress
owner: detection-engineering
review_date: 2026-09-18
```

## Repository Pattern

```text
detections/
  identity/
  windows/
  cloud/
tests/
  sample-events/
docs/
  triage/
metadata/
  data-sources.yml
```

## Pull Request Checklist

- [ ] Hypothesis is clear.
- [ ] Required fields are documented.
- [ ] Rule logic matches the hypothesis.
- [ ] Sample positive event exists.
- [ ] Sample benign event exists.
- [ ] False positives are documented.
- [ ] Triage guidance exists.
- [ ] Owner and review date are assigned.

## Deployment Stages

1. Local review.
2. Test with sample events.
3. Silent deployment or dashboard mode.
4. Low-severity alerting.
5. Production alerting.
6. Human-approved response workflow.
7. Automated response only after sustained reliability.

## Metrics

- Number of detections with tests
- Number of detections without owner
- Alert volume by rule
- False positive rate
- Last review date
- Time since last successful test

## Automation Ideas

- Validate metadata fields.
- Generate Markdown docs from detection YAML.
- Run sample events through logic.
- Flag expired review dates.
- Compare deployed detections to repository state.
