---
title: Detection Rule Examples
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [detection, examples, sigma, siem]
difficulty: intermediate
safe_publication: true
---


# Detection Rule Examples

## Overview

This page contains safe, defensive detection examples. The examples are not tied
to a single SIEM. They show how to structure logic, document assumptions, and
connect alerts to triage.

## Example 1 — Password Spray Pattern

### Hypothesis

If password spraying occurs, authentication logs may show many users with failed
logons from one source over a short window, possibly followed by a success.

### Required Fields

- `timestamp`
- `source_ip`
- `user`
- `result`
- `application`

### Pseudocode

```text
GROUP authentication_events BY source_ip OVER 15 minutes
WHERE result = "failure"
COUNT distinct user >= 20
AND COUNT failures per user <= 3
OPTIONALLY JOIN success from same source_ip within 30 minutes
```

### Example Sigma-Style Logic

```yaml
title: Possible Password Spraying From Single Source
status: experimental
logsource:
  category: authentication
condition: many_distinct_users_failed_from_same_source
fields:
  - source_ip
  - user
  - result
falsepositives:
  - Vulnerability scanner
  - Misconfigured service
  - Shared VPN egress
level: medium
```

### Triage

1. Identify source IP and user count.
2. Check if source belongs to VPN, scanner, or known service.
3. Look for successful authentication after failures.
4. Review MFA challenges and user reports.
5. Escalate if success occurred or privileged users were targeted.

## Example 2 — Privileged Group Membership Change

### Hypothesis

If an attacker escalates privileges, audit logs may show a user added to a
privileged group outside approved administrative workflow.

### Windows Events

- 4728: member added to global security group
- 4732: member added to local security group
- 4756: member added to universal security group

### Pseudocode

```text
WHERE event_id IN (4728, 4732, 4756)
AND target_group IN privileged_groups
AND actor NOT IN approved_identity_management_services
AND timestamp NOT IN approved_change_window
```

### Triage

- Who performed the change?
- Which group was changed?
- Was the target account newly created?
- Did the target account log in after the change?
- Was there an approved change request?

## Example 3 — New Cloud Access Key for Rarely Used Identity

### Hypothesis

If cloud credentials are created for persistence or misuse, audit logs may show a
new access key for an identity that rarely creates keys or has stale activity.

### CloudTrail Fields

- `eventName`
- `userIdentity.arn`
- `sourceIPAddress`
- `userAgent`
- `recipientAccountId`
- `requestParameters.userName`

### Pseudocode

```text
WHERE eventName = "CreateAccessKey"
JOIN identity_profile ON userIdentity.arn
WHERE identity_profile.key_creation_count_90d = 0
OR identity_profile.last_console_login > 90 days
```

### Response

- Validate change ticket.
- Deactivate suspicious key if unauthorized.
- Review actions performed by the new key.
- Rotate related credentials if exposure is suspected.

## Example 4 — Suspicious API Object Access Pattern

### Hypothesis

If an actor attempts object-level authorization abuse, application logs may show
one user requesting many object IDs that do not belong to their tenant.

### Pseudocode

```text
WHERE endpoint MATCHES "/api/*/{object_id}"
AND response_status IN (403, 404)
GROUP BY user, source_ip OVER 10 minutes
COUNT distinct object_id >= 50
```

### Triage

- Confirm whether the user is a legitimate integration.
- Check whether object IDs are sequential or random.
- Review successful accesses around failures.
- Confirm application authorization behavior.

## Documentation Checklist

Each detection should include:

- [ ] Hypothesis
- [ ] Required telemetry
- [ ] Logic
- [ ] False positives
- [ ] Triage
- [ ] Response
- [ ] Test method
- [ ] Owner and review date
