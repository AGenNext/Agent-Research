from agent_research.platform import FlowEngine, ResearchStore
from agent_research.platform.models import FlowRunStatus, ObjectiveStatus


def test_flow_run_stops_at_gate(tmp_path):
    store = ResearchStore(str(tmp_path / "state"))
    engine = FlowEngine(store)

    objective = engine.create_objective(
        title="Test governed research loop",
        question="Can a flow preserve gates?",
    )

    run = engine.run_flow("intake", objective.id, stop_at_gate=True)

    assert run.flow_id == "research-objective-intake"
    assert run.status == FlowRunStatus.WAITING_FOR_HUMAN
    assert any(step.status == "waiting_for_gate" for step in run.steps)


def test_flow_run_completes_without_gate_stop(tmp_path):
    store = ResearchStore(str(tmp_path / "state"))
    engine = FlowEngine(store)

    objective = engine.create_objective(title="Test complete run")
    run = engine.run_flow("experiment", objective.id, stop_at_gate=False)

    assert run.status == FlowRunStatus.COMPLETED
    updated = store.load("objectives", objective.id, type(objective))
    assert updated.status == ObjectiveStatus.VERIFYING
