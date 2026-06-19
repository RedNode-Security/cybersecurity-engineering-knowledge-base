# 01 — Red Team

## Purpose

This section documents authorized adversary-simulation methodology. The goal is
to understand attacker behavior so defenders can improve visibility, controls,
and response. It is not a place for weaponized payloads, stealth guidance, or
unauthorized activity.

## Safety Principles

- Written authorization comes first.
- Scope must be specific and time-bound.
- Testing must stop if it risks production stability or safety.
- Evidence should prove risk without exposing unnecessary sensitive data.
- Findings should create defensive action: hardening, detection, response, or architecture improvement.

## Methodology Flow

```text
Authorization → Scope → Asset Map → Threat Model → Test Plan → Evidence → Report → Defensive Improvement
```

## Detailed Pages

- [Rules of Engagement Checklist](rules-of-engagement-checklist.md)
- [Attack Surface Mapping Methodology](attack-surface-mapping-methodology.md)

## Example Safe Assessment Output

A safe public writeup might include:

- Objective: identify externally exposed assets owned by the organization.
- Scope: `example.com` and approved cloud account IDs.
- Method: compare internal asset inventory with approved external discovery data.
- Finding: three ownerless subdomains point to decommissioned services.
- Impact: takeover risk if DNS records remain stale.
- Defensive action: remove stale DNS records, add owner tags, monitor new DNS records.
- Detection opportunity: alert when public DNS records are created without owner metadata.

## What Not To Publish

Do not publish:

- Exploit chains against real targets
- Payloads that enable unauthorized access
- Stealth, evasion, persistence, or bypass instructions
- Private customer data, internal hostnames, or secrets
- Target lists or mass-scanning instructions
