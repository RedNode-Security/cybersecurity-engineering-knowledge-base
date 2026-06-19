# 07 — Security Automation

## Purpose

Security automation reduces repetitive work, improves consistency, and speeds up
response. Good automation enriches, validates, routes, and documents before it
attempts disruptive containment.

## Automation Maturity Model

```text
Manual checklist → Scripted helper → Enrichment pipeline → Orchestrated workflow → Human-approved response
```

## Detailed Pages

- [Security Enrichment Pipeline Design](enrichment-pipeline-design.md)
- [Example Enrichment Workflow](example-enrichment-workflow.md)

## Good First Automations

- Validate IOC JSON.
- Generate an enriched alert summary.
- Check log source health.
- Add asset owner and criticality to alerts.
- Create case templates.
- Flag stale indicators and detections.

## Risky Automations

Use human approval for actions that disable accounts, block infrastructure, modify
firewalls, delete data, revoke production credentials, or affect customers.

## Automation Quality Standard

Automation content should include:

- Inputs and outputs
- Required fields
- Failure modes
- Audit logging
- Rollback or approval plan
- Example input and output
