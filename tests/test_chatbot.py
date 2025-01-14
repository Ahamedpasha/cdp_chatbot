import unittest
from chatbot.search import search_documentation

class TestChatbot(unittest.TestCase):
    def setUp(self):
        self.documentation_data = {
            "Segment": {
                "Set up a new source": "Go to your workspace, click 'Add Source', and choose your integration."
            }
        }
    
    def test_search_documentation(self):
        result = search_documentation("set up a new source", self.documentation_data)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], "Segment")
        self.assertEqual(result[0][1], "Set up a new source")
        self.assertIn("Go to your workspace", result[0][2])

if __name__ == "__main__":
    unittest.main()
