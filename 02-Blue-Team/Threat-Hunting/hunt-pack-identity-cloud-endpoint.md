---
title: Hunt Pack — Identity, Cloud, and Endpoint
domain: blue-team
category: threat-hunting
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [threat-hunting, identity, cloud, endpoint]
difficulty: advanced
safe_publication: true
---


# Hunt Pack — Identity, Cloud, and Endpoint

## Overview

This hunt pack provides hypothesis-driven hunts that combine identity, cloud, and
endpoint telemetry. Use only in environments you own or are authorized to monitor.

## Hunt 1 — Rare Admin Role Activation

### Hypothesis

Compromised privileged users may activate admin roles from unusual sources.

### Data Sources

- IdP sign-in logs
- Privileged access management logs
- Cloud audit logs
- Asset inventory

### Query Sketch

```text
WHERE role_activation = true
AND user.role = privileged
AND source_ip NOT IN user.previous_sources_90d
```

### Escalation

Escalate if role activation is followed by IAM, logging, or data access changes.

## Hunt 2 — Access Key Creation Followed by Enumeration

### Hypothesis

An actor may create a cloud access key and enumerate resources.

### Query Sketch

```text
CreateAccessKey
JOIN cloud_api_calls BY actor WITHIN 60 minutes
WHERE api_call IN (ListBuckets, ListUsers, DescribeInstances, GetCallerIdentity)
```

### False Positives

- New deployment pipeline
- Approved automation rollout
- Break-glass test

## Hunt 3 — Suspicious Script Execution After Risky Login

### Hypothesis

A compromised account may authenticate and then execute administrative scripts on
an endpoint.

### Query Sketch

```text
risky_signin(user)
JOIN endpoint_process(user) WITHIN 4 hours
WHERE process IN powershell_or_shell_interpreters
AND host_is_sensitive = true
```

## Hunt 4 — Data Access Spike After Privilege Change

### Hypothesis

Unauthorized privilege changes may be followed by abnormal data access.

### Query Sketch

```text
privilege_change(user)
JOIN application_data_access(user) WITHIN 24 hours
WHERE data_volume > user.baseline_p95
```

## Hunt Report Template

| Field | Value |
|---|---|
| Hypothesis |  |
| Time range |  |
| Data sources |  |
| Query summary |  |
| Findings |  |
| False positives |  |
| Detections created |  |
| Control improvements |  |
