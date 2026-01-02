# src/plugins/google_keep.py

from dataclasses import dataclass, field
from typing import List, Dict, Any

# =================================================================
# Placeholder Data Structures
# (These will be moved to a central 'src/models.py' or similar later)
# =================================================================

@dataclass
class Entry:
    """Represents a single piece of data processed by the pipeline."""
    id: str
    source: str
    content: str
    vector: List[float] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


class BasePlugin:
    """Base class for all plugins."""
    def __init__(self, config: Dict[str, Any]):
        self.config = config

    def execute(self, *args, **kwargs):
        raise NotImplementedError("Plugin must implement the 'execute' method.")


class SubscriptionPlugin(BasePlugin):
    """Base class for plugins that subscribe to data sources."""
    def execute(self) -> List[Entry]:
        """Subscribes to a data source and returns a list of entries."""
        raise NotImplementedError(
            "SubscriptionPlugin must implement 'execute' and return a List[Entry]."
        )


# =================================================================
# Plugin Implementation
# =================================================================

class Plugin(SubscriptionPlugin):
    """
    A subscription plugin to fetch data from Google Keep Takeout JSON files.
    The class must be named 'Plugin'.
    """
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.source_path = self.config.get("path")
        if not self.source_path:
            raise ValueError("Config for GoogleKeep plugin must contain a 'path'.")

    def execute(self) -> List[Entry]:
        """
        Reads JSON files from the specified Google Keep takeout directory,
        parses them, and returns them as a list of Entry objects.
        """
        print(f"Executing GoogleKeepPlugin: Reading from '{self.source_path}'...")

        # In the actual implementation, this method will:
        # 1. Find all .json files in `self.source_path`.
        # 2. Read and parse each JSON file.
        # 3. Transform the JSON content into an `Entry` object.
        # 4. Collect and return the list of `Entry` objects.

        # For this skeleton, we'll just return an empty list.
        return []
