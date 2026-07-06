# Flow: Research Objective Intake

## Purpose

Convert a raw idea into a scoped, reviewable research objective.

---

## Trigger

A human submits an idea, question, problem, repo, paper, market concern, or benchmark target.

---

## Actors

- Human principal investigator
- Research Concierge Agent
- Governance Reviewer

---

## Inputs

- raw idea or question
- domain
- intended use
- constraints
- expected output
- risk level
- due date, if any

---

## Steps

```text
1. Capture raw idea.
2. Identify domain and intended decision.
3. Ask clarifying questions only when required.
4. Convert idea into objective.
5. Define success criteria.
6. Define evidence requirements.
7. Define forbidden actions and safety limits.
8. Create initial research plan.
9. Open human approval gate.
10. Move objective to planned or rejected.
```

---

## Artifacts

- `RESEARCH_PLAN.md`
- objective card
- risk card
- approval record

---

## Gates

```text
scope gate
  → risk gate
  → human approval gate
```

---

## Exit States

- `planned`
- `needs_clarification`
- `rejected`
- `suspended`

---

## Minimum Objective Card

```yaml
id: obj-001
title: "Evaluate governed agentic research workflows"
owner: human
domain: agentic-research
status: planned
success_criteria:
  - evidence pack produced
  - citations verified
  - claims graded
  - human review complete
risk_level: medium
```
