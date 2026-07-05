# AGenNext Agent-Research

## Governed Agentic Research Infrastructure

**Version:** 0.1  
**Status:** Canonical draft  
**Repository:** `AGenNext/Agent-Research`  
**Author:** Chinmay Panda / AGenNext

---

## Abstract

Agentic AI is emerging as a new class of autonomous intelligence: systems that can pursue complex goals, adapt to dynamic environments, use tools, make decisions, and operate over long horizons with reduced human supervision. The IEEE Access survey *Agentic AI: Autonomous Intelligence for Complex Goals—A Comprehensive Survey* frames agentic AI around autonomy, goal complexity, adaptability, environmental responsiveness, learning paradigms, governance, and ethical deployment.

AGenNext Agent-Research extends that foundation into a concrete operating model for research and development. It treats the agent not as an oracle or independent author, but as a governed research associate working under human direction. The human researcher remains the principal investigator; the agent executes bounded research loops, preserves evidence, verifies claims, and escalates uncertainty.

This whitepaper proposes an open framework for human-directed, agent-assisted research. It defines the research loop, governance model, primitives, repository structure, evaluation metrics, safety controls, and roadmap required to make agentic research reproducible, auditable, and trustworthy.

---

## 1. Why Agent-Research Exists

Most AI systems are optimized for answers. Research is optimized for disciplined truth-seeking under uncertainty.

A researcher does not merely ask for a response. A researcher must ask a question, form a hypothesis, design an experiment, evaluate a method, record failure, verify evidence, compare prior work, and decide what deserves to become knowledge.

Agentic AI changes the scale of research execution. A capable agent can inspect a codebase, read papers, write scripts, run experiments, generate plots, maintain reports, check citations, and continue across long sessions. But without governance, the same agent can drift, fabricate references, alter evaluation criteria, overclaim from weak evidence, or silently forget failures.

The principle of AGenNext Agent-Research is therefore simple:

> Agentic research does not remove research discipline. It makes research discipline mandatory.

---

## 2. Definition: Agentic AI for Research

For AGenNext, an agentic research system is an autonomous or semi-autonomous AI system that can:

1. understand a research goal;
2. decompose it into sub-goals;
3. plan and execute experiments;
4. use tools, files, APIs, and compute environments;
5. adapt to new evidence;
6. document its actions;
7. preserve failures;
8. verify claims before presenting them as conclusions;
9. operate under human-defined constraints;
10. escalate decisions that require human judgment.

This aligns with the broader Agentic AI literature, which distinguishes agentic systems from traditional AI by their autonomy, adaptability, goal-directed behavior, decision-making capability, and operation in dynamic environments.

---

## 3. From Agentic AI to Agentic Research

Agentic AI is broader than research. It applies to healthcare, finance, manufacturing, education, cyber-physical systems, disaster management, and customer support. However, research is a special domain because the cost of error is epistemic: a false claim can mislead future work.

Agentic research therefore requires stronger controls than ordinary automation.

The agent must not only complete a task. It must preserve the path by which the task was completed.

The output of Agent-Research is not just a document. It is a connected trail of:

- research questions;
- hypotheses;
- experiments;
- logs;
- datasets;
- code changes;
- citations;
- verification scripts;
- claims;
- human review decisions;
- publication artifacts.

---

## 4. The Human Role

AGenNext Agent-Research is human-directed.

The human researcher remains responsible for:

- choosing the research direction;
- defining success criteria;
- approving risky actions;
- judging novelty;
- interpreting significance;
- approving publication;
- accepting ethical accountability.

The agent may act as assistant, collaborator, associate, or auditor, but it does not replace the principal investigator.

---

## 5. The Agentic Research Loop

The core loop is:

> **Explore → Plan → Implement → Evaluate → Analyze → Record → Commit → Iterate**

### 5.1 Explore

The agent studies the available context: papers, code, notes, issues, datasets, previous experiments, constraints, and evaluation metrics.

### 5.2 Plan

The agent proposes a research plan with scope, baseline, metric, hypothesis, expected risks, and verification strategy.

### 5.3 Implement

The agent writes code, scripts, tests, notebooks, prompts, data transforms, or proof attempts.

