from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

from core.action import Action


def list_files(directory: str = ".") -> List[str]:
    return sorted([p.name for p in Path(directory).iterdir()])


def read_file(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def search_in_file(path: str, query: str) -> List[Dict[str, Any]]:
    results: List[Dict[str, Any]] = []
    for i, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), start=1):
        if query in line:
            results.append({"line_no": i, "line": line})
    return results

def terminate(message: str) -> str:
        """Terminate the agent loop and provide a summary message."""
        return message


LIST_FILES = Action(
    name="list_files",
    function=list_files,
    description="List files in a directory.",
    parameters={
        "type": "object",
        "properties": {"directory": {"type": "string", "default": "."}},
        "required": [],
    },
    terminal=False
)

READ_FILE = Action(
    name="read_file",
    function=read_file,
    description="Read a text file and return its contents.",
    parameters={
        "type": "object",
        "properties": {"path": {"type": "string"}},
        "required": ["path"],
    },
    terminal=False
)

SEARCH_IN_FILE = Action(
    name="search_in_file",
    function=search_in_file,
    description="Search for a substring in a file and return matching lines with line numbers.",
    parameters={
        "type": "object",
        "properties": {"path": {"type": "string"}, "query": {"type": "string"}},
        "required": ["path", "query"],
    },
    terminal=False
)
