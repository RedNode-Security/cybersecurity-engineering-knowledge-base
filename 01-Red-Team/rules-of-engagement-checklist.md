---
title: Rules of Engagement Checklist
domain: red-team
category: methodology
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [red-team, authorization, methodology]
difficulty: beginner
safe_publication: true
---


# Rules of Engagement Checklist

## Overview

Rules of engagement define the legal, operational, safety, and communication
boundaries for an authorized security assessment. They prevent ambiguity and make
sure the work creates defensive value without creating unnecessary business risk.

## Required Authorization

Before any testing begins, document:

| Field | Example |
|---|---|
| Approver | CISO or delegated system owner |
| Assessment owner | Security testing lead |
| Business owner | Application or platform owner |
| Scope start | 2026-07-01T09:00:00Z |
| Scope end | 2026-07-05T17:00:00Z |
| Emergency contact | security-incident@example.com |
| Stop authority | Incident commander or business owner |

## Scope Checklist

- [ ] In-scope domains are listed.
- [ ] In-scope applications are listed.
- [ ] In-scope IP ranges or cloud accounts are listed.
- [ ] In-scope test accounts are identified.
- [ ] Out-of-scope assets are explicitly listed.
- [ ] Testing windows and blackout windows are documented.
- [ ] Production-impacting actions require separate approval.
- [ ] Third-party dependencies are reviewed.

## Prohibited Actions Example

Unless separately authorized, prohibit:

- Destructive testing
- Persistence mechanisms
- Data exfiltration beyond minimal proof
- Denial-of-service testing
- Social engineering against employees
- Testing third-party systems
- Accessing customer data
- Modifying production data

## Stop Conditions

Testing should pause immediately if:

- System instability is observed.
- Customer-facing service impact occurs.
- Sensitive data is exposed unexpectedly.
- Testing reaches an out-of-scope asset.
- A third-party asset is discovered.
- The assessment team cannot contact the escalation owner.

## Evidence Handling

Evidence should prove the finding without creating additional risk.

Good evidence:

```text
Screenshot showing role name and timestamp, with sensitive values redacted.
```

Bad evidence:

```text
Full database export or full secret value copied into a report.
```

## Sample ROE Summary

```text
Assessment: External attack surface review
Scope: example.com, api.example.com, approved cloud account 123456789012
Dates: 2026-07-01 to 2026-07-05
Allowed: passive discovery, configuration review, authenticated test account review
Prohibited: destructive testing, persistence, social engineering, third-party testing
Stop contact: security-incident@example.com
Report due: 5 business days after assessment end
```

## Defensive Handoff

Each finding should include:

- Business impact
- Evidence
- Affected assets
- Recommended remediation
- Detection opportunity
- Logging gap if applicable
- Owner and target date

## Safety Boundary

This checklist supports authorized testing only. Do not use it for systems you do
not own or do not have explicit permission to assess.
