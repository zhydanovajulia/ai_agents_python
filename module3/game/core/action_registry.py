from __future__ import annotations
from typing import Any, Dict, List
from core.action import Action


class ActionRegistry:
    def __init__(self) -> None:
        self._actions: Dict[str, Action] = {}

    def register(self, action: Action) -> None:
        if action.name in self._actions:
            raise ValueError(f"Action '{action.name}' is already registered.")
        self._actions[action.name] = action

    def get(self, name: str) -> Action:
        if name not in self._actions:
            raise KeyError(f"Unknown action '{name}'. Registered: {list(self._actions.keys())}")
        return self._actions[name]

    def list(self) -> List[Action]:
        return list(self._actions.values())

    def execute(self, name: str, **args) -> Any:
        return self.get(name).execute(**args)
