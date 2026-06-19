---
title: Kubernetes Threat Model and Detections
domain: cloud-security
category: kubernetes-security
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [kubernetes, cloud, detection, threat-modeling]
difficulty: advanced
safe_publication: true
---


# Kubernetes Threat Model and Detections

## Overview

Kubernetes security requires visibility into identity, API server actions,
workloads, admission control, secrets, network policy, and container runtime
behavior.

## Assets

| Asset | Why it matters |
|---|---|
| API server | Control plane for cluster changes |
| Service accounts | Workload identity and permissions |
| Secrets | Credentials and sensitive configuration |
| Nodes | Runtime environment for workloads |
| Images | Software supply chain input |
| Admission policies | Prevent unsafe deployments |

## Key Logs

- API server audit logs
- Cloud provider audit logs
- Container runtime logs
- Admission controller logs
- Network flow logs
- Image scanner findings

## Detection Ideas

| Behavior | Signal |
|---|---|
| Secret read by unusual identity | API audit `get secrets` |
| Privileged pod creation | pod spec privileged or hostPath |
| New cluster-admin binding | RBAC role binding change |
| Exec into sensitive pod | API audit `pods/exec` |
| Suspicious image deployment | image from untrusted registry |
| Admission policy bypass attempt | denied admission events |

## Example Audit Event Questions

```text
verb: create
resource: rolebindings
namespace: kube-system
actor: system:serviceaccount:example:builder
```

Ask:

- Should this service account modify RBAC?
- Is the namespace sensitive?
- Was this part of deployment automation?
- Did the role grant cluster-wide access?

## Hardening Checklist

- [ ] API audit logging enabled.
- [ ] RBAC is least privilege.
- [ ] Secrets access is restricted.
- [ ] Privileged containers are denied by policy.
- [ ] Admission control is enforced.
- [ ] Images are scanned and provenance is reviewed.
- [ ] Network policies restrict sensitive namespaces.

## References

- Kubernetes audit logging: https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/
- Kubernetes RBAC: https://kubernetes.io/docs/reference/access-authn-authz/rbac/
