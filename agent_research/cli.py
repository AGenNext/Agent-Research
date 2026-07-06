from pathlib import Path
from typing import Optional

import typer

from agent_research.dashboard import DashboardExporter
from agent_research.core.regression import RegressionGate
from agent_research.core.report import MarkdownReportGenerator
from agent_research.core.runner import BenchmarkRunner
from agent_research.core.summary import SummaryWriter
from agent_research.platform import FlowEngine, ResearchStore
from agent_research.platform.models import FlowRun

app = typer.Typer(help="AGenNext Agent-Research CLI")
clear_app = typer.Typer(help="CLEARBench evaluation commands")
flow_app = typer.Typer(help="Governed research flow commands")

app.add_typer(clear_app, name="clear")
app.add_typer(flow_app, name="flow")


def _engine(workspace: str) -> FlowEngine:
    return FlowEngine(ResearchStore(workspace))


def _echo_flow_run(run: FlowRun):
    typer.echo(f"Flow Run: {run.id}")
    typer.echo(f"Flow: {run.flow_id}")
    typer.echo(f"Objective: {run.objective_id}")
    typer.echo(f"Status: {run.status}")
    typer.echo(f"Gates: {', '.join(run.gates) if run.gates else 'none'}")
    for step in run.steps:
        gate = f" [{step.gate}]" if step.gate else ""
        typer.echo(f"- {step.id}: {step.status}{gate}")


@flow_app.command("init")
def init_workspace(
    title: str = "Agent-Research Workspace",
    owner: str = "human",
    workspace: str = ".agent-research",
):
    """Initialize a local governed research workspace."""
    created = _engine(workspace).init_workspace(title=title, owner=owner)
    typer.echo(f"Workspace created: {created.id}")
    typer.echo(f"State path: {workspace}")


@flow_app.command("objective")
def create_objective(
    title: str,
    question: str = "",
    workspace_id: str = "default",
    owner: str = "human",
    domain: str = "agentic-research",
    workspace: str = ".agent-research",
):
    """Create a research objective card."""
    objective = _engine(workspace).create_objective(
        title=title,
        question=question,
        workspace_id=workspace_id,
        owner=owner,
        domain=domain,
    )
    typer.echo(f"Objective created: {objective.id}")
    typer.echo(f"Status: {objective.status}")


@flow_app.command("list")
def list_flows(workspace: str = ".agent-research"):
    """List built-in executable flows."""
    engine = _engine(workspace)
    for flow_id in engine.available_flows():
        typer.echo(flow_id)


@flow_app.command("run")
def run_flow(
    flow_id: str,
    objective_id: str,
    actor: str = "human",
    workspace: str = ".agent-research",
    stop_at_gate: bool = True,
):
    """Run a governed research flow until completion or the next gate."""
    run = _engine(workspace).run_flow(
        flow_id=flow_id,
        objective_id=objective_id,
        actor=actor,
        stop_at_gate=stop_at_gate,
    )
    _echo_flow_run(run)


@flow_app.command("approve")
def approve_gate(
    run_id: str,
    actor: str = "human",
    workspace: str = ".agent-research",
):
    """Approve the next waiting gate for a flow run."""
    run = _engine(workspace).approve_next_gate(run_id=run_id, actor=actor)
    _echo_flow_run(run)


@flow_app.command("status")
def flow_status(run_id: str, workspace: str = ".agent-research"):
    """Show a flow run status."""
    store = ResearchStore(workspace)
    run = store.load("flows", run_id, FlowRun)
    _echo_flow_run(run)


@flow_app.command("objectives")
def list_objectives(workspace: str = ".agent-research"):
    """List local research objectives."""
    from agent_research.platform.models import Objective

    store = ResearchStore(workspace)
    for objective in store.list("objectives", Objective):
        typer.echo(f"{objective.id} | {objective.status} | {objective.title}")


@clear_app.command("run")
def run_benchmark(
    benchmark_dir: str,
    output: str = "outputs",
    repeats: int = 1,
    agent: str = "echo",
):
    runner = BenchmarkRunner(agent_name=agent)

    evaluations = runner.run_benchmark(benchmark_dir, repeats=repeats)

    for evaluation in evaluations:
        runner.save_result(output, evaluation)

    summary = runner.build_summary(evaluations)

    reporter = MarkdownReportGenerator()
    reporter.generate(summary, output)

    dashboard = DashboardExporter()
    dashboard.export_summary(summary, output)

    summary_writer = SummaryWriter()
    summary_writer.write(
        output,
        {
            "run_id": runner.context.run_id,
            "agent_team_id": runner.context.agent_team_id,
            "benchmark_dir": benchmark_dir,
            "repeats": repeats,
            "summary": summary.model_dump(),
            "evaluations": [e.model_dump() for e in evaluations],
        },
    )

    typer.echo("CLEARBench execution complete")
    typer.echo(f"Run ID: {runner.context.run_id}")
    typer.echo(f"Agent: {agent}")
    typer.echo(f"Tasks: {summary.total_tasks}")
    typer.echo(f"Runs: {summary.total_runs}")
    typer.echo(f"Success Rate: {summary.success_rate:.2f}")
    typer.echo(f"CLEAR Score: {summary.clear_score:.2f}")


@clear_app.command("compare")
def compare_runs(baseline: str, candidate: str):
    gate = RegressionGate()

    result = gate.compare(baseline, candidate)

    typer.echo("Comparison complete")
    typer.echo(f"Baseline Success Rate: {result['baseline_success_rate']:.2f}")
    typer.echo(f"Candidate Success Rate: {result['candidate_success_rate']:.2f}")
    typer.echo(f"Delta: {result['delta']:.2f}")


@clear_app.command("gate")
def gate_run(
    baseline: str,
    candidate: str,
    min_delta: float = 0.0,
):
    gate = RegressionGate()

    result = gate.compare(baseline, candidate)

    passed = result["delta"] >= min_delta

    typer.echo(f"Gate Passed: {passed}")

    if not passed:
        raise typer.Exit(code=1)


@clear_app.command("report")
def generate_report(output: str = "outputs"):
    path = Path(output)

    files = list(path.glob("*.json"))

    typer.echo(f"Found {len(files)} evaluation artifacts")

    report_path = path / "report.md"

    if report_path.exists():
        typer.echo(f"Markdown report: {report_path}")

    dashboard_path = path / "dashboard.json"

    if dashboard_path.exists():
        typer.echo(f"Dashboard export: {dashboard_path}")

    summary_path = path / "summary.json"

    if summary_path.exists():
        typer.echo(f"Summary artifact: {summary_path}")

    for file in files:
        typer.echo(file.name)


if __name__ == "__main__":
    app()
