---
title: Windows Detection References
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, windows, index]
difficulty: advanced
safe_publication: true
---


# Windows Detection References

## Purpose

This folder contains platform-neutral reference detections for the `windows`
domain. Each page includes a hypothesis, telemetry contract, sample data, false
positives, triage, response guidance, and test case mapping.

## Detections

- [Archive Created Before Large Upload](archive-created-before-upload.md)
- [Explicit Credentials Used on Rare Host](explicit-credentials-rare-host.md)
- [LSASS Access by Unusual Process](lsass-access-unusual-process.md)
- [New Local Administrator Added](new-local-admin-added.md)
- [New Service on Sensitive Host](new-service-sensitive-host.md)
- [Office Spawns Script Interpreter](office-spawns-script-interpreter.md)
- [PowerShell After Risky Logon](powershell-after-risky-logon.md)
- [PowerShell Encoded Command With Network](powershell-encoded-command-network.md)
- [Privileged Group Membership Change](privileged-group-membership-change.md)
- [Remote WMI Process Creation](wmi-process-creation-remote.md)
- [Scheduled Task Created by Unusual User](scheduled-task-unusual-user.md)
- [Security Tool Service Stopped](security-tool-service-stopped.md)
