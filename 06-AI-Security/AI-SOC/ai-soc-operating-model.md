---
title: AI SOC Operating Model
domain: ai-security
category: ai-soc
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [ai-soc, soc, automation, llm-security]
difficulty: advanced
safe_publication: true
---


# AI SOC Operating Model

## Scope

This page describes how AI assistance can support SOC work without replacing
control, accountability, or human judgment.

## Safe Use Cases

| Use case | Risk level |
|---|---|
| Summarize alert evidence | Low |
| Draft analyst notes | Low |
| Suggest triage checklist | Low |
| Query documentation | Low |
| Recommend containment | Medium |
| Execute containment | High |

## Control Model

```text
Alert → Evidence Bundle → AI Summary → Analyst Review → Policy Gate → Approved Action → Audit
```

## Requirements

- AI output must cite evidence sources or log IDs.
- Tool calls require policy checks.
- High-risk actions require human approval.
- Prompts and outputs are logged safely.
- Sensitive data is minimized.
- Model behavior is evaluated with test cases.

## Failure Modes

- Hallucinated timeline.
- Overconfident recommendation.
- Prompt injection from ticket or log text.
- Tool action without approval.
- Sensitive data copied into model context unnecessarily.

## Metrics

- Analyst time saved
- Recommendation acceptance rate
- Correction rate
- Unsafe recommendation count
- Missing evidence count
- Tool approval denial rate
