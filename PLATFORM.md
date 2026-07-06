# Agent-Research Platform

Agent-Research is the governed research operating layer for AGenNext. It turns research work into a platform of actors, relationships, actions, time, evidence, claims, reviews, and reproducible artifacts.

The platform keeps the human as principal investigator while giving agents bounded autonomy to search, plan, implement, evaluate, record, verify, and publish.

---

## 1. Platform Intent

The platform exists to answer one operational question:

> Can an organization use AI agents to accelerate research without losing provenance, reproducibility, accountability, or human judgment?

Agent-Research answers this by providing:

- a research control plane;
- governed research workspaces;
- research-native primitives;
- executable flows;
- evidence and claim tracking;
- CLEAR-style evaluation;
- human review gates;
- publication and refresh paths.

---

## 2. Design Doctrine

Agent-Research follows the AGenNext platform doctrine:

```text
Reality first. Models second.
```

The platform begins with real research activity:

- who is acting;
- what question is being pursued;
- what action happened;
- what evidence was produced;
- what claim was made;
- when it happened;
- who reviewed it;
- what changed afterward.

From that reality, the graph, events, agents, policies, reports, dashboards, and automations emerge.

---

## 3. Core Platform Layers

```text
Human Layer
  → principal investigator, reviewers, domain experts

Agent Layer
  → research associate agents, auditor agents, evaluator agents

Control Plane
  → workspaces, objectives, policies, approvals, lifecycle

Evidence Plane
  → sources, files, datasets, logs, traces, reports, artifacts

Evaluation Plane
  → CLEAR metrics, benchmarks, graders, reproducibility checks

Governance Plane
  → policy, permissions, citations, safety, audit, approval gates

Publication Plane
  → whitepapers, blogs, reports, releases, verified claim registry
```

---

## 4. Actor Model

Agent-Research separates real humans from AI agents.

### Humans

Humans own intent, accountability, interpretation, and final approval.

Human roles:

- principal investigator;
- reviewer;
- domain expert;
- governance approver;
- publisher.

### Agents

Agents execute bounded research actions.

Agent roles:

- research associate;
- literature scout;
- experiment runner;
- citation verifier;
- claim auditor;
- CLEAR evaluator;
- publication drafter.

### Organizations

Organizations define policy boundaries, evidence requirements, compliance needs, and publishing rules.

---

## 5. Platform Primitives

| Primitive | Meaning |
|---|---|
| `Workspace` | A bounded research environment. |
| `Objective` | A research goal or investigation. |
| `Question` | A scoped research question. |
| `Hypothesis` | A testable belief. |
| `Experiment` | A controlled research action. |
| `Evidence` | A source-backed observation or artifact. |
| `Claim` | A conclusion derived from evidence. |
| `Citation` | A verified source reference. |
| `Verification` | A method used to test a claim. |
| `Review` | A human or agent audit decision. |
| `Release` | A frozen publishable research snapshot. |
| `Refresh` | A scheduled or event-driven evidence update. |

---

## 6. Default Agent Topology

The default topology is one human-facing research concierge that orchestrates specialist agents underneath.

```text
Human PI
  → Research Concierge Agent
      → Literature Agent
      → Experiment Agent
      → Evidence Agent
      → Citation Agent
      → Claim Auditor Agent
      → CLEAR Evaluator Agent
      → Publisher Agent
```

This avoids forcing the user to manage many agents directly. Multi-agent direct interaction remains an advanced mode.

---

## 7. Platform States

A research objective moves through a governed lifecycle.

```text
proposed
  → scoped
  → planned
  → approved
  → executing
  → recording
  → verifying
  → human_review
  → release_candidate
  → published
  → refresh_watch
  → archived
```

Rejected, suspended, and retired states are allowed at every gate.

---

## 8. Deployment Shape

The platform is portable by design.

Baseline deployment:

```text
Kubernetes / K3s
  → Control Plane API
  → Workspace Runner
  → Agent Runtime
  → Event Bus
  → SurrealDB State
  → Object Storage Artifacts
  → Policy Engine
  → Evaluation Worker
  → Static Docs / UI
```

Preferred AGenNext infrastructure mapping:

- **Control Plane:** Kubernetes or K3s
- **Workflow:** Temporal-compatible flow model
- **Events:** CloudEvents-compatible events
- **Service Layer:** Dapr-compatible service calls
- **Policy:** OPA / OpenFGA-style controls
- **State:** SurrealDB
- **Evidence:** Git + object storage
- **Observability:** traces, run logs, evaluation reports

---

## 9. Platform APIs

Minimum platform API groups:

```text
/workspaces
/objectives
/questions
/hypotheses
/experiments
/evidence
/claims
/citations
/verifications
/reviews
/releases
/flows
/evaluations
```

Each API must preserve actor, action, timestamp, provenance, policy result, and artifact references.

---

## 10. Non-Negotiable Gates

No research claim should become canonical unless these gates pass:

```text
source gate
  → citation gate
  → evidence gate
  → evaluation gate
  → verification gate
  → human review gate
  → release gate
```

---

## 11. Platform Output

The platform produces:

- research reports;
- evidence packs;
- CLEAR evaluation reports;
- claim cards;
- citation cards;
- verification cards;
- publication-ready whitepapers;
- GitHub releases;
- refresh alerts when evidence changes.
