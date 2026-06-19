---
title: Zero Trust Reference Architecture
domain: architecture
category: zero-trust
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [zero-trust, identity, architecture]
difficulty: intermediate
safe_publication: true
---


# Zero Trust Reference Architecture

## Overview

Zero Trust is an architecture strategy based on explicit verification, least
privilege, continuous evaluation, and assumed breach.

## Core Principles

- Verify explicitly.
- Use least privilege.
- Assume breach.
- Evaluate risk continuously.
- Monitor access decisions.

## Components

| Component | Purpose |
|---|---|
| Identity provider | Authenticates users and workloads |
| Device posture | Evaluates endpoint health |
| Policy engine | Makes access decisions |
| Enforcement point | Applies access decisions |
| Asset inventory | Adds owner and criticality |
| Telemetry | Records decisions and anomalies |

## Example Access Decision

```text
User requests admin portal.
Policy checks: identity, MFA, device health, role, location, session risk.
Decision: allow, deny, or require step-up verification.
```

## Detection Ideas

- Privileged action after risky sign-in.
- Access from unmanaged device.
- Repeated denied access to sensitive application.
- Policy bypass attempts.

## References

- NIST SP 800-207: https://csrc.nist.gov/publications/detail/sp/800-207/final
- CISA Zero Trust Maturity Model: https://www.cisa.gov/zero-trust-maturity-model