### 5.4 Evaluate

The agent evaluates in tiers: smoke tests, small-scale tests, full benchmarks, ablations, and edge-case checks.

### 5.5 Analyze

The agent separates observation from inference and speculation. It must classify every claim by confidence.

### 5.6 Record

The agent updates durable artifacts such as `REPORT.md`, `TODO.md`, experiment logs, claim cards, citation cards, and verification files.

### 5.7 Commit

Every meaningful experiment is committed with structured metadata.

Example:

```text
exp(E012): test retrieval reranking baseline -- recall@10=0.72
```

### 5.8 Iterate

The next step is selected based on evidence, not impulse. If the research direction changes, the agent asks for human approval.

---

## 6. Commandments for Research Agents

These commandments turn general autonomy into disciplined research behavior.

### Integrity

1. **Never break a promise.** If the agent says it will do something, it must do it or explicitly record why it did not.
2. **Never manipulate evaluation.** Metrics, baselines, datasets, seeds, and problem definitions must not be changed to improve appearances.
3. **Never fabricate citations.** Every reference must be verified before being used as evidence.

### Autonomy

4. **Complete autonomous work before reporting.** Do not stop early when approved work remains possible.
5. **Make it work before moving on.** A crash is a bug until proven otherwise.

### Scientific Rigor

6. **Change one variable per experiment.** Otherwise attribution becomes impossible.
7. **Evaluate in tiers.** Small tests catch bugs; full evaluations support claims.
8. **Bound expectations.** Estimate theoretical or practical ceilings before claiming improvement.

### Reproducibility

9. **Record everything.** Failures, abandoned paths, negative results, and unresolved questions are part of research.
10. **Verify before claiming.** Claims must be marked as unverified, partially verified, verified, reproduced, or rejected.

---

## 7. Core Primitives

Agent-Research defines research-native primitives.

### 7.1 Research Question

A bounded investigation.

```json
{
  "id": "rq-001",
  "title": "Can governed agentic workflows improve reproducibility?",
  "domain": "agentic research",
  "status": "active",
  "owner": "human"
}
```

### 7.2 Hypothesis

A testable belief.

```json
{
  "id": "hyp-001",
  "research_question_id": "rq-001",
  "statement": "Structured research loops reduce unrecorded agent failures.",
  "status": "untested"
}
```

### 7.3 Experiment

A bounded test with one primary variable.

```json
{
  "id": "exp-001",
  "hypothesis_id": "hyp-001",
  "variable_changed": "reporting structure",
  "baseline": "unstructured chat workflow",
  "metric": "recorded action coverage",
  "status": "planned"
}
```

### 7.4 Evidence

An observed result connected to an artifact.

```json
{
  "id": "ev-001",
  "experiment_id": "exp-001",
  "artifact": "experiments/exp-001/results.csv",
  "summary": "Structured workflow recorded 94% of agent actions.",
  "verification_status": "partial"
}
```

### 7.5 Claim

A conclusion derived from evidence.

```json
{
  "id": "claim-001",
  "statement": "Structured research loops improve auditability in agent-assisted research.",
  "evidence_ids": ["ev-001"],
  "status": "partially_verified"
}
```

### 7.6 Citation

A verified external source.

```json
{
  "id": "cite-001",
  "title": "Agentic AI: Autonomous Intelligence for Complex Goals—A Comprehensive Survey",
  "source": "IEEE Access",
  "doi": "10.1109/ACCESS.2025.3532853",
  "verified": true
}
```

### 7.7 Verification

A method for checking a claim.

```json
{
  "id": "ver-001",
  "claim_id": "claim-001",
  "method": "replication script",
  "script": "verification/verify-exp-001.py",
  "result": "passed",
  "status": "verified"
}
```

---

## 8. Architecture

Agent-Research is organized into five layers.

### 8.1 Human Layer

Defines goals, constraints, ethical boundaries, approval gates, and publication intent.

### 8.2 Agent Layer

Plans, executes, tests, documents, searches, verifies, and escalates.

### 8.3 Governance Layer

Enforces policy, permissions, citation rules, evaluation rules, cost limits, and human review.

### 8.4 Evidence Layer

