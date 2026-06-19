---
title: Windows Endpoint Detection Deep Dive
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [windows, endpoint, edr, deep-dive]
difficulty: advanced
safe_publication: true
---


# Windows Endpoint Detection Deep Dive

## Scope

This page focuses on defensive Windows endpoint telemetry: process creation,
PowerShell, services, scheduled tasks, registry persistence, credential access
signals, and triage workflows.

## Telemetry Layers

| Layer | Example source | Value |
|---|---|---|
| Authentication | Security event log | Who accessed the host |
| Process | EDR or event 4688 | What executed |
| Script | PowerShell operational logs | What script content ran |
| Service | System logs and EDR | Persistence and admin activity |
| Scheduled task | Task Scheduler logs | Persistence and automation |
| Network | EDR network telemetry | External or lateral connections |
| File/registry | EDR or Sysmon | Persistence and payload staging |

## Process Tree Triage

When reviewing an endpoint alert, ask:

- What is the parent process?
- Is the parent expected to spawn this child?
- Which user context executed it?
- Was the command line interactive, scripted, encoded, or hidden?
- Did the process connect to the network?
- Did it write files or modify persistence locations?

## Example Suspicious Chain

```text
outlook.exe → powershell.exe → cmd.exe → archive utility → outbound connection
```

This chain is not automatically malicious, but it needs context. It may represent
user automation, a legitimate add-in, or suspicious post-phishing behavior.

## Common High-Value Detections

| Behavior | Data needed |
|---|---|
| Office spawning script interpreter | process parent/child and command line |
| PowerShell with unusual flags | command line and script block logs |
| New service creation | service name, binary path, actor |
| Scheduled task creation | task name, action, actor |
| LSASS access by unusual process | EDR process access telemetry |
| Archive creation before upload | file events, process events, proxy logs |

## False Positives

- Admin scripts
- Software deployment tools
- Endpoint management agents
- Backup software
- Developer build tools
- IT support remote sessions

## Triage Workflow

1. Confirm user and host.
2. Build process tree.
3. Check file hash and signing status.
4. Review network connections.
5. Check persistence changes.
6. Compare against known management tools.
7. Decide whether host isolation is needed.

## Response Guidance

Do not isolate every suspicious process automatically. Isolate when there is
strong evidence of active compromise, lateral movement, credential access, or
ongoing data loss.
