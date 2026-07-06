# Flow: Evidence Refresh

## Purpose

Keep research decisions fresh by re-checking sources, claims, benchmarks, and assumptions over time.

---

## Trigger

- scheduled refresh date arrives;
- source is updated;
- benchmark changes;
- model/tool version changes;
- human requests revalidation;
- claim is challenged.

---

## Actors

- Evidence Agent
- Citation Verifier Agent
- Claim Auditor Agent
- Human Reviewer

---

## Inputs

- release snapshot
- source index
- claim registry
- freshness policy
- benchmark version

---

## Steps

```text
1. Load source index.
2. Check source availability.
3. Check source freshness.
4. Identify changed evidence.
5. Identify impacted claims.
6. Re-run required verification.
7. Re-score confidence.
8. Mark stale or invalid claims.
9. Notify human reviewer.
10. Create refresh report.
```

---

## Artifacts

- refresh report
- stale source list
- impacted claim list
- updated citation cards
- updated claim cards

---

## Gates

```text
freshness gate
  → impact gate
  → verification gate
  → human notification gate
```

---

## Exit States

- `still_current`
- `updated`
- `claim_reopened`
- `claim_rejected`
- `human_review_required`

---

## Rule

A research result is not permanent. It is current only until evidence changes.
