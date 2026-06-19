---
title: PowerShell Detection Deep Dive
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [powershell, windows, detection, deep-dive]
difficulty: advanced
safe_publication: true
---


# PowerShell Detection Deep Dive

## Scope

PowerShell is a legitimate administrative tool and a common post-compromise tool.
Detection should focus on context, parent process, execution pattern, and follow-on
behavior rather than treating every PowerShell event as malicious.

## Useful Telemetry

| Source | Value |
|---|---|
| PowerShell Script Block Logging | Script content when enabled |
| Module Logging | Module and command usage |
| Process command line | Flags, parent, user, execution path |
| EDR telemetry | Process tree, network, file writes |
| Windows Security logs | User context and logon type |

## Risk Indicators

| Indicator | Why it matters |
|---|---|
| Office parent process | May indicate phishing or macro-based execution |
| Hidden or non-interactive execution | Common in automation and abuse; needs context |
| Encoded command | Often used to carry complex scripts; also used by legitimate tools |
| Download and execute pattern | Higher risk when followed by network retrieval |
| Security tool tampering commands | Potential defense impairment |
| Credential or token access | High-risk behavior |

## Detection Approach

Good detection is layered:

```text
PowerShell event + suspicious parent + unusual user/host + network or credential behavior
```

Weak detection:

```text
powershell.exe executed
```

## Example Triage

```text
Parent: winword.exe
Child: powershell.exe
User: finance.user@example.com
Host: FIN-WKS-12
Network: outbound connection to 198.51.100.20
Context: user opened external attachment minutes earlier
Decision: suspicious; escalate and preserve endpoint evidence
```

## False Positives

- Endpoint management scripts
- Login scripts
- Software deployment
- Backup or monitoring agents
- Developer automation

## Hardening and Logging

- Enable PowerShell Script Block Logging where appropriate.
- Forward logs centrally.
- Monitor high-risk parent-child relationships.
- Maintain allowlist of management tools and signed scripts.
- Review script execution on sensitive servers.

## Response

- Preserve script content and command line.
- Review parent process and user activity.
- Check network connections and downloaded files.
- Hunt for same command or hash across hosts.
- Isolate host only when evidence supports active compromise.
