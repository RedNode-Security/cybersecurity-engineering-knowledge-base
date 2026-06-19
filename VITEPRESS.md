---
title: VitePress Site Guide
status: published
created: 2026-06-19
updated: 2026-06-19
tags: [vitepress, documentation, github-pages]
safe_publication: true
---

# VitePress Site Guide

## Overview

The public documentation site lives in `docs/` and is built with VitePress.
It acts as a curated portal into the full Cybersecurity Engineering Handbook.

## Local Development

```bash
npm install
npm run docs:dev
```

## Production Build

```bash
npm run docs:build
npm run docs:preview
```

## GitHub Pages

The deployment workflow is:

```text
.github/workflows/deploy-vitepress.yml
```

In repository settings, set GitHub Pages source to:

```text
GitHub Actions
```
