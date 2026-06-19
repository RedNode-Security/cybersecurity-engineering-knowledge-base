# 06 — AI Security

## Purpose

AI security addresses risks introduced by LLMs, retrieval systems, agents, tools,
data flows, model outputs, and evaluation gaps. The central engineering challenge
is separating trusted instructions from untrusted data while controlling tool use
and data exposure.

## AI Security Operating Model

```text
User Input → Policy Boundary → Model Context → Retrieval → Tool Use → Output → Monitoring → Evaluation
```

## Detailed Pages

- [LLM Security Overview](LLM-Security/README.md)
- [Prompt Injection Threat Model](LLM-Security/prompt-injection-threat-model.md)
- [Prompt Injection Evaluation Examples](LLM-Security/prompt-injection-evaluation-examples.md)
- [RAG Security Checklist](RAG-Security/rag-security-checklist.md)

## Example AI Security Question

If an AI assistant can read tickets and call tools, ask:

- Which tickets can it read?
- Which tools can it call?
- Can it change production systems?
- Does retrieved ticket text count as instruction or untrusted data?
- Which actions require human approval?
- What logs prove why a tool was called?

## AI Security Quality Standard

AI security pages should include:

- Trust boundaries
- Data flow
- Tool permissions
- Prompt injection risks
- Monitoring and evaluation plan
- Example safe/unsafe behavior
