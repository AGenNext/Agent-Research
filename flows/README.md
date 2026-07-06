# Agent-Research Flows

Flows are the executable operating patterns of Agent-Research.

Each flow defines:

- trigger;
- actors;
- required inputs;
- ordered steps;
- artifacts produced;
- gates;
- exit states.

---

## Flow Catalog

| Flow | Purpose |
|---|---|
| `research-objective-intake.md` | Convert an idea into a scoped research objective. |
| `literature-evidence-flow.md` | Collect, verify, and freshness-check sources. |
| `experiment-execution-flow.md` | Run controlled experiments with evidence capture. |
| `claim-verification-flow.md` | Convert evidence into graded claims. |
| `clearbench-evaluation-flow.md` | Evaluate agents across Cost, Latency, Efficacy, Assurance, Reliability. |
| `publication-release-flow.md` | Publish only after evidence, verification, and human review. |
| `evidence-refresh-flow.md` | Re-check stale evidence and reopen claims when needed. |

---

## Canonical End-to-End Flow

```text
idea
  → objective intake
  → research plan
  → literature evidence
  → experiment execution
  → claim verification
  → CLEAR evaluation
  → human review
  → publication release
  → evidence refresh watch
```

---

## Flow Invariants

```text
No claim without evidence.
No evidence without source.
No source without provenance.
No evaluation without reproducible artifact.
No publication without human review.
```
