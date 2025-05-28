import unittest
from browser_history import Stack

class TestBrowserHistoryManagement(unittest.TestCase):
    def setUp(self):
        self.history = Stack()

    def test_push(self):
        self.history.push("link1")
        self.assertEqual(self.history.peek(), "link1")

    def test_pop(self):
        self.history.push("link1")
        self.history.push("link2")
        popped_link = self.history.pop()
        self.assertEqual(popped_link, "link2")
        self.assertEqual(self.history.peek(), "link1")


if __name__ == "__main__":
    unittest.main()