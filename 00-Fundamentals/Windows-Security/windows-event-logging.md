---
title: Windows Event Logging
domain: fundamentals
category: windows-security
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [windows, logging, event-id, detection]
difficulty: beginner
safe_publication: true
---


# Windows Event Logging

## Overview

Windows event logs record authentication, account management, process execution,
PowerShell activity, service changes, policy changes, and many other events.
They are essential for detection engineering and incident response.

## Important Log Channels

| Channel | Why it matters |
|---|---|
| Security | Logon, privilege, account, group, and audit policy events |
| System | Service and driver events |
| PowerShell Operational | Script block and module activity when enabled |
| Windows Defender Operational | Malware and protection events |
| Task Scheduler Operational | Scheduled task registration and execution |
| Sysmon | Enhanced process, network, file, and registry telemetry if deployed |

## Common Security Event IDs

| Event ID | Meaning | Example use |
|---|---|---|
| 4624 | Successful logon | New source, unusual logon type, rare host access |
| 4625 | Failed logon | Password guessing and spraying |
| 4648 | Explicit credentials used | Run-as and lateral movement investigation |
| 4672 | Special privileges assigned | Privileged session monitoring |
| 4688 | Process created | Command execution if process auditing is enabled |
| 4720 | Account created | Unauthorized account creation |
| 4728 | Added to global security group | Domain privilege escalation |
| 4732 | Added to local security group | Local administrator changes |
| 4740 | Account locked out | Password attack or user issue |
| 4768 | Kerberos TGT requested | Domain authentication baseline |
| 4769 | Kerberos service ticket requested | Service access patterns |
| 4771 | Kerberos pre-authentication failed | Password guessing |

## Example Event Interpretation

Synthetic event:

```json
{
  "event_id": 4728,
  "timestamp": "2026-06-18T11:40:00Z",
  "actor": "EXAMPLE\j.smith",
  "target_user": "EXAMPLE\a.tempadmin",
  "group": "Domain Admins",
  "host": "dc01.example.com"
}
```

Questions:

- Is `j.smith` expected to modify privileged groups?
- Was there a change ticket?
- Was the target user newly created?
- Did the target user log in after being added?
- Did the actor authenticate from a normal device?

## Logging Baseline

- [ ] Account logon events are collected from domain controllers.
- [ ] Account management events are collected.
- [ ] Privilege use and group changes are monitored.
- [ ] PowerShell Script Block Logging is enabled where appropriate.
- [ ] Process command-line logging is enabled where appropriate.
- [ ] Logs are forwarded centrally.
- [ ] Time synchronization is working.
- [ ] Retention supports investigations.

## Detection Examples

- Privileged group membership change outside change window.
- Multiple failed logons for many users from one source.
- Explicit credential use followed by remote logon.
- New local administrator added on a workstation.
- PowerShell execution shortly after suspicious authentication.

## References

- Microsoft audit events: https://learn.microsoft.com/windows/security/threat-protection/auditing/audit-events
- Windows event forwarding: https://learn.microsoft.com/windows/security/operating-system-security/device-management/use-windows-event-forwarding-to-assist-in-intrusion-detection
