# tests/test_llm_metadata_enricher.py

import unittest
import sys
import os

# Add 'src' to path to allow direct import of plugins
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from plugins.base import Entry
from plugins.llm_metadata_enricher import Plugin as MetadataEnricherPlugin

class TestLlmMetadataEnricherPlugin(unittest.TestCase):
    """
    Unit tests for the LLMMetadataEnricherPlugin filter plugin.
    """

    def test_metadata_enrichment_mock(self):
        """
        Tests that the plugin correctly adds new metadata to an entry
        without removing existing metadata.
        """
        # 1. Create a sample entry with some pre-existing metadata
        sample_entry = Entry(
            id="test_id_456",
            source="test_source",
            content="This is some content to analyze for enrichment.",
            metadata={"original_key": "original_value"}
        )

        # 2. Instantiate the plugin
        config = {"model": "gemini-1.5-flash"}
        plugin = MetadataEnricherPlugin(config)

        # 3. Execute the plugin with the sample entry
        processed_entries = list(plugin.execute(iter([sample_entry])))

        # 4. Check that one entry was returned
        self.assertEqual(len(processed_entries), 1)
        processed_entry = processed_entries[0]

        # 5. Verify the new metadata was added
        self.assertIn("llm_tags", processed_entry.metadata)
        self.assertEqual(processed_entry.metadata["llm_tags"], ["mock_tag", "test"])

        self.assertIn("llm_intent", processed_entry.metadata)
        self.assertEqual(processed_entry.metadata["llm_intent"], "mock_intent_for_testing")

        # 6. Verify that the original metadata is still present
        self.assertIn("original_key", processed_entry.metadata)
        self.assertEqual(processed_entry.metadata["original_key"], "original_value")

        # 7. Verify other fields were not changed
        self.assertEqual(processed_entry.id, sample_entry.id)
        self.assertEqual(processed_entry.content, sample_entry.content)


if __name__ == '__main__':
    unittest.main()
