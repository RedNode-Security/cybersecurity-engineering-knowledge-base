---
title: Risk Register and Control Evidence
domain: fundamentals
category: risk-management
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [risk, controls, evidence, governance]
difficulty: intermediate
safe_publication: true
---


# Risk Register and Control Evidence

## Overview

A risk register turns security concerns into tracked decisions. Control evidence
proves whether security controls are actually operating. Elite security teams do
not only say a control exists; they can show evidence, owner, review cadence,
exceptions, and improvement history.

## Core Model

```text
Risk → Control → Evidence → Owner → Review → Exception → Improvement
```

## Risk Register Fields

| Field | Description | Example |
|---|---|---|
| Risk ID | Stable identifier | RISK-ID-001 |
| Scenario | What could happen | Compromised admin account modifies cloud logging |
| Asset | What is affected | Production AWS organization |
| Likelihood | Probability estimate | Medium |
| Impact | Business impact | High |
| Existing controls | Current mitigations | MFA, CloudTrail, SCP, alerting |
| Evidence | Proof controls operate | CloudTrail logs, IAM review export |
| Owner | Responsible person/team | Cloud Platform Team |
| Treatment | Mitigate, transfer, accept, avoid | Mitigate |
| Due date | Target date | 2026-09-18 |
| Residual risk | Remaining risk after controls | Medium |

## Example Risk Record

```yaml
risk_id: RISK-CLOUD-001
scenario: CloudTrail logging is disabled or modified by a compromised privileged identity.
asset: AWS production organization
impact: high
likelihood: medium
existing_controls:
  - MFA for privileged roles
  - CloudTrail organization trail
  - alert on StopLogging and DeleteTrail
  - service control policy restricting logging changes
control_evidence:
  - CloudTrail event selector configuration export
  - SIEM alert test result
  - SCP policy review record
owner: Cloud Platform Team
treatment: mitigate
review_date: 2026-09-18
```

## Control Evidence Examples

| Control | Evidence |
|---|---|
| MFA for admins | IdP policy export and admin login sample |
| Centralized logging | Log source health dashboard and retention setting |
| Least privilege | Access review report and unused permission findings |
| Incident response | Tabletop report and playbook execution evidence |
| Vulnerability management | Patch SLA report and exception register |
| Detection engineering | Detection test result and alert volume metrics |

## Evidence Quality Levels

| Level | Description | Example |
|---|---|---|
| Weak | Statement without proof | “MFA is enabled” |
| Better | Configuration snapshot | Export of MFA policy |
| Strong | Configuration plus operational event | MFA policy and recent admin MFA logs |
| Elite | Continuous evidence with review | Dashboard, alerting, owner, exceptions, test history |

## Control Failure Questions

For each important control, ask:

- How would we know if this control stopped working?
- Who owns the alert?
- How quickly would we notice?
- What evidence proves recovery?
- What exceptions exist?
- When was it last tested?

## Automation Opportunities

- Generate monthly access review evidence.
- Pull log source health into a control dashboard.
- Create tickets for expired risk exceptions.
- Compare cloud configuration against policy-as-code baseline.
- Track which detections have test evidence.

## Executive Summary Template

```text
Risk: Privileged cloud identity misuse
Current rating: High
Treatment: Mitigate
Progress: 3 of 5 controls implemented
Evidence: MFA policy export, CloudTrail alert test, access review completed
Residual risk: Medium until privileged access workflow is fully implemented
Next action: deploy approval workflow for production admin role assumption
```
