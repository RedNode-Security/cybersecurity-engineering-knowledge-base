---
title: Reference — Prompt Injection Defense
domain: ai-security
category: llm-security
status: published
created: 2026-06-18
updated: 2026-06-19
tags: [prompt-injection, llm-security, reference]
difficulty: advanced
safe_publication: true
---


# Reference — Prompt Injection Defense

## Scope

This page covers defensive engineering for prompt injection in LLM applications.
It focuses on trust boundaries, tool control, retrieval security, monitoring, and
evaluation. It does not provide bypass techniques.

## Core Problem

LLM applications often mix several kinds of text:

- System instructions
- Developer instructions
- User input
- Retrieved documents
- Tool results
- Memory

Prompt injection becomes dangerous when untrusted text influences privileged
behavior, reveals sensitive data, or triggers tools outside the user's authority.

## Design Principle

```text
Instructions and data must not have the same authority.
```

Retrieved documents, user prompts, and tool outputs should be treated as data.
They may be summarized or analyzed, but they should not be allowed to redefine
policy or grant permissions.

## Control Layers

| Layer | Control |
|---|---|
| Input | Classify risky requests and sensitive intent |
| Context | Separate trusted instructions from untrusted data |
| Retrieval | Enforce authorization-aware retrieval |
| Tools | Apply least privilege and approval gates |
| Output | Redact sensitive data and enforce policy |
| Logging | Record prompts, retrieved IDs, tool calls, and decisions safely |
| Evaluation | Test direct and indirect injection cases |

## Tool-Use Rule

The model may recommend an action, but a policy engine should decide whether the
action is allowed.

```text
Model recommendation → Policy check → Human approval if needed → Tool execution → Audit log
```

## Example Evaluation Case

| Field | Value |
|---|---|
| Test | Retrieved document contains instruction-like text |
| Risk | Model treats document as system instruction |
| Expected behavior | Model summarizes the document but ignores instruction-like content |
| Evidence | No privileged tool call, no policy override, source ID logged |

## Monitoring Signals

- Repeated requests for hidden policy or system prompts
- Retrieved content containing instruction-like phrases
- Tool calls inconsistent with user intent
- Sensitive output redaction events
- Unusual increase in refusals or policy triggers

## Common Mistakes

- Giving the model broad production tools.
- Treating retrieved content as trusted instruction.
- Relying only on a prompt to enforce policy.
- Logging sensitive prompts without redaction.
- Having no regression tests for injection scenarios.

## References

- OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- MITRE ATLAS: https://atlas.mitre.org/
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
