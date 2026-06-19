# Detection Rule Library

This directory contains platform-neutral detection metadata. These are not
copy-paste SIEM rules. They are reference artifacts that describe hypotheses,
required telemetry, false positives, triage, response, ownership, and review
cadence.

## Domains

| Directory | Focus |
|---|---|
| `identity` | Sign-in, MFA, OAuth, roles, account misuse |
| `windows` | Windows security and endpoint behavior |
| `cloud` | AWS and Azure control-plane events |
| `application` | API and application audit events |
| `kubernetes` | Kubernetes API audit behavior |
| `ai` | AI agent and tool-use audit events |

## Validation

Run:

```bash
python scripts/validate_detection_metadata.py
```

## Production Use

Before production use, convert metadata into your SIEM language, validate with
local log fields, tune false positives, add test events, and assign an owner.
