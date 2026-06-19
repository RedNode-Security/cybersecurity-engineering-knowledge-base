---
title: Detection Reference Coverage
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, coverage, reference-library]
difficulty: advanced
safe_publication: true
---


# Detection Reference Coverage

## Summary

Total reference detections: **66**

## Coverage By Domain

| Domain | Count |
|---|---|
| ai | 6 |
| application | 6 |
| cloud | 12 |
| identity | 12 |
| kubernetes | 6 |
| linux | 6 |
| network | 6 |
| windows | 12 |

## Coverage By Severity

| Severity | Count |
|---|---|
| critical | 7 |
| high | 42 |
| medium | 17 |

## Coverage By Data Source

| Data source | Count |
|---|---|
| `admin_audit_logs` | 3 |
| `admission_controller_logs` | 1 |
| `ai_agent_audit_logs` | 2 |
| `application_audit_logs` | 7 |
| `asset_inventory` | 1 |
| `aws_cloudtrail` | 8 |
| `azure_audit_logs` | 4 |
| `change_records` | 1 |
| `cloud_asset_inventory` | 1 |
| `device_inventory` | 1 |
| `directory_audit_logs` | 2 |
| `directory_inventory` | 1 |
| `dns_logs` | 4 |
| `edr_file_events` | 5 |
| `edr_process_events` | 8 |
| `identity_audit_logs` | 2 |
| `identity_inventory` | 1 |
| `identity_signin_logs` | 9 |
| `identity_token_logs` | 1 |
| `kubernetes_audit_logs` | 6 |
| `linux_audit_logs` | 5 |
| `linux_auth_logs` | 2 |
| `llm_audit_logs` | 3 |
| `mfa_logs` | 1 |
| `network_flow_logs` | 3 |
| `proxy_logs` | 5 |
| `rag_audit_logs` | 1 |
| `windows_security_events` | 4 |
| `windows_system_events` | 2 |
| `windows_task_scheduler` | 1 |

## Detection Inventory

