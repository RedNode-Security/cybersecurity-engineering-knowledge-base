# Reference-Grade Content Standard

## Definition

A reference-grade page is accurate, useful, safe, maintainable, and specific. It
should help a reader understand the topic and make a better security decision.

## Required Sections by Content Type

### Detection Page

- Detection hypothesis
- Required telemetry
- Logic or pseudocode
- False positives
- Triage steps
- Response actions
- Test plan
- References

### CVE Page

- Executive summary
- Affected products and versions
- Impact
- Exposure conditions
- Mitigation and patch guidance
- Detection opportunities
- Safe validation
- References

### Playbook

- Objective
- Scope
- Trigger conditions
- Severity criteria
- Evidence collection
- Triage steps
- Containment
- Recovery
- Lessons learned

### Architecture Page

- Context
- Components
- Data flow
- Trust boundaries
- Failure modes
- Operational ownership
- Metrics
- References

## Reference-Grade Checklist

- [ ] The page has a specific audience.
- [ ] The page states what is in scope and out of scope.
- [ ] Examples are safe and useful.
- [ ] Operational steps are realistic.
- [ ] References support factual claims.
- [ ] False positives or limitations are included.
- [ ] Automation guidance includes safety controls.
- [ ] The page has a review date or maintenance expectation.

## Page Scoring

| Score | Meaning |
|---|---|
| 1 | Stub or placeholder |
| 2 | Useful draft but lacks examples or references |
| 3 | Good practitioner note |
| 4 | Review-ready reference page |
| 5 | Published reference-grade page |

A page should not be marked `published` until it scores 5.
