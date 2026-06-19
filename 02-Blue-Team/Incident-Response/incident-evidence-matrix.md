---
title: Incident Evidence Matrix
domain: blue-team
category: incident-response
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [incident-response, evidence, dfir]
difficulty: advanced
safe_publication: true
---


# Incident Evidence Matrix

## Overview

An evidence matrix helps responders collect the right data quickly without
missing key sources. It also prevents unnecessary collection of sensitive data.

## Evidence by Incident Type

| Incident type | Primary evidence | Secondary evidence |
|---|---|---|
| Account compromise | Sign-in logs, MFA logs, audit logs | Endpoint telemetry, mailbox logs, OAuth grants |
| Malware execution | EDR process tree, file hashes, network connections | DNS, proxy, memory capture if approved |
| Cloud compromise | CloudTrail, IAM changes, key usage | VPC flow logs, GuardDuty, asset inventory |
| Data exposure | Application audit, database audit, object access logs | Proxy, DLP, storage access logs |
| Web attack | Web access logs, WAF logs, app logs | EDR on web host, database logs |

## Evidence Quality

| Quality | Description |
|---|---|
| Raw | Original log or artifact with timestamp |
| Normalized | Parsed into SIEM fields |
| Enriched | Includes asset, user, and business context |
| Correlated | Linked across multiple sources |
| Preserved | Exported or retained according to evidence process |

## Chain of Custody Fields

- Collector
- Timestamp
- Source system
- Collection method
- Hash or export identifier where applicable
- Storage location
- Access permissions
- Retention period

## Example Evidence Record

```yaml
case_id: IR-2026-001
artifact: identity-signin-export
source: example-idp
collected_by: analyst@example.com
collected_at: 2026-06-18T12:00:00Z
time_range: 2026-06-17T00:00:00Z to 2026-06-18T12:00:00Z
storage_location: secure-case-repository/IR-2026-001/signins.json
handling: internal-restricted
```

## Collection Priorities

1. Volatile or short-retention logs.
2. Identity and access evidence.
3. Control-plane audit logs.
4. Endpoint timeline.
5. Network and proxy evidence.
6. Business application audit logs.

## Common Gaps

- Logs retained for too few days.
- Timestamps in different time zones.
- Missing user or device identifiers.
- Evidence copied into unapproved tickets.
- No record of who collected the evidence.
