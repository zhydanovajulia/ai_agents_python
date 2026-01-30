from __future__ import annotations

from typing import Any, Callable, Dict


class Action:
    def __init__(
        self,
        name: str,
        function: Callable[..., Any],
        description: str,
        parameters: Dict,
        terminal: bool = False,
    ):
        self.name = name
        self.function = function
        self.description = description
        self.terminal = terminal
        self.parameters = parameters

    def execute(self, **args) -> Any:
        """Execute the action's function"""
        return self.function(**args)
