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

LLM security addresses risks introduced by prompts, retrieval systems, agents, tools, data flows, and model outputs.

## Key Risks

- Prompt injection
- Data leakage
- Insecure tool use
- Untrusted retrieval content
- Over-permissive agents
- Weak evaluation and monitoring

## Defender Questions

- What data can the model access?
- What tools can the model call?
- What trust boundary separates user input, retrieved content, and system instructions?
- Are outputs monitored for policy violations?
- Are high-risk actions human-approved?

## Architecture Themes

- Least-privilege tool access
- Retrieval content isolation
- Prompt and output logging
- Human-in-the-loop approvals
- Evaluation-driven controls
