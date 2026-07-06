from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional
from uuid import uuid4

from pydantic import BaseModel, Field


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


class ObjectiveStatus(str, Enum):
    PROPOSED = "proposed"
    SCOPED = "scoped"
    PLANNED = "planned"
    APPROVED = "approved"
    EXECUTING = "executing"
    RECORDING = "recording"
    VERIFYING = "verifying"
    HUMAN_REVIEW = "human_review"
    RELEASE_CANDIDATE = "release_candidate"
    PUBLISHED = "published"
    REFRESH_WATCH = "refresh_watch"
    ARCHIVED = "archived"
    REJECTED = "rejected"
    SUSPENDED = "suspended"
    RETIRED = "retired"


class FlowRunStatus(str, Enum):
    CREATED = "created"
    RUNNING = "running"
    WAITING_FOR_HUMAN = "waiting_for_human"
    COMPLETED = "completed"
    BLOCKED = "blocked"
    FAILED = "failed"


class ClaimStatus(str, Enum):
    UNVERIFIED = "unverified"
    PARTIALLY_VERIFIED = "partially_verified"
    VERIFIED = "verified"
    REPRODUCED = "reproduced"
    REJECTED = "rejected"
    SUPERSEDED = "superseded"
    STALE = "stale"


class Workspace(BaseModel):
    id: str = Field(default_factory=lambda: f"ws-{uuid4().hex[:10]}")
    title: str
    owner: str = "human"
    status: str = "active"
    created_at: str = Field(default_factory=utc_now)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class Objective(BaseModel):
    id: str = Field(default_factory=lambda: f"obj-{uuid4().hex[:10]}")
    workspace_id: str = "default"
    title: str
    question: str = ""
    owner: str = "human"
    domain: str = "agentic-research"
    status: ObjectiveStatus = ObjectiveStatus.PROPOSED
    success_criteria: List[str] = Field(default_factory=list)
    risk_level: str = "medium"
    created_at: str = Field(default_factory=utc_now)
    updated_at: str = Field(default_factory=utc_now)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class FlowStep(BaseModel):
    id: str
    name: str
    status: str = "pending"
    gate: Optional[str] = None
    artifacts: List[str] = Field(default_factory=list)
    notes: List[str] = Field(default_factory=list)
    started_at: Optional[str] = None
    completed_at: Optional[str] = None


class FlowRun(BaseModel):
    id: str = Field(default_factory=lambda: f"flowrun-{uuid4().hex[:10]}")
    flow_id: str
    objective_id: str
    actor: str = "human"
    status: FlowRunStatus = FlowRunStatus.CREATED
    inputs: Dict[str, Any] = Field(default_factory=dict)
    steps: List[FlowStep] = Field(default_factory=list)
    artifacts: List[str] = Field(default_factory=list)
    gates: List[str] = Field(default_factory=list)
    created_at: str = Field(default_factory=utc_now)
    updated_at: str = Field(default_factory=utc_now)


class EvidenceCard(BaseModel):
    id: str = Field(default_factory=lambda: f"ev-{uuid4().hex[:10]}")
    objective_id: str
    source: str
    summary: str
    grade: str = "C"
    provenance: Dict[str, Any] = Field(default_factory=dict)
    status: str = "collected"
    created_at: str = Field(default_factory=utc_now)


class ClaimCard(BaseModel):
    id: str = Field(default_factory=lambda: f"claim-{uuid4().hex[:10]}")
    objective_id: str
    statement: str
    status: ClaimStatus = ClaimStatus.UNVERIFIED
    evidence_ids: List[str] = Field(default_factory=list)
    citation_ids: List[str] = Field(default_factory=list)
    verification_ids: List[str] = Field(default_factory=list)
    limitations: List[str] = Field(default_factory=list)
    created_at: str = Field(default_factory=utc_now)
    updated_at: str = Field(default_factory=utc_now)


class CitationCard(BaseModel):
    id: str = Field(default_factory=lambda: f"cite-{uuid4().hex[:10]}")
    title: str
    year: int
    source_type: str
    status: str = "unverified"
    authors: List[str] = Field(default_factory=list)
    venue: Optional[str] = None
    doi: Optional[str] = None
    url: Optional[str] = None
    used_for: List[str] = Field(default_factory=list)
    access_date: Optional[str] = None


class AuditEvent(BaseModel):
    id: str = Field(default_factory=lambda: f"audit-{uuid4().hex[:10]}")
    actor: str
    action: str
    target_type: str
    target_id: str
    result: str
    artifact: Optional[str] = None
    timestamp: str = Field(default_factory=utc_now)
    metadata: Dict[str, Any] = Field(default_factory=dict)
