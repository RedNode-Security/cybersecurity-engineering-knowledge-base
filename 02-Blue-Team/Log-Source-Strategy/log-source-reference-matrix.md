---
title: Log Source Reference Matrix
domain: blue-team
category: log-source-strategy
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [logging, telemetry, siem, detection]
difficulty: beginner
safe_publication: true
---


# Log Source Reference Matrix

## Overview

A log source strategy defines which telemetry is required to detect, investigate,
and respond to security events. Detection quality is limited by telemetry quality.

## Matrix

| Domain | Log source | Required fields | Example detections |
|---|---|---|---|
| Identity | IdP sign-ins | user, source, result, MFA, app | Risky login, password spray |
| Windows | Security logs | event ID, user, host, logon type | Group change, lateral movement |
| Endpoint | EDR | process, parent, command line, hash | Suspicious script execution |
| Network | DNS | query, client, response, timestamp | Beaconing, tunneling suspicion |
| Network | Proxy | URL, user, action, category | Phishing and malware downloads |
| Cloud | Audit logs | actor, action, resource, region | New keys, logging tampering |
| Application | App audit | user, object, action, result | Data access abuse |
| Email | Gateway logs | sender, recipient, URL, attachment | Phishing triage |

## Log Quality Checklist

- [ ] Timestamps are normalized.
- [ ] User and host fields are populated.
- [ ] Event outcome is clear.
- [ ] Logs are retained long enough.
- [ ] Logs can be joined with asset and identity context.
- [ ] Sensitive fields are protected.
- [ ] Ingestion health is monitored.

## Example Gap

```text
Detection idea: suspicious API object access
Required logs: application audit logs with user, endpoint, object_id, tenant_id, result
Gap: application logs do not include tenant_id
Action: create engineering ticket to add tenant_id to audit events
```

## Automation Ideas

- Monitor log source health.
- Generate data source coverage reports.
- Alert when critical log ingestion stops.
- Track detections that depend on missing fields.
- Report retention gaps by data source.

## References

- MITRE ATT&CK Data Sources: https://attack.mitre.org/datasources/
