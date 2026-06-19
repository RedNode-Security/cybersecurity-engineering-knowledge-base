---
title: Windows Authentication Detection
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [windows, authentication, detection, identity]
difficulty: intermediate
safe_publication: true
---


# Windows Authentication Detection

## Overview

Windows authentication logs are central to detecting credential misuse, password
attacks, lateral movement, privilege escalation, and unauthorized administrative
activity.

## Log Sources

| Source | Events | Value |
|---|---|---|
| Domain Controller Security logs | Kerberos, NTLM, group changes | Domain-level identity evidence |
| Endpoint Security logs | Local logon and local group changes | Host-level access evidence |
| PowerShell logs | Script execution after logon | Post-authentication activity |
| EDR | Process and network context | Confirms what happened after access |
| VPN and IdP | Remote access and MFA | Adds user and location context |

## Important Event IDs

| Event ID | Meaning | Detection use |
|---|---|---|
| 4624 | Successful logon | New source, unusual logon type, rare host access |
| 4625 | Failed logon | Password guessing and spraying |
| 4648 | Explicit credentials used | Run-as and lateral movement context |
| 4672 | Special privileges assigned | Privileged logon monitoring |
| 4720 | User account created | Unauthorized account creation |
| 4728 | Added to global security group | Privilege escalation monitoring |
| 4732 | Added to local security group | Local admin changes |
| 4740 | Account locked out | Password attack or user issue |
| 4768 | Kerberos TGT requested | Domain authentication baseline |
| 4769 | Kerberos service ticket requested | Service access patterns |
| 4771 | Kerberos pre-authentication failed | Password guessing signal |
| 4776 | NTLM credential validation | Legacy authentication monitoring |

## Logon Types Worth Understanding

| Logon type | Meaning | Investigation value |
|---|---|---|
| 2 | Interactive | Console login |
| 3 | Network | Access to shared resources or remote services |
| 4 | Batch | Scheduled task or batch job |
| 5 | Service | Service startup |
| 7 | Unlock | Workstation unlock |
| 10 | RemoteInteractive | RDP or terminal services |
| 11 | CachedInteractive | Cached domain credential use |

## Detection Scenario — Password Spray Followed by Success

Synthetic sequence:

```text
10:00 source=203.0.113.50 user=a.user result=failure event=4625
10:01 source=203.0.113.50 user=b.user result=failure event=4625
10:02 source=203.0.113.50 user=c.user result=failure event=4625
10:07 source=203.0.113.50 user=b.user result=success event=4624
```

Triage questions:

- How many unique users failed from the source?
- Did any privileged account fail or succeed?
- Was MFA challenged or satisfied?
- Is the source a VPN, proxy, scanner, or unknown internet address?
- What did the successful account do afterward?

## Detection Scenario — Privileged Group Change

Synthetic event:

```json
{
  "event_id": 4728,
  "actor": "EXAMPLE\helpdesk01",
  "target_user": "EXAMPLE\temp.admin",
  "target_group": "Domain Admins",
  "host": "dc01.example.com",
  "timestamp": "2026-06-18T12:10:00Z"
}
```

Triage questions:

- Is `helpdesk01` allowed to modify this group?
- Was `temp.admin` newly created?
- Was the change approved?
- Did the target account authenticate after the change?
- Did the actor authenticate from a normal workstation?

## False Positives

- Helpdesk password reset workflows
- Vulnerability scanners
- Service account password changes
- Admin maintenance windows
- VPN egress changes
- New device deployments

## Response Actions

- Reset or disable account if compromise is likely.
- Revoke sessions where supported.
- Remove unauthorized group memberships.
- Isolate affected endpoint if endpoint compromise is suspected.
- Preserve domain controller and endpoint logs.
- Hunt for the same source, account, or pattern across the environment.

## References

- Microsoft audit event documentation: https://learn.microsoft.com/windows/security/threat-protection/auditing/audit-events
- MITRE ATT&CK Credential Access: https://attack.mitre.org/tactics/TA0006/
