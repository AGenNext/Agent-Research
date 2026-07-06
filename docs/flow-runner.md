# Executable Flow Runner

Agent-Research includes a local filesystem-backed flow engine for governed research workflows.

## Install

```bash
pip install -e .
```

## Commands

```bash
agent-research flow init --title "Agent Research Workspace"
agent-research flow objective "Evaluate governed agentic research" --question "Can agents preserve evidence?"
agent-research flow list
agent-research flow run intake obj-your-id
agent-research flow status flowrun-your-id
agent-research flow approve flowrun-your-id
```

## Local State

State is stored in `.agent-research/`.

```text
.agent-research/
  workspaces/
  objectives/
  flows/
  evidence/
  claims/
  citations/
  artifacts/
  audit.jsonl
```

## Flow Behavior

The current runner is deterministic and gate-aware. It creates flow runs, step artifacts, and audit events. Real agent execution can attach behind the same contract later.

## Built-In Flows

```text
research-objective-intake
literature-evidence
experiment-execution
claim-verification
clearbench-evaluation
publication-release
evidence-refresh
```
