from typing import Dict, List

from agent_research.platform.models import FlowStep

DEFAULT_FLOWS: Dict[str, List[FlowStep]] = {
    "research-objective-intake": [
        FlowStep(id="capture", name="Capture raw idea"),
        FlowStep(id="scope", name="Scope objective", gate="scope gate"),
        FlowStep(id="criteria", name="Define success criteria"),
        FlowStep(id="evidence", name="Define evidence requirements", gate="evidence gate"),
        FlowStep(id="risk", name="Assign risk level", gate="risk gate"),
        FlowStep(id="plan", name="Create research plan"),
        FlowStep(id="approval", name="Request human approval", gate="human approval gate"),
    ],
    "literature-evidence": [
        FlowStep(id="search-plan", name="Generate source search plan"),
        FlowStep(id="collect", name="Collect candidate sources"),
        FlowStep(id="dedupe", name="Remove duplicate sources"),
        FlowStep(id="citation", name="Verify citation metadata", gate="citation gate"),
        FlowStep(id="extract", name="Extract evidence"),
        FlowStep(id="grade", name="Grade evidence quality", gate="source gate"),
        FlowStep(id="freshness", name="Mark freshness", gate="freshness gate"),
        FlowStep(id="pack", name="Store evidence pack"),
    ],
    "experiment-execution": [
        FlowStep(id="confirm", name="Confirm hypothesis metric and baseline", gate="baseline gate"),
        FlowStep(id="one-variable", name="Confirm one changed variable", gate="one-variable gate"),
        FlowStep(id="prepare", name="Prepare environment"),
        FlowStep(id="tier1", name="Run Tier 1 smoke test", gate="smoke-test gate"),
        FlowStep(id="tier2", name="Run Tier 2 small-signal test"),
        FlowStep(id="tier3", name="Run Tier 3 full evaluation", gate="full-evaluation gate"),
        FlowStep(id="capture", name="Capture logs outputs configs and failures"),
        FlowStep(id="analyze", name="Analyze against baseline"),
        FlowStep(id="record", name="Update report and TODO", gate="artifact gate"),
    ],
    "claim-verification": [
        FlowStep(id="normalize", name="Normalize claim into one sentence", gate="precision gate"),
        FlowStep(id="link", name="Link evidence", gate="evidence gate"),
        FlowStep(id="citation", name="Check citations", gate="citation gate"),
        FlowStep(id="counter", name="Search for counterevidence", gate="counterevidence gate"),
        FlowStep(id="verify", name="Run verification", gate="verification gate"),
        FlowStep(id="review", name="Request human review", gate="review gate"),
    ],
    "clearbench-evaluation": [
        FlowStep(id="load", name="Load benchmark"),
        FlowStep(id="baseline", name="Run baseline"),
        FlowStep(id="candidate", name="Run candidate"),
        FlowStep(id="traces", name="Capture traces"),
        FlowStep(id="efficacy", name="Grade efficacy"),
        FlowStep(id="cost", name="Calculate cost"),
        FlowStep(id="latency", name="Calculate latency"),
        FlowStep(id="assurance", name="Run assurance checks"),
        FlowStep(id="reliability", name="Run reliability checks"),
        FlowStep(id="report", name="Generate comparison report"),
    ],
    "publication-release": [
        FlowStep(id="freeze", name="Freeze candidate artifact"),
        FlowStep(id="claims", name="Check claims", gate="claim gate"),
        FlowStep(id="citations", name="Check citations", gate="citation gate"),
        FlowStep(id="limitations", name="Check limitations", gate="limitation gate"),
        FlowStep(id="data", name="Check data policy", gate="data policy gate"),
        FlowStep(id="license", name="Check license", gate="license gate"),
        FlowStep(id="approval", name="Request human approval", gate="approval gate"),
        FlowStep(id="release", name="Create release snapshot", gate="release gate"),
    ],
    "evidence-refresh": [
        FlowStep(id="load", name="Load source index"),
        FlowStep(id="availability", name="Check source availability"),
        FlowStep(id="freshness", name="Check freshness", gate="freshness gate"),
        FlowStep(id="impact", name="Identify impacted claims", gate="impact gate"),
        FlowStep(id="verify", name="Run verification", gate="verification gate"),
        FlowStep(id="notify", name="Notify reviewer", gate="notification gate"),
        FlowStep(id="report", name="Create refresh report"),
    ],
}

FLOW_ALIASES = {
    "intake": "research-objective-intake",
    "literature": "literature-evidence",
    "evidence": "literature-evidence",
    "experiment": "experiment-execution",
    "claim": "claim-verification",
    "clear": "clearbench-evaluation",
    "publish": "publication-release",
    "refresh": "evidence-refresh",
}


def resolve_flow_id(flow_id: str) -> str:
    return FLOW_ALIASES.get(flow_id, flow_id)
