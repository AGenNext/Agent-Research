# Flow: Experiment Execution

## Purpose

Run controlled research experiments with reproducible inputs, explicit metrics, durable logs, and preserved failures.

---

## Trigger

A planned hypothesis requires empirical, computational, software, product, or benchmark testing.

---

## Actors

- Experiment Agent
- Evidence Agent
- CLEAR Evaluator Agent
- Human Reviewer

---

## Inputs

- approved research plan
- hypothesis
- baseline
- metric definition
- dataset or fixture
- environment specification
- compute budget
- safety limits

---

## Steps

```text
1. Confirm hypothesis and metric.
2. Confirm baseline and fixed variables.
3. Create experiment card.
4. Prepare environment.
5. Run Tier 1 smoke test.
6. Run Tier 2 small-signal test.
7. Run Tier 3 full evaluation when justified.
8. Capture logs, outputs, configs, and failures.
9. Analyze result against baseline.
10. Update report and TODO.
11. Commit experiment artifacts.
12. Send to verification or mark as failed.
```

---

## Evaluation Tiers

```text
Tier 1: seconds/minutes, checks that it runs.
Tier 2: small subset, checks signal and obvious failure.
Tier 3: full benchmark, supports claims.
```

---

## Artifacts

- experiment card
- run command
- environment file
- logs
- output data
- plots
- failure notes
- result summary
- git commit

---

## Gates

```text
baseline gate
  → one-variable gate
  → smoke-test gate
  → full-evaluation gate
  → artifact-completeness gate
```

---

## Exit States

- `verified_result_candidate`
- `failed_with_artifacts`
- `needs_rerun`
- `blocked`

---

## Rule

A failed experiment is still a successful platform event if it is recorded, reproducible, and useful for the next decision.
