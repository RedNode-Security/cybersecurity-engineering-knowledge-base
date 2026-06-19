---
title: LLM Security
domain: ai-security
category: llm-security
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [llm-security, prompt-injection, rag-security]
difficulty: intermediate
safe_publication: true
---


# LLM Security

## Overview

LLM security protects model-enabled systems from prompt injection, data leakage,
unsafe tool use, untrusted retrieval content, memory risks, and weak evaluation.

## Local Pages

- [Prompt Injection Threat Model](prompt-injection-threat-model.md)
- [Prompt Injection Evaluation Examples](prompt-injection-evaluation-examples.md)

## Core Components

| Component | Risk | Control |
|---|---|---|
| User prompt | Direct injection | Input policy and refusal behavior |
| System prompt | Policy exposure | Do not reveal hidden instructions |
| Retrieved content | Indirect injection | Treat as untrusted data |
| Tools | Unauthorized action | Least privilege and approval gates |
| Memory | Persistent malicious state | Scope and expiration |
| Output | Sensitive disclosure | Redaction and monitoring |

## Design Rule

Untrusted content can be summarized, classified, and transformed. It should not
be allowed to redefine system behavior or grant permissions.
