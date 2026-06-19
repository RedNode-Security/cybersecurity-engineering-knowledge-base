---
title: Detection Reference Library Index
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, reference-library, index]
difficulty: advanced
safe_publication: true
---


# Detection Reference Library Index

## Purpose

This directory contains human-readable reference pages for the detection metadata
rules under `../rules/`. Each page explains the detection in practical analyst
language and includes sample data.

## Domain Folders

| Folder | Coverage |
|---|---|
| `identity` | Sign-in, MFA, OAuth, roles, privileged identity |
| `windows` | Windows endpoint and security event behavior |
| `linux` | Linux authentication, privilege, and persistence signals |
| `network` | DNS, proxy, egress, and beaconing behavior |
| `cloud` | AWS and Azure control-plane detection |
| `kubernetes` | Kubernetes audit and workload security |
| `application` | API, GraphQL, authorization, and sensitive operations |
| `ai` | LLM, RAG, and AI agent security telemetry |

## Review Standard

Every detection page should answer:

1. What behavior is being detected?
2. Which telemetry is required?
3. What does a positive event look like?
4. What does benign activity look like?
5. What false positives are expected?
6. What should the analyst do next?
7. How should the detection be tested?
