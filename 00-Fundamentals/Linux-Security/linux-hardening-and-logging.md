---
title: Linux Hardening and Logging
domain: fundamentals
category: linux-security
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [linux, hardening, logging, ssh]
difficulty: beginner
safe_publication: true
---


# Linux Hardening and Logging

## Overview

Linux security depends on identity, permissions, service configuration, package
management, logging, network exposure, and operational discipline. A hardened
system is easier to defend because risky behavior becomes more visible and less
impactful.

## Core Areas

| Area | Defensive focus |
|---|---|
| Users and groups | Least privilege and account lifecycle |
| SSH | Strong authentication and restricted remote access |
| Sudo | Controlled privilege elevation and auditability |
| Services | Reduce exposed and unnecessary daemons |
| Packages | Patch known vulnerabilities |
| Logs | Preserve evidence for authentication and system changes |
| File permissions | Protect sensitive configuration and keys |

## Important Logs

| Log | Use |
|---|---|
| `/var/log/auth.log` or `/var/log/secure` | SSH, sudo, authentication events |
| `journalctl` | systemd service and system logs |
| `/var/log/syslog` or `/var/log/messages` | General system events |
| auditd logs | Detailed security audit events if configured |

## Example Auth Log

Synthetic event:

```text
Jun 18 10:22:14 linux01 sshd[1201]: Failed password for invalid user admin from 203.0.113.20 port 51244 ssh2
```

Questions:

- Is the source expected?
- How many users were attempted?
- Did any attempt succeed afterward?
- Is the host internet-facing?
- Are there repeated attempts across multiple hosts?

## Hardening Checklist

- [ ] Disable direct root SSH login.
- [ ] Prefer SSH keys or centralized identity with MFA where possible.
- [ ] Remove unused users and groups.
- [ ] Review sudoers entries.
- [ ] Disable unnecessary services.
- [ ] Enable host firewall rules.
- [ ] Keep packages updated.
- [ ] Forward logs centrally.
- [ ] Monitor new users, sudo changes, and service changes.

## Detection Ideas

- Multiple SSH failures followed by success.
- New user created outside provisioning process.
- Sudoers file modified.
- SSH key added to an account.
- New systemd service created.
- Unexpected outbound connection from a server.

## Automation Opportunities

- Daily report of users with sudo privileges.
- Alert on direct root login attempts.
- Check for unauthorized listening services.
- Compare installed packages against vulnerability data.
- Monitor integrity of SSH authorized keys for privileged users.

## References

- CIS Linux benchmarks: https://www.cisecurity.org/cis-benchmarks
- Linux audit documentation: https://linux.die.net/man/8/auditd
