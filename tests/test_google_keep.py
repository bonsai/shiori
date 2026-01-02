# tests/test_google_keep.py

import unittest
import sys
import os

# Add the 'src' directory to the Python path to allow importing the plugin
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from plugins.google_keep import Plugin as GoogleKeepPlugin

class TestGoogleKeepPlugin(unittest.TestCase):
    """
    Unit tests for the GoogleKeep subscription plugin.
    """

    def test_plugin_initialization(self):
        """
        Tests if the plugin can be initialized correctly.
        """
        # Define a sample config, similar to what would be in rag.yaml
        config = {
            "source_type": "takeout_json",
            "path": "/fake/path/to/takeout/keep/"
        }

        # Try to instantiate the plugin
        try:
            plugin = GoogleKeepPlugin(config)
            # Check if the path is correctly stored in the instance
            self.assertEqual(plugin.source_path, config["path"])
        except Exception as e:
            self.fail(f"Plugin initialization failed with an unexpected error: {e}")

    def test_plugin_execution_returns_list(self):
        """
        Tests if the execute method returns a list, even if it's empty for now.
        """
        config = {"path": "/fake/path"}
        plugin = GoogleKeepPlugin(config)
        result = plugin.execute()
        self.assertIsInstance(result, list, "The execute method should return a list.")

if __name__ == '__main__':
    unittest.main()
