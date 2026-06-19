---
title: Kubernetes Detection References
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, kubernetes, index]
difficulty: advanced
safe_publication: true
---


# Kubernetes Detection References

## Purpose

This folder contains platform-neutral reference detections for the `kubernetes`
domain. Each page includes a hypothesis, telemetry contract, sample data, false
positives, triage, response guidance, and test case mapping.

## Detections

- [Kubernetes Admission Denied Spike](admission-denied-spike.md)
- [Kubernetes Cluster Admin Binding Created](cluster-admin-binding-created.md)
- [Kubernetes Exec in Sensitive Namespace](pod-exec-sensitive-namespace.md)
- [Kubernetes HostPath Mount Created](hostpath-mount-created.md)
- [Kubernetes Privileged Pod Created](privileged-pod-created.md)
- [Kubernetes Secret Read by Unusual Service Account](secret-read-unusual-service-account.md)
