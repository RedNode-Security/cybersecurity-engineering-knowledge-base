---
title: Example Enrichment Workflow
domain: security-automation
category: automation-frameworks
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [automation, enrichment, example]
difficulty: intermediate
safe_publication: true
---


# Example Enrichment Workflow

## Scenario

A SIEM alert fires for unusual authentication followed by a privileged action.
The enrichment workflow gathers context before an analyst reviews the case.

## Input Alert

```json
{
  "alert_id": "alert-1001",
  "alert_name": "Unusual Sign-in Followed by Privileged Action",
  "user": "alex.admin@example.com",
  "source_ip": "203.0.113.77",
  "asset": "cloud-admin-portal",
  "severity": "high",
  "timestamp": "2026-06-18T09:31:00Z"
}
```

## Enrichment Steps

1. Look up user role and department.
2. Check whether user is privileged.
3. Look up asset owner and criticality.
4. Query recent sign-ins for the user.
5. Query recent privileged actions.
6. Check known maintenance windows.
7. Check whether source IP is known corporate infrastructure.
8. Produce an investigation summary.

## Example Output

```json
{
  "alert_id": "alert-1001",
  "user_context": {
    "department": "IT Operations",
    "privileged": true,
    "mfa_enabled": true
  },
  "asset_context": {
    "owner": "Cloud Platform Team",
    "criticality": "high"
  },
  "risk_context": {
    "new_source_ip_for_user": true,
    "approved_change_found": false,
    "privileged_action_count_1h": 2
  },
  "recommended_triage": [
    "Contact user through approved channel",
    "Review role activation event",
    "Check access key creation after sign-in"
  ]
}
```

## Human Approval Gates

Require approval before:

- Disabling account
- Removing privilege
- Blocking IP globally
- Revoking all user tokens
- Rotating production credentials

## Failure Modes

| Failure | Safe behavior |
|---|---|
| User lookup fails | Continue with unknown user context and flag missing data |
| Asset inventory unavailable | Do not lower severity automatically |
| Threat intel lookup times out | Mark enrichment incomplete |
| Conflicting data sources | Show both values and require analyst review |

## Metrics

- Enrichment completion rate
- Average enrichment time
- Missing context count
- Analyst feedback score
- False positive reduction