| Domain | ID | Detection | Data sources | Severity | Confidence |
|---|---|---|---|---|---|
| ai | `DET-AI-AGENT_REPEATED_TOOL_FAILURE` | AI Agent Repeated Tool Failure | ai_agent_audit_logs | medium | medium |
| ai | `DET-AI-HIDDEN_PROMPT_EXTRACTION_ATTEMPT` | Hidden Prompt Extraction Attempt | llm_audit_logs | medium | medium |
| ai | `DET-AI-LLM_TOOL_CALL_WITHOUT_APPROVAL` | LLM Tool Call Without Required Approval | ai_agent_audit_logs | high | medium |
| ai | `DET-AI-PROMPT_INJECTION_ATTEMPTS` | Prompt Injection Attempt Pattern | llm_audit_logs | medium | medium |
| ai | `DET-AI-RAG_SENSITIVE_COLLECTION_ACCESS` | RAG Sensitive Collection Access | rag_audit_logs | medium | medium |
| ai | `DET-AI-SENSITIVE_OUTPUT_REDACTION_SPIKE` | Sensitive Output Redaction Spike | llm_audit_logs | high | medium |
| application | `DET-APPLICATION-API_ADMIN_ACTION_NEW_SOURCE` | API Admin Action from New Source | application_audit_logs | high | medium |
| application | `DET-APPLICATION-API_CROSS_TENANT_DENIALS` | API Cross-Tenant Authorization Denials | application_audit_logs | high | medium |
| application | `DET-APPLICATION-API_REPEATED_AUTHZ_FAILURES` | Repeated API Authorization Failures | application_audit_logs | medium | medium |
| application | `DET-APPLICATION-API_SENSITIVE_EXPORT_SPIKE` | API Sensitive Data Export Spike | application_audit_logs | high | medium |
| application | `DET-APPLICATION-GRAPHQL_HIGH_COMPLEXITY_QUERY` | GraphQL High Complexity Query | application_audit_logs | medium | medium |
| application | `DET-APPLICATION-WEBHOOK_SECRET_ROTATION_FAILURE` | Webhook Secret Rotation Failure | application_audit_logs | medium | medium |
| cloud | `DET-CLOUD-AWS_ADMIN_POLICY_ATTACHMENT` | AWS Administrator Policy Attachment | aws_cloudtrail | high | medium |
| cloud | `DET-CLOUD-AWS_CLOUDTRAIL_TAMPERING` | AWS CloudTrail Logging Tampering | aws_cloudtrail | critical | high |
| cloud | `DET-CLOUD-AWS_GUARDDUTY_DISABLED` | AWS GuardDuty Disabled | aws_cloudtrail | critical | high |
| cloud | `DET-CLOUD-AWS_KMS_KEY_POLICY_CHANGED` | AWS KMS Key Policy Changed | aws_cloudtrail | high | medium |
| cloud | `DET-CLOUD-AWS_PUBLIC_SECURITY_GROUP_ADMIN_PORT` | AWS Security Group Admin Port Opened Publicly | aws_cloudtrail, cloud_asset_inventory | high | medium |
| cloud | `DET-CLOUD-AWS_RARE_ACCESS_KEY_CREATED` | AWS Access Key Created for Rare User | aws_cloudtrail, identity_inventory | high | medium |
| cloud | `DET-CLOUD-AWS_ROOT_ACCOUNT_USE` | AWS Root Account Use | aws_cloudtrail | critical | high |
| cloud | `DET-CLOUD-AWS_S3_PUBLIC_ACCESS_BLOCK_DISABLED` | AWS S3 Public Access Block Disabled | aws_cloudtrail | high | medium |
| cloud | `DET-CLOUD-AZURE_CONDITIONAL_ACCESS_DISABLED` | Azure Conditional Access Policy Disabled | azure_audit_logs | critical | high |
| cloud | `DET-CLOUD-AZURE_HIGH_RISK_APP_CONSENT` | Azure High-Risk App Consent | azure_audit_logs | high | medium |
| cloud | `DET-CLOUD-AZURE_PRIVILEGED_ROLE_ASSIGNMENT` | Azure Privileged Role Assignment | azure_audit_logs | high | medium |
| cloud | `DET-CLOUD-AZURE_SERVICE_PRINCIPAL_CREDENTIAL_ADDED` | Azure Service Principal Credential Added | azure_audit_logs | high | medium |
| identity | `DET-IDENTITY-BREAK_GLASS_ACCOUNT_USED` | Break-Glass Account Used | identity_signin_logs, admin_audit_logs | critical | high |
| identity | `DET-IDENTITY-DISABLED_ACCOUNT_SUCCESSFUL_LOGIN` | Disabled Account Successful Login | identity_signin_logs, directory_audit_logs | critical | high |
| identity | `DET-IDENTITY-IMPOSSIBLE_TRAVEL_SENSITIVE_APP` | Impossible Travel to Sensitive App | identity_signin_logs | high | medium |
| identity | `DET-IDENTITY-MFA_METHOD_CHANGE_FOLLOWED_BY_LOGIN` | MFA Method Change Followed by New Login | identity_audit_logs, identity_signin_logs | high | medium |
| identity | `DET-IDENTITY-MULTIPLE_MFA_PROMPTS_USER` | Multiple MFA Prompts for User | mfa_logs | medium | medium |
| identity | `DET-IDENTITY-NEW_DEVICE_SENSITIVE_ACCESS` | New Device Sensitive Access | identity_signin_logs, device_inventory | high | medium |
| identity | `DET-IDENTITY-PASSWORD_SPRAY_FOLLOWED_BY_SUCCESS` | Password Spray Followed by Success | identity_signin_logs | high | medium |
| identity | `DET-IDENTITY-PRIVILEGED_ROLE_ASSIGNMENT_NO_CHANGE` | Privileged Role Assignment Without Change Context | admin_audit_logs, change_records | high | medium |
| identity | `DET-IDENTITY-RISKY_SIGNIN_PRIVILEGED_ACTION` | Risky Sign-in Followed by Privileged Action | identity_signin_logs, admin_audit_logs | high | medium |
| identity | `DET-IDENTITY-SERVICE_ACCOUNT_INTERACTIVE_LOGIN` | Service Account Interactive Login | identity_signin_logs, directory_inventory | high | medium |
| identity | `DET-IDENTITY-SUSPICIOUS_OAUTH_CONSENT` | Suspicious OAuth Consent | identity_audit_logs, application_audit_logs | high | medium |
| identity | `DET-IDENTITY-TOKEN_REFRESH_AFTER_USER_DISABLED` | Token Refresh After User Disabled | identity_token_logs, directory_audit_logs | high | medium |
| kubernetes | `DET-KUBERNETES-ADMISSION_DENIED_SPIKE` | Kubernetes Admission Denied Spike | kubernetes_audit_logs, admission_controller_logs | medium | medium |
| kubernetes | `DET-KUBERNETES-CLUSTER_ADMIN_BINDING_CREATED` | Kubernetes Cluster Admin Binding Created | kubernetes_audit_logs | high | medium |
| kubernetes | `DET-KUBERNETES-HOSTPATH_MOUNT_CREATED` | Kubernetes HostPath Mount Created | kubernetes_audit_logs | high | medium |
| kubernetes | `DET-KUBERNETES-POD_EXEC_SENSITIVE_NAMESPACE` | Kubernetes Exec in Sensitive Namespace | kubernetes_audit_logs | medium | medium |
| kubernetes | `DET-KUBERNETES-PRIVILEGED_POD_CREATED` | Kubernetes Privileged Pod Created | kubernetes_audit_logs | high | medium |
| kubernetes | `DET-KUBERNETES-SECRET_READ_UNUSUAL_SERVICE_ACCOUNT` | Kubernetes Secret Read by Unusual Service Account | kubernetes_audit_logs | high | medium |
| linux | `DET-LINUX-AUTHORIZED_KEYS_MODIFIED` | Authorized Keys Modified | linux_audit_logs, edr_file_events | high | medium |
| linux | `DET-LINUX-CRON_ENTRY_MODIFIED` | Cron Entry Modified by Unusual User | linux_audit_logs, edr_file_events | medium | medium |
| linux | `DET-LINUX-NEW_SUDO_USER_CREATED` | New Sudo-Capable User Created | linux_auth_logs, linux_audit_logs | high | medium |
| linux | `DET-LINUX-NEW_SYSTEMD_SERVICE_CREATED` | New Systemd Service Created | linux_audit_logs, edr_file_events | high | medium |
| linux | `DET-LINUX-SSH_FAILURES_FOLLOWED_BY_SUCCESS` | SSH Failures Followed by Success | linux_auth_logs | high | medium |
| linux | `DET-LINUX-SUDOERS_FILE_MODIFIED` | Sudoers File Modified | linux_audit_logs, edr_file_events | high | medium |
| network | `DET-NETWORK-ANONYMIZING_NETWORK_FROM_SERVER` | Anonymizing Network Access From Server | proxy_logs, network_flow_logs | medium | medium |
| network | `DET-NETWORK-BEACONING_REGULAR_INTERVAL` | Regular Interval Beaconing | proxy_logs, dns_logs, network_flow_logs | medium | medium |
| network | `DET-NETWORK-DNS_HIGH_ENTROPY_SUBDOMAINS` | High Entropy DNS Subdomains | dns_logs | medium | low |
| network | `DET-NETWORK-LARGE_UPLOAD_RARE_DESTINATION` | Large Upload to Rare Destination | proxy_logs, network_flow_logs | high | medium |
| network | `DET-NETWORK-NEWLY_OBSERVED_DOMAIN_SENSITIVE_HOST` | Newly Observed Domain From Sensitive Host | dns_logs, asset_inventory | medium | medium |
| network | `DET-NETWORK-PROXY_EXECUTABLE_DOWNLOAD_RARE_DOMAIN` | Executable Download From Rare Domain | proxy_logs, dns_logs | high | medium |
| windows | `DET-WINDOWS-ARCHIVE_CREATED_BEFORE_UPLOAD` | Archive Created Before Large Upload | edr_file_events, proxy_logs | high | medium |
| windows | `DET-WINDOWS-EXPLICIT_CREDENTIALS_RARE_HOST` | Explicit Credentials Used on Rare Host | windows_security_events | medium | medium |
| windows | `DET-WINDOWS-LSASS_ACCESS_UNUSUAL_PROCESS` | LSASS Access by Unusual Process | edr_process_events | critical | medium |
| windows | `DET-WINDOWS-NEW_LOCAL_ADMIN_ADDED` | New Local Administrator Added | windows_security_events | high | medium |
| windows | `DET-WINDOWS-NEW_SERVICE_SENSITIVE_HOST` | New Service on Sensitive Host | windows_system_events, edr_process_events | high | medium |
| windows | `DET-WINDOWS-OFFICE_SPAWNS_SCRIPT_INTERPRETER` | Office Spawns Script Interpreter | edr_process_events | high | medium |
| windows | `DET-WINDOWS-POWERSHELL_AFTER_RISKY_LOGON` | PowerShell After Risky Logon | identity_signin_logs, edr_process_events | high | medium |
| windows | `DET-WINDOWS-POWERSHELL_ENCODED_COMMAND_NETWORK` | PowerShell Encoded Command With Network | edr_process_events | high | medium |
| windows | `DET-WINDOWS-PRIVILEGED_GROUP_MEMBERSHIP_CHANGE` | Privileged Group Membership Change | windows_security_events | high | high |
| windows | `DET-WINDOWS-SCHEDULED_TASK_UNUSUAL_USER` | Scheduled Task Created by Unusual User | windows_task_scheduler, edr_process_events | medium | medium |
| windows | `DET-WINDOWS-SECURITY_TOOL_SERVICE_STOPPED` | Security Tool Service Stopped | windows_system_events, edr_process_events | high | medium |
| windows | `DET-WINDOWS-WMI_PROCESS_CREATION_REMOTE` | Remote WMI Process Creation | edr_process_events, windows_security_events | high | medium |

## Interpretation

This library now covers identity, endpoint, Linux, network, cloud, Kubernetes,
application, and AI security telemetry. It is broad enough to function as a real
reference library, but each detection still needs local SIEM mapping before
production use.
