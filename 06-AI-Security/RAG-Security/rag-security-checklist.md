---
title: RAG Security Checklist
domain: ai-security
category: rag-security
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [rag-security, llm-security, data-security]
difficulty: intermediate
safe_publication: true
---


# RAG Security Checklist

## Overview

Retrieval-Augmented Generation systems combine model prompts with retrieved
content. RAG security focuses on protecting data, preserving trust boundaries,
tracking provenance, and preventing retrieved content from becoming instructions.

## RAG Data Flow

```text
User Query → Retriever → Document Store → Context Builder → LLM → Output → Logs/Evaluation
```

## Trust Boundaries

| Boundary | Risk | Control |
|---|---|---|
| User query | Malicious or sensitive input | Input policy checks |
| Retriever | Over-broad access | Authorization-aware retrieval |
| Document store | Sensitive data exposure | ACLs and data classification |
| Retrieved content | Indirect prompt injection | Treat as untrusted data |
| Output | Leakage or unsafe advice | Output filtering and citations |

## Checklist

### Data Access

- [ ] Retrieval respects user authorization.
- [ ] Sensitive collections are labeled.
- [ ] Documents have owners and classification.
- [ ] Deleted documents are removed from indexes.
- [ ] Index refresh process is documented.

### Prompt Injection Controls

- [ ] Retrieved content is clearly separated from instructions.
- [ ] The model is told retrieved content is untrusted data.
- [ ] Documents are scanned for instruction-like patterns where useful.
- [ ] Tool use based on retrieved content requires policy checks.

### Output Controls

- [ ] Responses cite sources where possible.
- [ ] Sensitive values are redacted.
- [ ] The system avoids revealing hidden prompts or policies.
- [ ] The model indicates uncertainty when retrieval is weak.

### Monitoring

- [ ] User query, retrieved document IDs, and output metadata are logged safely.
- [ ] Retrieval failures are tracked.
- [ ] Sensitive collection access is monitored.
- [ ] Prompt injection attempts are counted.

## Example Failure Mode

A support knowledge-base article contains text that tells the assistant to ignore
all previous instructions. If the RAG system treats that text as instruction, the
assistant may behave incorrectly.

Safe behavior:

```text
The assistant summarizes the article and ignores instruction-like content inside it because retrieved documents are untrusted data.
```

## Evaluation Ideas

- Document with embedded instruction-like text.
- User without access asks for restricted document summary.
- Query attempts to extract hidden prompt.
- Retrieved document includes fake tool-use instruction.
- Output contains sensitive token pattern and should be redacted.
