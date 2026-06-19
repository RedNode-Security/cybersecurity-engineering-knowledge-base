---
title: Prompt Injection Defense
description: Defensive engineering for LLM prompt injection, RAG, and agent tool use.
status: published
created: 2026-06-19
updated: 2026-06-19
tags: [llm-security, prompt-injection, ai-security]
safe_publication: true
---

# Prompt Injection Defense

## What it is

Prompt injection happens when untrusted text attempts to influence an LLM system
to ignore instructions, reveal sensitive data, misuse tools, or produce unsafe
output.

The core problem is that LLM applications often mix several types of text:

- system instructions,
- developer instructions,
- user input,
- retrieved documents,
- tool results,
- memory.

## Design principle

```text
Instructions and data must not have the same authority.
```

Retrieved documents, user prompts, and tool outputs should be treated as data.
They may be summarized or analyzed, but they should not be allowed to redefine
policy or grant permissions.

## Control layers

| Layer | Control |
|---|---|
| Input | Classify risky requests and sensitive intent |
| Context | Separate trusted instructions from untrusted data |
| Retrieval | Enforce authorization-aware retrieval |
| Tools | Apply least privilege and approval gates |
| Output | Redact sensitive data and enforce policy |
| Logging | Record prompts, retrieved IDs, tool calls, and decisions safely |
| Evaluation | Test direct and indirect injection cases |

## Tool-use rule

The model may recommend an action, but a policy engine should decide whether the
action is allowed.

```text
Model recommendation → Policy check → Human approval if needed → Tool execution → Audit log
```

## Monitoring signals

- repeated requests for hidden policy or system prompts,
- retrieved content containing instruction-like phrases,
- tool calls inconsistent with user intent,
- sensitive output redaction events,
- unusual increase in refusals or policy triggers.

## Related source file

- [Prompt Injection Defense Reference](https://github.com/RedNode-Security/cybersecurity-engineering-handbook/blob/main/06-AI-Security/LLM-Security/reference-prompt-injection-defense.md)
