from __future__ import annotations

from game.core.action_registry import ActionRegistry
from game.actions.filesystem_actions import LIST_FILES, READ_FILE, SEARCH_IN_FILE


def build_action_registry() -> ActionRegistry:
    registry = ActionRegistry()
    registry.register(LIST_FILES)
    registry.register(READ_FILE)
    registry.register(SEARCH_IN_FILE)
    return registry
