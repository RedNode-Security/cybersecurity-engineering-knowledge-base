---
title: Priority Intelligence Requirements
domain: threat-intelligence
category: intelligence-operations
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [pir, threat-intelligence, requirements]
difficulty: advanced
safe_publication: true
---


# Priority Intelligence Requirements

## Overview

Priority Intelligence Requirements, or PIRs, define the questions threat
intelligence must answer for the organization. Without PIRs, intelligence teams
collect interesting information that may not change decisions.

## Good PIRs

Good PIRs are specific, decision-oriented, and tied to assets or operations.

Weak:

```text
What are threat actors doing?
```

Strong:

```text
Which actively exploited vulnerabilities affect our internet-facing identity, VPN, email, and cloud administration systems?
```

## Example PIRs

| PIR | Decision supported |
|---|---|
| Which KEV-listed CVEs affect internet-facing assets? | Emergency patch priority |
| Which phishing campaigns target our brand or users? | Email detection and awareness |
| Which cloud TTPs map to our AWS organization? | CloudTrail detections |
| Which indicators are safe for blocking? | Control deployment decision |
| Which actor behaviors require new detections? | Detection engineering backlog |

## Intelligence Requirements Workflow

```text
Business Risk → PIR → Collection Plan → Analysis → Defensive Action → Feedback
```

## Collection Plan Example

```yaml
pir: Actively exploited CVEs affecting internet-facing assets
sources:
  - vendor advisories
  - CISA KEV
  - NVD
  - EPSS
  - asset inventory
analysis_outputs:
  - prioritized CVE queue
  - patch owner mapping
  - detection opportunities
feedback:
  - remediation status
  - false positive notes
```

## Intelligence-to-Action Matrix

| Intelligence | Possible action |
|---|---|
| Exploited CVE | Patch, mitigate, detect, hunt |
| High-confidence IOC | Alert, block, enrich, hunt |
| Actor TTP | Detection hypothesis and tabletop scenario |
| Brand phishing | Email controls and user notification |
| Cloud abuse technique | CloudTrail analytic and IAM hardening |
