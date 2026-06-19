---
title: IR Playbook — Account Compromise
domain: blue-team
category: incident-response
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [incident-response, identity, account-compromise]
difficulty: intermediate
safe_publication: true
---


# IR Playbook — Account Compromise

## Objective

Investigate, contain, eradicate, and recover from suspected account compromise
while preserving evidence and minimizing business disruption.

## Scope

In scope:

- Corporate user accounts
- Privileged accounts
- Cloud accounts
- SaaS accounts
- Service accounts where applicable

Out of scope:

- Full malware reverse engineering
- Legal notification decisions
- HR disciplinary process

## Trigger Conditions

- Impossible travel or unusual sign-in
- MFA fatigue or suspicious MFA reset
- Password spray followed by success
- Privileged group or role change
- New OAuth consent or suspicious token use
- User report of unauthorized mailbox or file access
- Alert from detection engineering content

## Severity Criteria

| Severity | Criteria | Example response |
|---|---|---|
| Low | Suspicious sign-in but plausible explanation | Monitor and document |
| Medium | Suspicious sign-in plus sensitive app access | Revoke sessions and reset password |
| High | Confirmed misuse, privilege change, or data access | Contain account and investigate scope |
| Critical | Privileged account or broad tenant compromise | Incident command and emergency containment |

## Triage Checklist

- [ ] Identify account, source IP, device, application, and timestamp.
- [ ] Review sign-ins for 24 to 72 hours.
- [ ] Check MFA challenges, resets, and method changes.
- [ ] Review password resets and recovery changes.
- [ ] Review role assignments and group membership changes.
- [ ] Check mailbox rules, forwarding, and OAuth grants where relevant.
- [ ] Review endpoint telemetry for involved devices.
- [ ] Contact user through approved channel if appropriate.
- [ ] Decide containment level.

## Evidence to Preserve

| Evidence | Why it matters |
|---|---|
| Sign-in logs | Shows access timeline and source context |
| MFA logs | Shows challenge, success, failure, and method changes |
| Admin audit logs | Shows privilege or configuration changes |
| Mailbox audit logs | Shows forwarding, rules, and access |
| OAuth grant logs | Shows third-party app access |
| Endpoint telemetry | Shows whether source device is compromised |
| Analyst timeline | Preserves reasoning and decisions |

## Containment Options

Choose based on severity and business impact:

1. Revoke sessions.
2. Reset password.
3. Require MFA re-registration.
4. Temporarily disable account.
5. Remove unauthorized roles or groups.
6. Revoke suspicious OAuth grants.
7. Disable suspicious access keys or tokens.
8. Isolate endpoint if compromise is suspected.

## Eradication

- Remove malicious mailbox rules.
- Remove unauthorized app consent.
- Rotate exposed secrets.
- Remove unauthorized privileges.
- Fix weak authentication policy.
- Patch or rebuild compromised endpoint if needed.

## Recovery

- Restore legitimate access.
- Confirm MFA methods are trusted.
- Monitor account for recurrence.
- Notify stakeholders based on severity.
- Document residual risk and follow-up tasks.

## Lessons Learned

- Was the alert timely?
- Were logs complete?
- Were privileges excessive?
- Did MFA reduce impact?
- Did response require manual steps that can be automated?
- Which detection or control should change?

## Automation Opportunities

Automate:

- Sign-in summary generation
- MFA method change lookup
- Role and group change lookup
- OAuth grant summary
- Case template creation
- Post-incident task tracking

Require approval for:

- Account disablement
- Privilege removal
- Broad token revocation
- Production secret rotation
