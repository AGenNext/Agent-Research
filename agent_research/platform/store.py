import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Type, TypeVar

from pydantic import BaseModel

from agent_research.platform.models import AuditEvent

T = TypeVar("T", bound=BaseModel)


class ResearchStore:
    """Filesystem-backed state store for local Agent-Research runs.

    This is intentionally simple: every platform primitive is stored as JSON under
    a predictable directory, while audit events are appended to JSONL. It gives us
    an executable platform now and leaves room for SurrealDB later.
    """

    def __init__(self, root: str = ".agent-research"):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        for name in [
            "workspaces",
            "objectives",
            "flows",
            "evidence",
            "claims",
            "citations",
            "verifications",
            "reviews",
            "releases",
            "artifacts",
        ]:
            (self.root / name).mkdir(parents=True, exist_ok=True)

    def path_for(self, collection: str, item_id: str) -> Path:
        return self.root / collection / f"{item_id}.json"

    def save(self, collection: str, item: BaseModel) -> str:
        path = self.path_for(collection, getattr(item, "id"))
        with open(path, "w", encoding="utf-8") as f:
            json.dump(item.model_dump(mode="json"), f, indent=2)
        return str(path)

    def load(self, collection: str, item_id: str, model: Type[T]) -> T:
        path = self.path_for(collection, item_id)
        if not path.exists():
            raise FileNotFoundError(f"No {collection} item found for id {item_id}")
        with open(path, "r", encoding="utf-8") as f:
            payload = json.load(f)
        return model(**payload)

    def list(self, collection: str, model: Type[T]) -> List[T]:
        items = []
        for path in sorted((self.root / collection).glob("*.json")):
            with open(path, "r", encoding="utf-8") as f:
                items.append(model(**json.load(f)))
        return items

    def append_audit(self, event: AuditEvent) -> str:
        path = self.root / "audit.jsonl"
        with open(path, "a", encoding="utf-8") as f:
            f.write(event.model_dump_json() + "\n")
        return str(path)

    def write_artifact(self, relative_path: str, content: str) -> str:
        path = self.root / "artifacts" / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return str(path)

    def read_audit(self) -> Iterable[Dict[str, Any]]:
        path = self.root / "audit.jsonl"
        if not path.exists():
            return []
        rows = []
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    rows.append(json.loads(line))
        return rows
