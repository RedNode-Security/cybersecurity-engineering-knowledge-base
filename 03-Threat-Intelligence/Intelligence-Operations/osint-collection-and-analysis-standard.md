---
title: OSINT Collection and Analysis Standard
domain: threat-intelligence
category: osint
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [osint, analysis, source-evaluation]
difficulty: advanced
safe_publication: true
---


# OSINT Collection and Analysis Standard

## Scope

This page defines a safe, repeatable OSINT workflow for cybersecurity research,
CVE tracking, IOC validation, and threat context. It does not cover intrusive or
unauthorized collection.

## Collection Principles

- Start with an intelligence requirement.
- Prefer primary sources.
- Record source, date, and confidence.
- Separate facts from assumptions.
- Avoid copying restricted or copyrighted material.
- Do not publish private victim data.

## Source Evaluation

| Question | Why it matters |
|---|---|
| Is the source primary? | Vendor advisories are stronger than summaries |
| Is the claim dated? | Exploitation and versions change |
| Is evidence provided? | Screenshots without context can mislead |
| Is there corroboration? | Multiple sources reduce uncertainty |
| Is attribution claimed? | Attribution requires strong evidence |

## Analysis Workflow

```text
Requirement → Source collection → Extraction → Corroboration → Confidence → Defensive action
```

## Example Requirement

```text
Which currently exploited vulnerabilities affect externally exposed identity, VPN, email, and cloud administration systems?
```

## Output Format

```yaml
requirement: exploited edge-device CVEs
source: vendor advisory
collected_at: 2026-06-19
claim: fixed version available
confidence: high
relevance: product present in asset inventory
action: create patch task and detection review
```

## Common Mistakes

- Treating social media claims as verified facts.
- Publishing indicators without context.
- Ignoring expiration dates.
- Copying exploit details into public notes.
- Confusing actor claims with evidence-backed attribution.
