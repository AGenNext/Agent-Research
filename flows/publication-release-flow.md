# Flow: Publication Release

## Purpose

Convert verified research artifacts into a public or internal release only after governance gates pass.

---

## Trigger

A research report, benchmark, whitepaper, blog, or decision memo is ready for publication review.

---

## Actors

- Publisher Agent
- Claim Auditor Agent
- Human Reviewer
- Governance Approver

---

## Inputs

- candidate report
- evidence pack
- claim cards
- citation cards
- verification cards
- review checklist
- target channel

---

## Steps

```text
1. Freeze candidate artifact.
2. Check all claims have status.
3. Check all citations are verified.
4. Check limitations are present.
5. Check no restricted data is included.
6. Check license and attribution.
7. Generate release notes.
8. Request human approval.
9. Publish to target channel.
10. Create release snapshot.
11. Schedule evidence refresh.
```

---

## Target Channels

- GitHub release
- whitepaper
- technical report
- blog
- documentation
- internal decision memo
- public benchmark report

---

## Gates

```text
claim gate
  → citation gate
  → limitation gate
  → data policy gate
  → license gate
  → human approval gate
  → release gate
```

---

## Exit States

- `published`
- `approved_internal_only`
- `blocked_by_governance`
- `needs_revision`

---

## Rule

Publishing is not formatting. Publishing is the act of making a verified research state accountable.
