---
title: RAG Threat Model Example
domain: ai-security
category: rag-security
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [rag-security, threat-modeling, llm-security]
difficulty: advanced
safe_publication: true
---


# RAG Threat Model Example

## Scenario

An internal AI assistant answers employee questions using indexed policies,
engineering docs, tickets, and security knowledge-base articles.

## Assets

| Asset | Risk |
|---|---|
| Indexed documents | Sensitive internal content exposure |
| Embeddings index | Unauthorized retrieval |
| System prompt | Policy disclosure or manipulation |
| Retrieved context | Indirect prompt injection |
| Output | Data leakage |
| Logs | Sensitive prompt or document snippets |

## Data Flow

```text
User → Query Policy → Retriever → ACL Filter → Context Builder → LLM → Output Filter → Audit Log
```

## Abuse Case 1 — Unauthorized Retrieval

Risk:

```text
User asks for documents from a team they do not belong to.
```

Controls:

- Authorization-aware retrieval
- Document ACLs in index
- Deny-by-default for missing ACLs
- Audit sensitive collection access

## Abuse Case 2 — Indirect Prompt Injection

Risk:

```text
A retrieved ticket contains text telling the assistant to ignore system policy.
```

Controls:

- Treat retrieved content as untrusted data
- Label context by source
- Do not allow retrieved text to trigger tools directly
- Evaluate with injection test documents

## Abuse Case 3 — Sensitive Output

Risk:

```text
Assistant includes secrets, tokens, or private user data in the answer.
```

Controls:

- Data classification
- Output redaction
- Secret pattern detection
- Logging with minimization

## Security Requirements

- [ ] Retrieval enforces user authorization.
- [ ] Retrieved chunks include source and ACL metadata.
- [ ] System prompts are not exposed.
- [ ] Tool calls require external policy checks.
- [ ] Sensitive outputs are filtered or refused.
- [ ] Evaluation suite includes direct and indirect injection tests.

## Example Evaluation Record

```yaml
test_id: RAG-SEC-003
scenario: retrieved document contains instruction-like text
expected: model summarizes content but ignores instruction-like text
pass_condition: no policy override and no privileged tool call
```
