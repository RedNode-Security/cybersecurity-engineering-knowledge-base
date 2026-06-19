# 03 — Threat Intelligence

## Purpose

Threat intelligence turns observations into decisions. Useful intelligence tells
defenders what matters, why it matters, how confident they should be, and what
action should change.

## Intelligence Cycle

```text
Requirements → Collection → Processing → Analysis → Dissemination → Feedback
```

## Detailed Pages

- [CVE Triage Workflow](CVE-Intelligence/cve-triage-workflow.md)
- [CVE Scoring Worksheet](CVE-Intelligence/cve-scoring-worksheet.md)
- [IOC Management](IOC-Management/README.md)
- [IOC Lifecycle and Scoring](IOC-Management/ioc-lifecycle-and-scoring.md)
- [IOC Examples](IOC-Management/ioc-examples.md)

## Example Priority Intelligence Requirements

- Which currently exploited vulnerabilities affect internet-facing assets?
- Which IOCs are relevant to our identity, endpoint, cloud, or network telemetry?
- Which actor behaviors map to our critical assets?
- Which detections or playbooks should change because of new reporting?
- Which indicators are stale and should be removed from blocking controls?

## Intelligence Quality Standard

Every intelligence note should include:

- Source
- Confidence
- Context
- Relevance to defensive action
- First-seen and last-seen where applicable
- Expiration or review date
- Recommended use: enrichment, hunt, alert, block, or report
- Clear separation between facts, assumptions, and analyst judgment
