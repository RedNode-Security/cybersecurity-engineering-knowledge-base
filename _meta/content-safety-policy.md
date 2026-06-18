# Content Safety Policy

This repository is public-facing and should remain safe, legal, and professionally useful.

## Allowed

- Defensive analysis
- Security architecture guidance
- Sanitized indicators of compromise
- CVE summaries focused on risk, patching, mitigation, and detection
- High-level adversary methodology for authorized testing
- Lab-only educational examples that cannot be directly used against third-party systems
- Detection logic, triage workflows, and response playbooks

## Not Allowed

- Real secrets or private data
- Malware binaries
- Destructive payloads
- Working exploit chains for active real-world abuse
- Instructions to bypass detection, hide persistence, or evade security tools
- Target-specific operational details for systems you do not own or have permission to test
- Claims of attribution without evidence and confidence level

## CVE Publication Guidance

For CVE notes, include:

- Affected products and versions
- Impact
- Exposure conditions
- Patch/mitigation guidance
- Detection opportunities
- Safe validation notes
- References

Avoid:

- Weaponized exploit code
- Mass-scanning instructions
- Target lists
- Operational payloads

## IOC Publication Guidance

For IOCs, include:

- Source
- First seen / last seen
- Type
- Confidence
- Context
- Expiration or review date

Avoid:

- Private environment data
- Sensitive internal hostnames
- Unverified indicators without labeling confidence
