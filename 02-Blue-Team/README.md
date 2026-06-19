# 02 — Blue Team

## Purpose

The blue-team section explains how to detect, investigate, contain, recover, and
improve. It connects telemetry, detection engineering, SOC triage, incident
response, threat hunting, malware investigation, and automation.

## Operating Model

```text
Telemetry → Detection → Enrichment → Triage → Response → Lessons Learned → Better Controls
```

## Detailed Pages

### Detection Engineering

- [Detection Engineering Overview](Detection-Engineering/README.md)
- [Detection Engineering Methodology](Detection-Engineering/detection-engineering-methodology.md)
- [Detection-as-Code Lifecycle](Detection-Engineering/detection-as-code-lifecycle.md)
- [Detection Rule Examples](Detection-Engineering/detection-rule-examples.md)
- [Windows Authentication Detection](Detection-Engineering/windows-authentication-detection.md)
- [Sample Detection Hypothesis](Detection-Engineering/sample-detection-hypothesis.md)

### SOC, IR, Hunting, and Telemetry

- [SOC Alert Triage Workflow](SOC-Operations/soc-alert-triage.md)
- [Incident Response Overview](Incident-Response/README.md)
- [Account Compromise Playbook](Incident-Response/account-compromise-playbook.md)
- [Example Account Compromise Case](Incident-Response/example-account-compromise-case.md)
- [Threat Hunting Methodology](Threat-Hunting/threat-hunting-methodology.md)
- [Log Source Reference Matrix](Log-Source-Strategy/log-source-reference-matrix.md)

## Example Analyst Workflow

Alert: unusual sign-in followed by privileged group change.

1. Identify actor, source, device, target group, and timestamp.
2. Review sign-ins for the previous 72 hours.
3. Check whether the group change is linked to a change ticket.
4. Enrich with user role, asset criticality, and MFA status.
5. Review endpoint telemetry from the source host.
6. Classify as benign, suspicious, or confirmed incident.
7. If confirmed: revoke sessions, reset password, remove privilege, preserve logs.
8. Create detection improvements based on gaps found during response.

## Blue-Team Quality Standard

A useful defensive page includes:

- Required telemetry
- Detection logic or hypothesis
- False positives
- Triage workflow
- Response actions
- Evidence to preserve
- Automation opportunities
- Examples or sample events
