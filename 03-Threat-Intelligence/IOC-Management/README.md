---
title: IOC Management
domain: threat-intelligence
category: ioc-management
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [ioc, threat-intelligence]
difficulty: beginner
safe_publication: true
---

# IOC Management

## Overview

Indicators of compromise are observable artifacts associated with suspicious or malicious activity. They are useful when context, confidence, source, and expiration are maintained.

## IOC Quality Fields

- Type
- Value
- Source
- Confidence
- First seen
- Last seen
- Context
- Tags
- Expiration or review date

## Operational Guidance

- Treat IOCs as perishable intelligence
- Prefer behavior-based detection when possible
- Track source reliability
- Avoid adding low-confidence IOCs directly to blocking controls
- Document false positives

## Sample

See [`../samples/ioc-sample.json`](../samples/ioc-sample.json).
