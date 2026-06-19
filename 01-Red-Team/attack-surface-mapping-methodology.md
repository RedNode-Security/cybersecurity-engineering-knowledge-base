---
title: Attack Surface Mapping Methodology
domain: red-team
category: attack-surface-mapping
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [attack-surface, reconnaissance, methodology]
difficulty: intermediate
safe_publication: true
---


# Attack Surface Mapping Methodology

## Overview

Attack surface mapping identifies exposed systems, applications, identities,
cloud resources, third-party dependencies, and ownership gaps. The purpose is to
improve defensive visibility and reduce unknown exposure.

## Authorized Use Only

Only map assets that are owned by your organization or explicitly authorized in
written scope. Do not perform mass scanning or target third-party systems.

## Mapping Model

```text
Scope → Asset Sources → Normalization → Exposure Review → Ownership → Risk → Remediation → Monitoring
```

## Data Sources

| Source | Example value | Why it matters |
|---|---|---|
| DNS inventory | `api.example.com` | Finds public names |
| Certificate transparency | `login.example.com` | Reveals public TLS names |
| Cloud inventory | Load balancers, public IPs | Identifies cloud exposure |
| CMDB | App owner and environment | Adds accountability |
| WAF/CDN config | Public app front doors | Shows expected entry points |
| IdP apps | SSO-integrated apps | Reveals identity-facing surfaces |

## Asset Inventory Example

| Asset | Type | Exposure | Owner | Criticality | Expected? |
|---|---|---|---|---|---|
| `www.example.com` | Web app | Public | Web Team | Medium | Yes |
| `api.example.com` | API | Public | Platform Team | High | Yes |
| `old-dev.example.com` | Web app | Public | Unknown | Unknown | No |
| `admin.example.com` | Admin portal | VPN only | IT Ops | High | Yes |

## Risk Factors

Higher priority assets often have:

- Public exposure
- Unknown owner
- Sensitive data
- Administrative functionality
- Weak or unknown authentication
- Stale DNS or cloud resources
- Missing logs or monitoring

## Workflow

1. Confirm scope and authorization.
2. Gather assets from approved internal sources.
3. Normalize asset names, owners, environments, and criticality.
4. Classify exposure: public, partner, internal, restricted, unknown.
5. Identify unexpected or ownerless assets.
6. Review authentication and administrative entry points.
7. Prioritize remediation by impact and exposure.
8. Create detection and monitoring improvements.

## Example Finding

```text
Finding: Ownerless public subdomain
Asset: old-dev.example.com
Observation: DNS record points to a decommissioned service endpoint.
Impact: Potential takeover or user confusion if record remains stale.
Recommendation: Remove DNS record, verify cloud resource deletion, add DNS owner review.
Detection opportunity: Alert when public DNS records lack owner metadata.
```

## Defensive Automation

- Detect newly created public DNS records.
- Compare DNS records against CMDB owners.
- Flag assets with unknown environment or owner.
- Alert on public cloud resources without approved tags.
- Create recurring review tickets for public admin portals.

## References

- OWASP Web Security Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
- CISA Attack Surface Management: https://www.cisa.gov/resources-tools/services/attack-surface-management
