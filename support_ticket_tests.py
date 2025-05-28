import unittest
from support_ticket import Queue, Ticket, Stack

class TestSupportTicket(unittest.TestCase):
    def setUp(self):
        self.q = Queue()
        self.s = Stack()
        self.ticket1 = Ticket(1, "Issue1")
        self.ticket2 = Ticket(2, "Issue2")

    def test_enqueue_dequeue(self):
        self.q.enqueue(self.ticket1)
        self.q.enqueue(self.ticket2)
        self.assertEqual(self.q.dequeue().issue_description, "Issue1")

    def test_stack_pop(self):
        self.q.enqueue(self.ticket1)
        self.s.push(self.q.dequeue())
        self.assertEqual(self.s.pop().issue_description, "Issue1")


if __name__ == "__main__":
    unittest.main()