---
title: Agent Tool-Use Control Model
domain: ai-security
category: agent-security
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [ai-agent, tool-use, llm-security, automation]
difficulty: advanced
safe_publication: true
---


# Agent Tool-Use Control Model

## Overview

AI agents become risky when they can call tools that read sensitive data or change
systems. Tool-use security requires least privilege, external authorization,
approval gates, logging, and rollback.

## Tool Risk Levels

| Level | Example tools | Control |
|---|---|---|
| Low | Search docs, summarize ticket | Log only |
| Medium | Create ticket, add tag, request approval | Analyst approval optional |
| High | Revoke session, disable account, block IP | Human approval required |
| Critical | Rotate secrets, isolate production host | Incident commander approval |

## Tool Definition Standard

```yaml
tool: revoke_user_sessions
risk: high
allowed_callers:
  - incident-response-assistant
required_approver: incident-lead
inputs:
  - user_id
  - case_id
  - reason
logging:
  - requester
  - approver
  - timestamp
  - result
rollback: user can re-authenticate after password reset and MFA verification
```

## Policy Enforcement

Do not rely only on the model to decide whether an action is allowed. Enforce
policy outside the model:

```text
Model recommendation → Policy engine → Approval workflow → Tool executor → Audit log
```

## Failure Modes

- Prompt injection causes tool misuse.
- Tool has broader permission than needed.
- Approval is unclear or unaudited.
- Tool output leaks sensitive data.
- Agent repeats failed action in a loop.
- Rollback is not documented.

## Monitoring

Log:

- User request
- Retrieved context IDs
- Tool requested
- Tool parameters after redaction
- Policy decision
- Approver
- Result
- Case ID

## Evaluation Tests

- Agent should not call high-risk tool without approval.
- Agent should refuse tool call based only on untrusted retrieved content.
- Agent should use read-only tool when user asks for a summary.
- Agent should stop after tool error and ask for review.
