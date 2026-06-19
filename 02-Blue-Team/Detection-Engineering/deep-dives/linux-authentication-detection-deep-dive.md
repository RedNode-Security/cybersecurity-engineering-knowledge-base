---
title: Linux Authentication Detection Deep Dive
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [linux, ssh, authentication, detection]
difficulty: advanced
safe_publication: true
---


# Linux Authentication Detection Deep Dive

## Scope

This page covers Linux authentication and privilege detection: SSH, sudo, user
creation, authorized keys, systemd services, and audit evidence.

## Primary Logs

| Log | Use |
|---|---|
| `/var/log/auth.log` | Debian/Ubuntu authentication and sudo |
| `/var/log/secure` | RHEL/CentOS authentication and sudo |
| `journalctl` | systemd service and host events |
| auditd | Detailed security audit events |
| EDR | Process, file, and network context |

## Detection Ideas

| Behavior | Signal |
|---|---|
| SSH brute force followed by success | failures then success from same source |
| New privileged user | user creation and sudo group membership |
| SSH key added | authorized_keys modification |
| Sudoers modified | change to sudoers or sudoers.d |
| New systemd service | service file creation and enablement |
| Unusual outbound connection | server connects to rare external IP |

## Example Auth Log Pattern

```text
Failed password for invalid user admin from 203.0.113.20
Accepted publickey for deploy from 198.51.100.10
sudo: deploy : TTY=pts/0 ; COMMAND=/usr/bin/systemctl restart app
```

Questions:

- Is `deploy` expected to log in interactively?
- Is the source expected?
- Was sudo use approved?
- Did a service file change before restart?

## False Positives

- Automation accounts
- Configuration management tools
- Deployment pipelines
- Emergency admin sessions
- Bastion host activity

## Response

- Preserve auth logs and shell history where appropriate.
- Review user and key changes.
- Check sudoers and systemd changes.
- Review outbound network activity.
- Rotate keys if compromise is suspected.
