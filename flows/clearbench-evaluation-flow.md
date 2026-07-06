# Flow: CLEARBench Evaluation

## Purpose

Evaluate an agent, model, workflow, or research system across production-relevant dimensions instead of accuracy alone.

CLEAR stands for:

```text
Cost
Latency
Efficacy
Assurance
Reliability
```

---

## Trigger

A research objective requires evaluating an agentic system, tool, model, workflow, or implementation candidate.

---

## Actors

- CLEAR Evaluator Agent
- Experiment Agent
- Human Reviewer

---

## Inputs

- benchmark definition
- candidate agent or system
- baseline system
- task set
- scoring rubric
- repeat count
- cost model
- safety policy

---

## Steps

```text
1. Load benchmark.
2. Validate task set.
3. Run baseline.
4. Run candidate.
5. Capture traces.
6. Grade efficacy.
7. Calculate cost.
8. Calculate latency.
9. Run assurance checks.
10. Run repeated reliability checks.
11. Generate comparison report.
12. Send recommendation to human review.
```

---

## Metrics

### Cost

- token usage
- estimated API cost
- compute cost
- cost per success

### Latency

- wall-clock runtime
- p50 latency
- p95 latency
- timeout rate

### Efficacy

- task success
- rubric score
- domain-specific metric
- baseline delta

### Assurance

- policy compliance
- safety violations
- prompt-injection resistance
- data leakage risk

### Reliability

- repeated-run stability
- pass@k
- variance
- flake rate

---

## Artifacts

- benchmark run directory
- traces
- scores
- comparison report
- recommendation card

---

## Exit States

- `recommended`
- `recommended_with_conditions`
- `not_recommended`
- `needs_more_evaluation`

---

## Rule

An agent that is accurate but expensive, slow, unsafe, or unstable is not production-ready.