Stores reports, logs, datasets, plots, benchmark results, failures, and verification artifacts.

### 8.5 Publication Layer

Turns verified artifacts into whitepapers, technical reports, blogs, papers, benchmarks, and releases.

---

## 9. Governance Model

The survey literature emphasizes that Agentic AI creates challenges around accountability, transparency, privacy, fairness, safety, regulation, and human oversight. Agent-Research turns those concerns into operating rules.

### 9.1 Human-in-the-loop and human-on-the-loop

Human approval is required for publishing claims, changing benchmark definitions, using restricted data, running expensive compute, deleting evidence, or submitting public research.

### 9.2 Sandboxed execution

Agents should operate in bounded environments with explicit access to files, tools, secrets, network calls, and compute resources.

### 9.3 Citation governance

Every citation must record title, author list, venue, year, identifier, source URL or DOI, and claim relevance.

### 9.4 Evaluation governance

Every experiment must record baseline, metric, dataset, version, seed, environment, command, and known limitations.

### 9.5 Transparency and audit trails

Every agent action that affects research state must be traceable.

---

## 10. Evaluation Metrics for Research Agents

Agentic AI is often evaluated through adaptability, goal achievement efficiency, learning rate, robustness, scalability, and human-AI collaboration quality. Agent-Research adapts these into research-specific metrics:

- claim accuracy;
- citation accuracy;
- evidence completeness;
- reproducibility coverage;
- failure preservation;
- baseline integrity;
- one-variable experiment compliance;
- verification coverage;
- human review readiness;
- cost and compute efficiency;
- audit trail completeness.

Anti-metrics include fabricated citations, silent metric changes, missing baselines, unverified claims, undocumented failures, and overconfident conclusions.

---

## 11. Recommended Repository Structure

```text
Agent-Research/
  README.md
  WHITEPAPER.md
  GOVERNANCE.md
  SECURITY.md

  principles/
    00-overview.md
    01-human-directed-research.md
    02-agent-as-research-associate.md
    03-evidence-preserving-workflows.md
    04-research-as-kept-promise.md

  commandments/
    00-commandments.md
    01-integrity.md
    02-autonomy.md
    03-scientific-rigor.md
    04-reproducibility.md

  templates/
    INSTRUCTIONS.md
    RESEARCH_PLAN.md
    REPORT.md
    TODO.md
    EXPERIMENT_LOG.md
    CLAIM_CARD.md
    CITATION_CARD.md
    VERIFICATION_CARD.md

  schemas/
    research-question.schema.json
    hypothesis.schema.json
    experiment.schema.json
    evidence.schema.json
    claim.schema.json
    citation.schema.json
    verification.schema.json

  workflows/
    agent-session.md
    literature-review.md
    code-experiment.md
    benchmark-evaluation.md
    publication-review.md

  examples/
    literature-review/
    ml-experiment/
    software-research/
    policy-research/

  governance/
    evaluation-policy.md
    citation-policy.md
    reproducibility-policy.md
    human-approval-policy.md
```

---

## 12. Roadmap

### Phase 1: Foundation

- Publish README and whitepaper.
- Add commandments.
- Add templates.
- Add schemas.
- Add GitHub issue templates.

### Phase 2: Workflow

- Add research session runner.
- Add experiment logger.
- Add citation card generator.
- Add claim card generator.
- Add report generator.

### Phase 3: Governance

- Add policy-as-code.
- Add permission profiles.
- Add approval gates.
- Add audit logs.
- Add evaluation registry.

### Phase 4: Platform Integration

- Integrate with Agent-Builder.
- Integrate with Agent-Registry.
- Integrate with Agent-Trust.
- Integrate with Agent-Policy.
- Integrate with Agent-Publishing.

### Phase 5: Public Research Network

- Enable open research projects.
- Support community review.
- Publish reproducibility challenges.
- Maintain verified claim registry.

---

## 13. Conclusion

The future of research is not fully automated. The future of research is governed, agent-assisted, evidence-preserving, and human-directed.

AGenNext Agent-Research is the discipline layer for that future.

The human asks the question.  
The agent runs the loop.  
The system preserves the evidence.  
The community audits the claim.  
Only then does research become knowledge.
