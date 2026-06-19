# Source and Citation Policy

## Purpose

Reference-grade content needs sources. Sources make the repository trustworthy
and make future maintenance possible.

## Preferred Sources

Use primary sources whenever possible:

- Vendor advisories
- Official product documentation
- Standards bodies
- NIST, CISA, FIRST, OWASP, MITRE, CIS
- Project security advisories
- Reputable security research with clear evidence

## Source Quality

| Source type | Confidence | Use |
|---|---|---|
| Vendor advisory | High | Affected versions, fixes, mitigations |
| Official standard | High | Definitions and control guidance |
| NVD/CVE record | Medium/high | CVE metadata and severity |
| CISA KEV | High | Known exploited status |
| Reputable research | Medium/high | Detection and exploitation context |
| Social media | Low | Lead only; verify elsewhere |
| Unattributed blog | Low | Avoid for core claims |

## Citation Rules

- Put references at the end of each page.
- Prefer stable official URLs.
- Do not cite exploit repositories for public guidance unless there is a clear defensive reason.
- If a claim is likely to change, say when it was reviewed.
- For CVEs, include vendor advisory and NVD or CVE record where available.

## Claim Types That Need References

- Affected versions
- Fixed versions
- CVSS or severity scores
- Known exploitation status
- Security standard requirements
- Vendor-specific log fields or event IDs
- Product behavior that could change

## Claim Types That May Not Need References

- Internal methodology
- Synthetic examples
- General triage questions
- Repository-specific workflow decisions

## Handling Uncertainty

Use clear language:

```text
Public reporting indicates exploitation, but this note does not independently verify campaign attribution.
```

Avoid unsupported language:

```text
This actor definitely performed the attack.
```
