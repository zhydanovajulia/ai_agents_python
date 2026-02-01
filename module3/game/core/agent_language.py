from __future__ import annotations
from typing import List
from module3.game.core.environment import Environment
from .action import Action
from .goal import Goal
from .memory import Memory
from .prompt import Prompt


class AgentLanguage:
    def __init__(self):
        pass

    def construct_prompt(self,
                         actions: List[Action],
                         environment: Environment,
                         goals: List[Goal],
                         memory: Memory) -> Prompt:
        raise NotImplementedError("Subclasses must implement this method")


    def parse_response(self, response: str) -> dict:
        raise NotImplementedError("Subclasses must implement this method")
