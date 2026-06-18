# Project Status

Last updated: 2026-06-18

## Current State

The repository has moved from initial foundation into a Phase 2 candidate state.

Completed foundation items:

- Domain folder structure
- Documentation templates
- Content safety policy
- Taxonomy
- Contribution guide
- IOC schema and sample
- Validation scripts
- GitHub issue templates
- GitHub Actions validation workflow
- Dual-license model selected and documented

Phase 2 starter items added:

- Detection engineering methodology
- Detection-as-code lifecycle
- Windows authentication detection guidance
- SOC alert triage workflow
- Account compromise incident response playbook
- Threat hunting methodology
- Log source reference matrix

## Immediate Priorities

1. Confirm GitHub Actions pass on `main`.
2. Convert `BACKLOG.md` items into GitHub issues.
3. Promote the strongest pages from `draft` to `reviewed` after source review.
4. Add references to primary vendor documentation where required.
5. Create GitHub labels from `.github/labels.yml` if desired.

## Quality Gates

Before marking a document as `published`:

- [ ] No secrets or sensitive environment data
- [ ] No unsafe operational exploit guidance
- [ ] References added
- [ ] Defensive value is explicit
- [ ] Detection guidance includes false positives and limitations
- [ ] Automation opportunity is documented
- [ ] Markdown renders correctly
- [ ] Repository validation passes
