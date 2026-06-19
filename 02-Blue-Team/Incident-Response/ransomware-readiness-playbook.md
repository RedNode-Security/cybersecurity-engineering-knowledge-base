---
title: Ransomware Readiness Playbook
domain: blue-team
category: incident-response
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [incident-response, ransomware, readiness]
difficulty: advanced
safe_publication: true
---


# Ransomware Readiness Playbook

## Overview

This playbook focuses on readiness, detection, containment, recovery, and
executive coordination for ransomware-style incidents. It does not contain
offensive or destructive guidance.

## Readiness Controls

- [ ] Critical assets and owners are documented.
- [ ] Backups are offline, immutable, or protected from admin compromise.
- [ ] Restore tests are performed regularly.
- [ ] EDR is deployed on critical endpoints and servers.
- [ ] Privileged access is minimized.
- [ ] Network segmentation limits lateral movement.
- [ ] Incident communication channels are pre-approved.
- [ ] Legal, privacy, executive, and communications contacts are documented.

## Detection Signals

| Signal | Data source |
|---|---|
| Mass file rename or write activity | EDR, file server logs |
| Security tool tampering | EDR, Windows events, admin logs |
| Suspicious remote admin tool use | EDR, Windows logs |
| Large internal lateral movement | Network and authentication logs |
| Backup deletion or modification | Backup platform logs |
| Unusual privileged account use | IdP, AD, PAM, CloudTrail |

## First 60 Minutes

1. Declare incident severity.
2. Establish incident command channel.
3. Identify affected systems and business processes.
4. Preserve identity and endpoint evidence.
5. Contain affected hosts or network segments if approved.
6. Protect backups and backup admin accounts.
7. Disable compromised credentials if confirmed.
8. Begin executive and legal notification workflow.

## Containment Decision Tree

```text
Is encryption active?
  yes → isolate affected segment or hosts if approved
  no → preserve evidence and identify staging/lateral movement
Are privileged credentials compromised?
  yes → revoke sessions, rotate credentials, review admin activity
Are backups at risk?
  yes → restrict backup admin access and preserve backup logs
```

## Recovery Questions

- Which systems are trusted for restore?
- Which backups are clean?
- What is the restore priority by business process?
- Which credentials must be rotated before reconnecting systems?
- Which detections must remain active during recovery?

## Lessons Learned

- Was initial access detected?
- Was lateral movement contained?
- Were backups protected?
- Did segmentation work?
- Were communications effective?
- Which controls need investment?
