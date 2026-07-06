# Flow: Literature Evidence

## Purpose

Collect, verify, grade, and preserve source-backed evidence before it is used in research decisions or claims.

---

## Trigger

A research objective requires background, prior art, market evidence, technical evidence, or policy evidence.

---

## Actors

- Literature Agent
- Evidence Agent
- Citation Verifier Agent
- Human Reviewer

---

## Inputs

- research objective
- search scope
- accepted source types
- freshness requirement
- exclusion criteria

---

## Steps

```text
1. Generate search plan.
2. Search primary sources first.
3. Collect candidate sources.
4. Remove duplicates and weak sources.
5. Verify bibliographic metadata.
6. Extract relevant evidence.
7. Assign evidence quality grade.
8. Attach source provenance.
9. Mark freshness and review date.
10. Store evidence pack.
```

---

## Source Priority

```text
primary paper / standard / official docs
  → reputable institutional report
  → peer-reviewed survey
  → implementation repository
  → high-quality technical blog
  → community discussion only as weak signal
```

---

## Artifacts

- citation cards
- evidence cards
- source index
- freshness log
- prior-art map

---

## Gates

```text
source quality gate
  → citation verification gate
  → relevance gate
  → freshness gate
```

---

## Exit States

- `evidence_ready`
- `insufficient_evidence`
- `needs_human_review`
- `stale_source`

---

## Evidence Quality Grades

```text
A = primary, current, directly relevant
B = reputable secondary source, relevant
C = useful context but indirect
D = weak signal only
F = unusable or unverifiable
```
