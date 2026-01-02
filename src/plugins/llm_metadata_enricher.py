# src/plugins/llm_metadata_enricher.py

from typing import Dict, Any, Iterator
from .base import Entry, FilterPlugin

class Plugin(FilterPlugin):
    """
    A filter plugin to enrich entry metadata using an LLM.
    """
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.model = self.config.get("model", "gemini-1.5-flash")
        self.prompt = self.config.get("prompt", "Extract tags and intent.")

    def execute(self, entries: Iterator[Entry]) -> Iterator[Entry]:
        """
        Receives entries, enriches their metadata, and yields them back.
        This is a mock implementation.
        """
        print(f"Executing LLMMetadataEnricherPlugin (using mock for model '{self.model}')...")

        for entry in entries:
            # [MOCK] In a real implementation, this would call a generative AI API
            # with entry.content and the prompt to get structured metadata.
            print(f"  Enriching metadata for entry: {entry.id[:10]}...")

            # Create deterministic, dummy metadata for testing.
            dummy_metadata = {
                "llm_tags": ["mock_tag", "test"],
                "llm_intent": "mock_intent_for_testing"
            }

            # Merge the new metadata into the existing metadata dictionary
            entry.metadata.update(dummy_metadata)

            yield entry
