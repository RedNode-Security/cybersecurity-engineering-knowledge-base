---
title: Site Roadmap
description: How the VitePress site should evolve.
status: published
created: 2026-06-19
updated: 2026-06-19
tags: [vitepress, roadmap, site]
safe_publication: true
---

# Site Roadmap

## Current site model

This VitePress site is a curated public portal. The full reference library remains
in GitHub, where it can be reviewed, versioned, and validated.

## Next site improvements

1. Move the highest-value published pages into the VitePress site as native pages.
2. Add a native detection library browser.
3. Add Mermaid-rendered architecture diagrams.
4. Add domain-specific landing pages.
5. Add release notes and review status pages.
6. Add search-friendly summaries for CVEs, playbooks, and detections.

## Recommended content migration order

| Phase | Pages to make native in VitePress |
|---|---|
| 1 | Published references and detection overview |
| 2 | Identity and Windows detection references |
| 3 | Cloud and application security references |
| 4 | AI security and architecture references |
| 5 | CVE library and IR playbooks |

## Why not mirror everything immediately?

The repository is large. Publishing everything at once makes the site harder to
navigate. A curated portal gives users a clean entry point while the full
repository remains available for deep reference.
