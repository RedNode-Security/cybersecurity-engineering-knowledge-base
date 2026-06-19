# Editorial Style Guide

## Voice

Write like a security engineer explaining the topic to another practitioner. The
style should be direct, specific, and calm. Avoid marketing language, dramatic
claims, and generic filler.

Good:

```text
A password spray detection should count distinct users, not only failed events.
Otherwise one mistyped password can look similar to an attack.
```

Weak:

```text
Password spraying is a dangerous cyber threat that organizations must take very seriously.
```

## Human-Written Quality Rules

- Use concrete examples.
- Prefer short paragraphs.
- Explain tradeoffs.
- Include failure modes.
- Say when something depends on environment.
- Avoid repeating the same structure in every paragraph.
- Do not overstate confidence.
- Do not use buzzwords without operational meaning.

## Technical Writing Rules

- Define scope early.
- Separate facts from judgment.
- Use tables when comparing options.
- Use checklists for operational steps.
- Use synthetic examples for logs, IOCs, and case studies.
- Include what can go wrong.
- Include how to validate safely.

## Prohibited Style

Avoid phrases like:

- “In today's rapidly evolving threat landscape”
- “It is crucial to note”
- “Robust and comprehensive security posture”
- “Leverage cutting-edge capabilities”
- “Seamlessly integrates”

These phrases make the writing feel generic and less trustworthy.

## Example Before and After

Before:

```text
Organizations should implement robust logging to detect malicious activity.
```

After:

```text
For account compromise, sign-in logs are not enough. The analyst also needs MFA events, role changes, OAuth grants, and the first sensitive action after login. Without those joins, the alert may show a risky login but not the impact.
```

## Review Question

At the end of each page, ask:

```text
Would an experienced analyst, engineer, or architect learn exactly what to do next?
```

If the answer is no, the page needs another pass.
