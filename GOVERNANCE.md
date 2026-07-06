# Agent-Research Governance

Governance is the boundary that turns agentic research from automation into accountable research infrastructure.

---

## 1. Governance Principle

```text
Autonomy is allowed only inside evidence, policy, and review boundaries.
```

Agents may execute research work, but they do not own truth, accountability, or publication authority.

---

## 2. Required Gates

Every publishable research artifact must pass:

```text
scope gate
  → source gate
  → citation gate
  → evidence gate
  → evaluation gate
  → verification gate
  → human review gate
  → release gate
```

---

## 3. Human Approval Required

Human approval is required for:

- publishing public claims;
- changing benchmark definitions;
- changing success metrics;
- using restricted or sensitive data;
- running high-cost compute;
- deleting research artifacts;
- submitting papers, reports, or releases;
- marking a high-impact claim as verified.

---

## 4. Agent Permissions

Agents may be granted scoped permissions:

| Permission | Meaning |
|---|---|
| `read_sources` | Read approved papers, docs, repositories, and datasets. |
| `write_artifacts` | Create reports, cards, logs, and summaries. |
| `run_experiments` | Execute approved scripts or benchmarks. |
| `verify_citations` | Check source metadata and provenance. |
| `grade_claims` | Recommend claim confidence status. |
| `draft_publication` | Draft publishable material. |
| `publish` | Reserved for human-approved automation only. |

Default posture:

```text
deny by default
allow by objective scope
escalate on uncertainty
record every state change
```

---

## 5. Claim Status Policy

Claims must use one of the following states:

```text
unverified
partially_verified
verified
reproduced
rejected
superseded
stale
```

A claim cannot be published as verified unless its evidence, citation, and verification cards exist.

---

## 6. Citation Policy

A citation must include:

- title;
- authors;
- year;
- venue or publisher;
- DOI, URL, arXiv ID, standard number, or repository URL;
- access date;
- relevance to the claim;
- verification status.

Fabricated or unverifiable citations must be removed or marked `unverified`.

---

## 7. Evaluation Policy

Every evaluation must record:

- baseline;
- metric;
- dataset or task set;
- seed, if applicable;
- environment;
- command;
- version;
- output path;
- known limitations.

Agents must not change metrics or baselines to make results look better.

---

## 8. Audit Log

Every important action should be recorded as an audit event:

```yaml
actor: agent:citation-verifier
action: verify_citation
target: cite-001
time: 2025-01-29T00:00:00Z
result: passed
artifact: citations/cite-001.yaml
```

---

## 9. Recovery and Retirement

Every objective, claim, and release must support graceful recovery or retirement.

```text
recover
  → reopen claim
  → rerun verification
  → update evidence
  → republish corrected state

retire
  → mark stale/superseded
  → preserve history
  → prevent future reuse as current evidence
```
