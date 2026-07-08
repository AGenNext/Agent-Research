# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

Agent-Research is AGenNext's governed agentic research platform. It contains three independent deployables plus a large body of governance/spec documentation:

1. **`agent_research/`** — the core Python package (installed as `agent-research` CLI via Typer). Contains the CLEARBench evaluation pipeline and the executable research flow engine.
2. **`backend/`** — a small standalone FastAPI demo API. It does **not** import the `agent_research` package; it serves hardcoded demo data (flow catalog, agent graph) for the UI. Has its own `requirements.txt`, Dockerfile, and tests (`backend/test_*.py`).
3. **`ui/`** — a React + Vite + TypeScript dashboard, deployed to GitHub Pages (Vite `base` is `/Agent-Research/`). Reads `VITE_API_BASE_URL` to reach the backend.

## Commands

```bash
# Core package: install + test
pip install -e . pytest
pytest                          # all tests in tests/
pytest tests/test_metrics.py    # single test file
pytest -k platform_flow         # by keyword

# CLEARBench evaluation
agent-research clear run benchmarks/clearbench_mini --agent echo --repeats 3 --output outputs/demo
agent-research clear report outputs/demo
agent-research clear compare <baseline_dir> <candidate_dir>
agent-research clear gate <baseline_dir> <candidate_dir> --min-delta 0.0   # exits 1 on regression

# Governed research flows (state stored in .agent-research/)
agent-research flow init --title "My Workspace"
agent-research flow objective "Title" --question "..."
agent-research flow list
agent-research flow run intake <objective-id>     # runs until the next human gate
agent-research flow approve <flowrun-id>          # approve gate, then re-run status
agent-research flow status <flowrun-id>

# Backend (from backend/)
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
pytest -q                       # backend tests live next to the code

# UI (from ui/)
npm install
npm run dev                     # dev server on 5173
npm run build

# Full stack
docker compose up               # backend on 8000, UI dev server on 5173
```

There is no configured linter or formatter. Python requires 3.10+ (CI uses 3.11/3.12); code uses Pydantic v2 (`model_dump`, `model_dump_json`).

## CI

- `.github/workflows/ci.yml` — three jobs: package (`pytest -q tests`), frontend (`npm run build` in `ui/`), backend (import check + `pytest -q` in `backend/`).
- `.github/workflows/tests.yml` — runs root `pytest` on every push.
- `.github/workflows/pages.yml` — builds `ui/` and deploys `ui/dist` to GitHub Pages on push to `main`.
- `.github/workflows/docker-publish.yml` — builds a Docker image from the repo root context to GHCR.

## Architecture

### CLEARBench evaluation pipeline (`agent_research/core/`, `agents/`, `oracles/`, `execution/`, `verticals/`)

The flow of `agent-research clear run`:

1. `cli.py` → `BenchmarkRunner` (`core/runner.py`) loads every `*.yaml` task in the benchmark directory into `BenchmarkTask` (`core/schemas.py`). Task YAML fields: `id`, `domain`, `title`, `prompt`, `expected.must_include`, `sla_seconds`, `policy.forbidden`, optional `oracle` config. See `benchmarks/clearbench_mini/` for examples.
2. `agents/factory.py` creates the agent by name: `echo`, `openai`, `anthropic`. **The OpenAI/Anthropic agents are scaffolds** — they read `OPENAI_API_KEY`/`ANTHROPIC_API_KEY` but return canned output; only `echo` is real.
3. `verticals/ai_agent_eval/graders.py` (`RuleBasedGrader`) produces initial per-dimension scores, then an oracle (`core/oracles.py::OracleFactory`) produces the `FinalVerdict` that overwrites success/efficacy. Oracle types: `rule_based` (substring checks against `expected.must_include`), `command` (shell command, pass = exit 0), `execution` (`core/execution_oracle.py` — applies the agent's output as a patch in a temp workspace and runs tests inside Docker via `execution/docker_runner.py`, which uses `--network none`; requires Docker).
4. Everything is evidence-tracked: `core/events.py` defines `EvaluationEvent`s appended as JSONL by `TraceCollector` (`core/traces.py`, default `traces/` in CWD), and prompts/outputs/verdicts are content-addressed by `ArtifactStore` (`core/artifacts.py`, default `artifacts/` in CWD).
5. `core/metrics.py` computes the CLEAR dimensions (Cost, Latency, Efficacy, Assurance, Reliability → `clear_score`), and `core/report.py` / `dashboard.py` / `core/summary.py` write `report.md`, `dashboard.json`, and `summary.json` into the output dir. `core/regression.py` (`RegressionGate`) compares two output dirs by success rate for `clear compare`/`clear gate`.

Caveat: the repo-root `artifacts/` directory contains **committed research artifacts** (e.g. `reactive-flux-aware-surface-selection/`), but `ArtifactStore` also defaults to writing runtime artifacts to `artifacts/` in the CWD, and `traces/` / `.agent-research/` are not gitignored (`outputs/` is). Don't commit runtime evaluation output; run evaluations from a scratch directory or clean up afterward.

### Flow engine (`agent_research/platform/`)

- `models.py` — Pydantic models for the platform primitives (Workspace, Objective, FlowRun, FlowStep, AuditEvent) and the objective lifecycle statuses.
- `store.py` (`ResearchStore`) — filesystem JSON store under `.agent-research/` (one directory per primitive collection, plus append-only `audit.jsonl`). Intentionally simple; SurrealDB is the planned future backend.
- `default_flows.py` — the seven built-in flows (`research-objective-intake`, `literature-evidence`, `experiment-execution`, `claim-verification`, `clearbench-evaluation`, `publication-release`, `evidence-refresh`) plus short CLI aliases (`intake`, `literature`, `experiment`, `claim`, `clear`, `publish`, `refresh`).
- `flow_engine.py` (`FlowEngine`) — deterministic, gate-aware runner. Steps execute in order, each writes a markdown artifact and audit events; when a step has a `gate`, the run stops with status `waiting_for_human` until `flow approve`. Completing a flow advances the linked objective's status via the transition map in `_advance_objective`. Real agent execution is meant to attach behind this same contract later.

### Keep these in sync

The flow catalog is duplicated in three places: `agent_research/platform/default_flows.py` (executable), `backend/main.py::FLOW_CATALOG` (demo API), and the markdown specs in `flows/*.md`. If you add or rename a flow, update all three.

## Documentation layout

The repo is doc-heavy by design — research governance is the product. `README.md` (principles, research commandments), `PLATFORM.md` (platform layers, actor model, lifecycle states, gates), `GOVERNANCE.md`, `WHITEPAPER.md`, `DEPLOYMENT.md`, `docs/flow-runner.md` (flow CLI usage), `flows/` (per-flow markdown specs), `contracts/` (research contract), `schemas/` (JSON Schemas for citation/claim/experiment), `templates/` (claim/citation/experiment/plan card templates), `research/` (collected paper notes), `benchmarks/` (task definitions).

Core principle to respect in any change: evidence, provenance, and human review gates are non-negotiable — don't remove audit events, artifact writes, or gate stops to "simplify" code.

## Conventions

- Commit messages use a short scope prefix, e.g. `platform: add flow engine tests`.
- New benchmark tasks are plain YAML files dropped into a benchmark directory — no registration step needed.
- New agents register in the `AGENTS` dict in `agent_research/agents/factory.py` and subclass `agents/base.py::BaseAgent` (implement `run(task) -> AgentResult`).
- New oracle types register in `core/oracles.py::OracleFactory`.
