import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
CORS_ORIGINS = [
    origin.strip()
    for origin in os.getenv("CORS_ORIGINS", "*").split(",")
    if origin.strip()
]

app = FastAPI(title="Agent-Research Backend", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

sample_data = {
    "agentNodes": [
        {
            "id": "planner",
            "label": "Planner Agent",
            "score": 0.86,
            "trustScore": 0.82,
            "status": "passed"
        },
        {
            "id": "coder",
            "label": "Coder Agent",
            "score": 0.52,
            "trustScore": 0.61,
            "status": "warning"
        }
    ],
    "executionLogs": [
        {
            "id": "log-1",
            "type": "agent",
            "message": "Planner created implementation plan",
            "score": 0.86
        }
    ]
}

FLOW_CATALOG = [
    "research-objective-intake",
    "literature-evidence",
    "experiment-execution",
    "claim-verification",
    "clearbench-evaluation",
    "publication-release",
    "evidence-refresh",
]

PLATFORM_GRAPH = {
    "nodes": [
        {"id": "human-pi", "label": "Human Principal Investigator", "kind": "human"},
        {"id": "concierge", "label": "Research Concierge Agent", "kind": "agent"},
        {"id": "literature", "label": "Literature Agent", "kind": "agent"},
        {"id": "experiment", "label": "Experiment Agent", "kind": "agent"},
        {"id": "evidence", "label": "Evidence Agent", "kind": "agent"},
        {"id": "citation", "label": "Citation Verifier Agent", "kind": "agent"},
        {"id": "claim", "label": "Claim Auditor Agent", "kind": "agent"},
        {"id": "clear", "label": "CLEAR Evaluator Agent", "kind": "agent"},
        {"id": "publisher", "label": "Publisher Agent", "kind": "agent"},
    ],
    "edges": [
        {"source": "human-pi", "target": "concierge", "label": "objective"},
        {"source": "concierge", "target": "literature", "label": "source search"},
        {"source": "concierge", "target": "experiment", "label": "experiment plan"},
        {"source": "literature", "target": "evidence", "label": "evidence cards"},
        {"source": "evidence", "target": "citation", "label": "citation check"},
        {"source": "evidence", "target": "claim", "label": "claim support"},
        {"source": "experiment", "target": "clear", "label": "benchmark result"},
        {"source": "claim", "target": "publisher", "label": "reviewed claims"},
        {"source": "publisher", "target": "human-pi", "label": "approval gate"},
    ],
}


class ObjectiveRequest(BaseModel):
    title: str
    question: str = ""
    owner: str = "human"


@app.get("/")
def root():
    return {
        "name": "Agent-Research Backend",
        "status": "ok",
        "version": "0.1.0",
        "environment": ENVIRONMENT
    }


@app.get("/health")
def health():
    return {"status": "healthy", "environment": ENVIRONMENT}


@app.get("/api/demo")
def demo_data():
    return sample_data


@app.get("/api/platform")
def platform_overview():
    return {
        "name": "Agent-Research Platform",
        "principle": "No claim without evidence. No evidence without source. No publication without review.",
        "flows": FLOW_CATALOG,
        "graph": PLATFORM_GRAPH,
    }


@app.get("/api/flows")
def list_flows():
    return {"flows": FLOW_CATALOG}


@app.post("/api/objectives")
def create_objective(request: ObjectiveRequest):
    return {
        "id": "obj-demo",
        "title": request.title,
        "question": request.question,
        "owner": request.owner,
        "status": "proposed",
        "next_flow": "research-objective-intake",
    }
