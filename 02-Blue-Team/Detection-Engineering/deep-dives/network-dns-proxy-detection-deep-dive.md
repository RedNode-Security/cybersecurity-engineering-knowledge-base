---
title: Network DNS and Proxy Detection Deep Dive
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [dns, proxy, network, detection]
difficulty: advanced
safe_publication: true
---


# Network DNS and Proxy Detection Deep Dive

## Scope

This page covers DNS and proxy telemetry for detecting phishing, malware staging,
beaconing, tunneling suspicion, and suspicious data access patterns.

## DNS Detection Ideas

| Behavior | Signal |
|---|---|
| Newly observed domain | domain first seen recently in environment |
| Beaconing | regular interval queries from same host |
| Tunneling suspicion | long labels, high entropy, high query volume |
| Phishing follow-up | user click followed by suspicious domain query |
| Malware infrastructure | domain from high-confidence IOC source |

## Proxy Detection Ideas

| Behavior | Signal |
|---|---|
| Suspicious download | executable or archive from rare domain |
| Data upload spike | high outbound volume to unusual destination |
| Policy violation | blocked category followed by allowed alternate domain |
| Credential phishing | login-looking path on newly observed domain |

## Required Fields

| Source | Fields |
|---|---|
| DNS | timestamp, client, query, response, query type |
| Proxy | timestamp, user, host, URL, method, status, bytes, category |
| EDR | process, command line, destination, user |
| Asset inventory | host owner, criticality, environment |

## Triage Workflow

1. Identify host and user.
2. Check domain age and environment first-seen time.
3. Determine process responsible for connection if EDR is available.
4. Review related downloads or uploads.
5. Check whether other hosts contacted the same destination.
6. Escalate if sensitive asset or suspicious process is involved.

## False Positives

- Content delivery networks
- Software updates
- Security tools
- Browser prefetching
- Developer package managers

## Automation

- Build a newly observed domain feed from internal DNS.
- Enrich domains with internal first-seen and prevalence.
- Join proxy downloads to endpoint process events.
- Flag rare destinations contacted by servers.
