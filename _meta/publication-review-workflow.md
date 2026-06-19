# Publication Review Workflow

## Overview

This workflow prevents the repository from becoming a large pile of unreviewed
notes. It creates a path from draft content to published reference material.

## Workflow

```text
Draft → Technical Review → Safety Review → Editorial Review → Published Index → Maintenance
```

## Step 1 — Draft

A draft may be incomplete, but it should still be safe to publish. Drafts can
contain TODOs, but they should not contain unsafe or private material.

## Step 2 — Technical Review

Reviewer checks:

- Accuracy
- Product-specific details
- References
- Examples
- Detection logic
- Operational steps

## Step 3 — Safety Review

Reviewer checks:

- No secrets
- No internal data
- No unsafe exploit guidance
- No target-specific details
- No unsupported attribution

## Step 4 — Editorial Review

Reviewer checks:

- Clear scope
- Human voice
- No filler
- Strong examples
- Good structure
- Useful conclusion

## Step 5 — Published Index

Only pages with `status: published` should be listed in a curated published
index. This keeps the public entry point clean.

## Step 6 — Maintenance

Every published page needs a review cadence:

- CVE pages: review when vendor guidance changes or quarterly if still relevant.
- Detection pages: review at least quarterly.
- Architecture pages: review semiannually.
- Playbooks: review after incidents or tabletop exercises.
