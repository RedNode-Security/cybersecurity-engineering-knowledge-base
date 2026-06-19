---
title: Security Engineering Principles
domain: fundamentals
category: security-engineering
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [principles, architecture, risk]
difficulty: beginner
safe_publication: true
---


# Security Engineering Principles

## Overview

Security engineering is the practice of designing, building, operating, and
improving systems so they remain trustworthy under failure, misuse, and attack.
It is not only about tools. It is about making risk visible, reducing blast
radius, building evidence, and improving continuously.

## Core Model

```text
Asset → Threat → Control → Evidence → Response → Improvement
```

Example:

| Model item | Example |
|---|---|
| Asset | Customer database |
| Threat | Stolen admin credentials |
| Control | MFA, least privilege, network segmentation |
| Evidence | Sign-in logs, database audit logs, EDR telemetry |
| Response | Revoke sessions, rotate credentials, preserve logs |
| Improvement | Add privileged-access review and detection coverage |

## Principle 1 — Assume Breach

Assume at least one control will fail. Design so the failure is visible and
contained.

### Example

Weak design:

```text
One VPN login gives broad access to all internal systems.
```

Better design:

```text
VPN access only reaches a brokered application layer. Admin access requires MFA,
device compliance, role approval, and audited privileged sessions.
```

### Detection Ideas

- New admin logon from unmanaged device
- Sensitive database access from unusual host
- Privileged action after risky authentication

## Principle 2 — Least Privilege

Grant the minimum permission required for the minimum time required.

### Example

A CI/CD pipeline needs permission to deploy one application. It should not have
organization-wide administrator privileges.

Checklist:

- [ ] Permission is scoped to required resources.
- [ ] Long-lived credentials are avoided.
- [ ] Role assumption is logged.
- [ ] Unused permission is reviewed.
- [ ] Emergency access is separate and monitored.

## Principle 3 — Secure by Default

The default path should be the safe path. Security should not depend on every
engineer remembering optional hardening steps.

Examples:

- New storage buckets are private by default.
- New repositories have secret scanning enabled.
- New cloud accounts send audit logs centrally.
- New admin accounts require MFA.

## Principle 4 — Defense in Depth

Use multiple complementary controls so one failure does not become total failure.

Example layers for a sensitive API:

| Layer | Control | Evidence |
|---|---|---|
| Identity | Strong authentication | IdP sign-in logs |
| Authorization | Object-level checks | Application audit logs |
| Network | Restricted admin access | Firewall and proxy logs |
| Endpoint | EDR on admin workstation | Process and network events |
| Data | Encryption and audit | Database audit logs |
| Monitoring | Detection and alerting | SIEM alerts and cases |

## Principle 5 — Evidence-Driven Security

A control should produce evidence. If nobody can prove the control is working,
the organization is relying on assumption.

Questions:

- What log shows this action?
- Who reviews the evidence?
- How long is evidence retained?
- What alert fires when the control fails?
- What metric shows improvement?

## Principle 6 — Automation First, Not Automation Blindly

Automate repeatable tasks, but keep high-impact decisions human-approved until
reliability is proven.

Good early automation:

- Enrich alerts with asset owner and criticality.
- Validate IOC JSON fields.
- Check whether critical logs are flowing.
- Generate access review reports.

Risky automation:

- Automatically disabling executive accounts.
- Blocking production IP ranges from a low-confidence IOC.
- Rotating production secrets without dependency mapping.

## Worked Example — New Admin User Created

Scenario:

```text
An admin account is created in a cloud account outside a change window.
```

Security engineering analysis:

| Question | Answer |
|---|---|
| Asset | Cloud control plane |
| Threat | Unauthorized privilege creation |
| Control | IAM change approval, MFA, CloudTrail logging |
| Evidence | `CreateUser`, `AttachUserPolicy`, `ConsoleLogin` events |
| Detection | New admin user outside approved window |
| Response | Disable user, remove policy, review actor activity |
| Improvement | Add approval workflow and automated access review |

## Practical Checklist

For any system, document:

- [ ] Critical assets
- [ ] Privileged identities
- [ ] Trust boundaries
- [ ] Preventive controls
- [ ] Detective controls
- [ ] Required logs
- [ ] Response owner
- [ ] Safe automation opportunities
- [ ] Review cadence

## References

- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
- CIS Controls: https://www.cisecurity.org/controls
- MITRE ATT&CK: https://attack.mitre.org/
