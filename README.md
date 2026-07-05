# AGenNext Agent-Research

**Governed agentic research infrastructure for human-directed, agent-assisted R&D.**

Agent-Research is the canonical AGenNext initiative for open agent research, education, awareness, standards, CLEAR-style evaluation, and responsible adoption.

It helps communities, builders, researchers, and enterprises understand, evaluate, and govern agent systems with evidence, provenance, reproducible artifacts, and human review.

Agent-Research is not a chatbot wrapper. It is a research operating layer.

---

## Responsibility

Agent-Research owns open research collection, evidence tracking, evaluation education, and research-to-decision workflows for agent systems.

It grounds product, technical, market, architecture, governance, and adoption decisions in verifiable evidence.

---

## Why this exists

Agentic AI systems can pursue complex goals, adapt to changing environments, use tools, reason over context, and execute long-running workflows. That makes them powerful for research and development.

But research is not just output generation. Research requires discipline:

- clear questions;
- testable hypotheses;
- controlled experiments;
- honest evaluation;
- verified citations;
- reproducible evidence;
- preserved failures;
- human review.

Without governance, agentic systems can drift, overclaim, fabricate citations, silently change evaluation criteria, or forget failed paths. Agent-Research exists to prevent that.

---

## Scope

Agent-Research covers:

- open agent research;
- agent education and awareness;
- academic research tracking;
- arXiv, IEEE, ACM, and paper evidence;
- market research;
- competitor research;
- technical due diligence;
- tool and library research;
- license and ecosystem research;
- research freshness checks;
- research-to-decision traceability;
- AI and agent evaluation research;
- responsible agent adoption;
- agent identity, governance, and operating model research.

---

## Core Principle

```text
No strategic decision without evidence.
No evidence without source.
No source without freshness and provenance.
No evaluation without reproducible artifacts.
No adoption without education, governance, and responsibility.
```

---

## Agentic Research Loop

```text
Explore → Plan → Implement → Evaluate → Analyze → Record → Commit → Iterate
```

The agent may execute the loop, but the human remains the principal investigator.

---

## Research Commandments

1. Never break a promise.
2. Never manipulate evaluation.
3. Never fabricate citations.
4. Complete autonomous work before reporting.
5. Make it work before moving on.
6. Change one variable per experiment.
7. Evaluate in tiers.
8. Bound expectations.
9. Record everything.
10. Verify before claiming.

---

## Research Primitives

Agent-Research defines research as connected artifacts:

- research question;
- hypothesis;
- experiment;
- evidence;
- claim;
- citation;
- verification;
- report;
- review decision.

---

## First Concrete Vertical: CLEARBench

CLEARBench is the first implementation vertical inside Agent-Research.

It is inspired by the CLEAR framework from *Beyond Accuracy: A Multi-Dimensional Framework for Evaluating Enterprise Agentic AI Systems*.

CLEAR evaluates agentic systems across five production dimensions:

- **Cost**: token usage, estimated API cost, cost per success, cost-normalized accuracy;
- **Latency**: wall-clock execution time, p50/p95 latency, SLA compliance;
- **Efficacy**: task success and domain-specific grading;
- **Assurance**: safety, policy compliance, prompt-injection resistance, data-leak prevention;
- **Reliability**: repeated-run stability through pass@k-style measurements.

The goal is to move beyond accuracy-only benchmarks and produce reproducible evaluation artifacts for enterprise AI agents.

---

## Consumers

- Agent-Team
- Agent-Knowledge
- Agent-Blueprint
- Agent-Eval
- Agent-Bench
- Model-Router
- future AGenNext products
- open community education and awareness programs

---

## Research Loop

```text
question
  → search sources
  → collect evidence
  → evaluate trust
  → synthesize options
  → recommend decision
  → link decision to evidence
  → refresh when evidence changes
```

## Evaluation Loop

```text
benchmark
  → run agent/model
  → capture traces
  → grade outputs
  → calculate CLEAR metrics
  → generate report
  → compare alternatives
  → preserve artifacts
```

---

## Quick Start

```bash
pip install -e .
agent-research clear run benchmarks/clearbench_mini --agent echo --repeats 3 --output outputs/clearbench-mini-echo
agent-research clear report outputs/clearbench-mini-echo
```

---

## UI Deployment

The CLEARBench UI lives in `ui/` and is deployed with GitHub Pages using the repository workflow in `.github/workflows/pages.yml`.

---

## Whitepaper

Read the canonical whitepaper: [`WHITEPAPER.md`](./WHITEPAPER.md).

---

## Repository Boundary

```text
Agent-Research
  → open research, education, awareness, and research-backed evaluation verticals

Agent-Trust
  → provenance and trust scoring

Agent-Eval
  → shared scoring and evaluation methods

Agent-Analytics
  → adoption/performance signals

Agent-Team
  → uses research and evaluation to make better decisions
```

---

## Initial Roadmap

- [x] Add whitepaper
- [x] Align README with governed agentic research
- [ ] Add governance policy
- [ ] Add templates
- [ ] Add JSON schemas
- [ ] Add GitHub issue templates
- [ ] Add research workflow examples
- [ ] Add citation verification workflow
- [ ] Add claim verification workflow
