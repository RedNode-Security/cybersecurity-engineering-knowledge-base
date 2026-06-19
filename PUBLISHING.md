# Publishing Guide

This repository should not be published as a final reference just because the
files exist. A reference-grade knowledge base needs editorial review, source
review, safety review, and periodic maintenance.

## Publication Rule

A page is considered published only when all of the following are true:

- The page has clear scope and does not try to cover everything at once.
- Technical claims are supported by primary or reputable sources.
- Examples are synthetic, sanitized, or clearly safe to publish.
- Detection content includes telemetry, false positives, triage, and response.
- Unsafe exploit, evasion, persistence, or unauthorized-access guidance is absent.
- The page has been reviewed by a human maintainer.
- The front matter status is changed from `draft` to `reviewed` or `published`.

## Status Meaning

| Status | Meaning | Use when |
|---|---|---|
| `draft` | Useful but still under review | New or expanded content |
| `reviewed` | Checked for accuracy, safety, and clarity | Good public reference |
| `published` | Portfolio-grade and maintained | Stable reference page |
| `archived` | Retained but not maintained | Old or superseded content |

## Human Review Workflow

1. Read the page end to end.
2. Remove vague claims and filler.
3. Check every factual claim that could be wrong.
4. Confirm examples use documentation-safe values.
5. Confirm the safety policy is satisfied.
6. Add or improve references.
7. Run repository validation.
8. Promote status only after review.

## Release Cadence

Use small, intentional releases:

- **Patch release:** typo, link, formatting, or small clarification.
- **Minor release:** new reference page, playbook, detection, or example dataset.
- **Major release:** new domain, major restructuring, or publication milestone.

## Recommended First Published Set

Do not mark every page as published at once. Start with a small, strong set:

1. Security Engineering Principles
2. Detection Engineering Methodology
3. Password Spray Detection Reference
4. Account Compromise Response Reference
5. CVE-2021-44228 Log4Shell Reference
6. Broken Object Level Authorization Reference
7. Prompt Injection Defense Reference
8. SOC Reference Architecture

That gives visitors a credible first impression without overclaiming maturity.
