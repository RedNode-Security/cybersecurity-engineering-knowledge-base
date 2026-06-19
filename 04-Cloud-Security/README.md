# 04 — Cloud Security

## Purpose

Cloud security protects identities, control-plane APIs, data stores, workloads,
network exposure, and audit logs. In cloud environments, identity and API actions
are often the real perimeter.

## Cloud Security Operating Model

```text
Identity → Control Plane → Workloads → Data → Network Exposure → Logging → Response
```

## Detailed Pages

- [AWS IAM Hardening Checklist](AWS-Security/aws-iam-hardening-checklist.md)
- [AWS CloudTrail Detection Examples](AWS-Security/aws-cloudtrail-detection-examples.md)

## Example Cloud Investigation

Alert: new access key created for an IAM user that has not used console access in
90 days.

1. Identify actor, key ID, source IP, user agent, and region.
2. Review recent `CreateAccessKey`, `AttachUserPolicy`, and `AssumeRole` events.
3. Check whether the user is a human or workload identity.
4. Confirm whether a change ticket or deployment explains the activity.
5. If suspicious, deactivate the key, preserve CloudTrail, and review follow-on actions.
6. Hunt for API calls from the new key across accounts and regions.

## Cloud Security Quality Standard

Cloud pages should include:

- Identity and permission impact
- Required logs
- Detection opportunities
- Misconfiguration examples
- Response actions
- Automation or policy-as-code ideas
