# Flow: Claim Verification

## Purpose

Convert evidence into graded claims only after source, experiment, and verification gates are satisfied.

---

## Trigger

A report, experiment, literature review, benchmark, or agent output proposes a claim.

---

## Actors

- Claim Auditor Agent
- Citation Verifier Agent
- Evidence Agent
- Human Reviewer

---

## Inputs

- proposed claim
- evidence cards
- citation cards
- experiment artifacts
- verification method
- confidence threshold

---

## Steps

```text
1. Normalize claim into one precise sentence.
2. Separate observation, inference, and speculation.
3. Link evidence to the claim.
4. Check source quality.
5. Check citation validity.
6. Check experimental reproducibility.
7. Run or inspect verification method.
8. Search for counterevidence.
9. Assign confidence grade.
10. Send high-impact claims to human review.
```

---

## Claim Grades

```text
unverified
partially_verified
verified
reproduced
rejected
```

---

## Artifacts

- claim card
- verification card
- evidence links
- counterevidence notes
- review decision

---

## Gates

```text
precision gate
  → evidence gate
  → citation gate
  → counterevidence gate
  → verification gate
  → human review gate
```

---

## Exit States

- `verified_claim`
- `partially_verified_claim`
- `rejected_claim`
- `needs_more_evidence`

---

## Rule

A claim without evidence is not a claim. It is a hypothesis or speculation.
