---
title: Sample Detection Hypothesis
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [detection, hypothesis]
difficulty: beginner
safe_publication: true
---

# Sample Detection Hypothesis

## Hypothesis

An unusual authentication pattern followed by privileged action may indicate account misuse or compromised credentials.

## Required Telemetry

- Identity provider sign-in logs
- Privileged action audit logs
- Asset inventory
- User baseline or peer-group context

## Detection Logic Sketch

Look for:

1. Authentication from unusual location or device
2. Followed by privileged action within a short time window
3. Where the user has limited historical use of that privilege

## False Positives

- New employee onboarding
- Travel
- VPN or proxy routing changes
- Planned admin work

## Triage

- Confirm user and device context
- Review change ticket or admin request
- Check for additional suspicious activity
- Contact account owner if needed

## Response

- Reset credentials if compromise is suspected
- Revoke active sessions
- Review privilege assignment
- Preserve logs for investigation
