from copy import deepcopy
from typing import Any, Dict, List

from agent_research.platform.default_flows import DEFAULT_FLOWS, resolve_flow_id
from agent_research.platform.models import (
    AuditEvent,
    FlowRun,
    FlowRunStatus,
    Objective,
    ObjectiveStatus,
    Workspace,
    utc_now,
)
from agent_research.platform.store import ResearchStore


class FlowEngine:
    """Runs documented Agent-Research flows against the local store.

    The first implementation is deterministic and file-backed. Each run creates
    explicit step state, artifacts, and audit events. Real agent execution can be
    attached behind the same contract later.
    """

    def __init__(self, store: ResearchStore):
        self.store = store

    def init_workspace(self, title: str = "Agent-Research Workspace", owner: str = "human") -> Workspace:
        workspace = Workspace(title=title, owner=owner)
        artifact = self.store.save("workspaces", workspace)
        self.store.append_audit(
            AuditEvent(
                actor=owner,
                action="create_workspace",
                target_type="workspace",
                target_id=workspace.id,
                result="created",
                artifact=artifact,
            )
        )
        return workspace

    def create_objective(
        self,
        title: str,
        question: str = "",
        workspace_id: str = "default",
        owner: str = "human",
        domain: str = "agentic-research",
        success_criteria: List[str] | None = None,
    ) -> Objective:
        objective = Objective(
            workspace_id=workspace_id,
            title=title,
            question=question,
            owner=owner,
            domain=domain,
            success_criteria=success_criteria or [],
            status=ObjectiveStatus.PROPOSED,
        )
        artifact = self.store.save("objectives", objective)
        self.store.append_audit(
            AuditEvent(
                actor=owner,
                action="create_objective",
                target_type="objective",
                target_id=objective.id,
                result="created",
                artifact=artifact,
            )
        )
        return objective

    def available_flows(self) -> List[str]:
        return sorted(DEFAULT_FLOWS.keys())

    def create_flow_run(
        self,
        flow_id: str,
        objective_id: str,
        actor: str = "human",
        inputs: Dict[str, Any] | None = None,
    ) -> FlowRun:
        canonical_flow_id = resolve_flow_id(flow_id)
        if canonical_flow_id not in DEFAULT_FLOWS:
            raise ValueError(f"Unknown flow '{flow_id}'. Available: {', '.join(self.available_flows())}")

        run = FlowRun(
            flow_id=canonical_flow_id,
            objective_id=objective_id,
            actor=actor,
            status=FlowRunStatus.CREATED,
            inputs=inputs or {},
            steps=deepcopy(DEFAULT_FLOWS[canonical_flow_id]),
            gates=[step.gate for step in DEFAULT_FLOWS[canonical_flow_id] if step.gate],
        )
        artifact = self.store.save("flows", run)
        self.store.append_audit(
            AuditEvent(
                actor=actor,
                action="create_flow_run",
                target_type="flow_run",
                target_id=run.id,
                result="created",
                artifact=artifact,
                metadata={"flow_id": canonical_flow_id, "objective_id": objective_id},
            )
        )
        return run

    def run_flow(
        self,
        flow_id: str,
        objective_id: str,
        actor: str = "human",
        inputs: Dict[str, Any] | None = None,
        stop_at_gate: bool = True,
    ) -> FlowRun:
        run = self.create_flow_run(flow_id, objective_id, actor=actor, inputs=inputs)
        run.status = FlowRunStatus.RUNNING
        run.updated_at = utc_now()

        for step in run.steps:
            step.started_at = utc_now()
            step.status = "running"
            self.store.append_audit(
                AuditEvent(
                    actor=actor,
                    action="start_step",
                    target_type="flow_step",
                    target_id=f"{run.id}:{step.id}",
                    result="running",
                    metadata={"flow_id": run.flow_id, "step": step.name},
                )
            )

            artifact_path = self._materialize_step_artifact(run, step.id, step.name)
            step.artifacts.append(artifact_path)
            step.completed_at = utc_now()

            if step.gate and stop_at_gate:
                step.status = "waiting_for_gate"
                run.status = FlowRunStatus.WAITING_FOR_HUMAN
                run.artifacts.append(artifact_path)
                run.updated_at = utc_now()
                self.store.save("flows", run)
                self.store.append_audit(
                    AuditEvent(
                        actor=actor,
                        action="gate_reached",
                        target_type="flow_run",
                        target_id=run.id,
                        result="waiting_for_human",
                        artifact=artifact_path,
                        metadata={"gate": step.gate, "step": step.id},
                    )
                )
                return run

            step.status = "completed"
            run.artifacts.append(artifact_path)
            self.store.append_audit(
                AuditEvent(
                    actor=actor,
                    action="complete_step",
                    target_type="flow_step",
                    target_id=f"{run.id}:{step.id}",
                    result="completed",
                    artifact=artifact_path,
                )
            )

        run.status = FlowRunStatus.COMPLETED
        run.updated_at = utc_now()
        self.store.save("flows", run)
        self.store.append_audit(
            AuditEvent(
                actor=actor,
                action="complete_flow_run",
                target_type="flow_run",
                target_id=run.id,
                result="completed",
                metadata={"flow_id": run.flow_id},
            )
        )
        self._advance_objective(run)
        return run

    def approve_next_gate(self, run_id: str, actor: str = "human") -> FlowRun:
        run = self.store.load("flows", run_id, FlowRun)
        for step in run.steps:
            if step.status == "waiting_for_gate":
                step.status = "completed"
                step.notes.append(f"Gate approved by {actor} at {utc_now()}")
                self.store.append_audit(
                    AuditEvent(
                        actor=actor,
                        action="approve_gate",
                        target_type="flow_step",
                        target_id=f"{run.id}:{step.id}",
                        result="approved",
                        metadata={"gate": step.gate},
                    )
                )
                break
        run.status = FlowRunStatus.RUNNING
        run.updated_at = utc_now()
        self.store.save("flows", run)
        return run

    def _materialize_step_artifact(self, run: FlowRun, step_id: str, step_name: str) -> str:
        content = "\n".join(
            [
                f"# {step_name}",
                "",
                f"- Flow Run: {run.id}",
                f"- Flow: {run.flow_id}",
                f"- Objective: {run.objective_id}",
                f"- Step: {step_id}",
                f"- Actor: {run.actor}",
                f"- Time: {utc_now()}",
                "",
                "## Inputs",
                "",
                "```json",
                run.model_dump_json(indent=2),
                "```",
                "",
                "## Result",
                "",
                "Generated by the local Agent-Research flow engine.",
            ]
        )
        return self.store.write_artifact(f"flows/{run.id}/{step_id}.md", content)

    def _advance_objective(self, run: FlowRun) -> None:
        try:
            objective = self.store.load("objectives", run.objective_id, Objective)
        except FileNotFoundError:
            return

        transitions = {
            "research-objective-intake": ObjectiveStatus.PLANNED,
            "literature-evidence": ObjectiveStatus.RECORDING,
            "experiment-execution": ObjectiveStatus.VERIFYING,
            "claim-verification": ObjectiveStatus.HUMAN_REVIEW,
            "clearbench-evaluation": ObjectiveStatus.HUMAN_REVIEW,
            "publication-release": ObjectiveStatus.PUBLISHED,
            "evidence-refresh": ObjectiveStatus.REFRESH_WATCH,
        }
        objective.status = transitions.get(run.flow_id, objective.status)
        objective.updated_at = utc_now()
        self.store.save("objectives", objective)
