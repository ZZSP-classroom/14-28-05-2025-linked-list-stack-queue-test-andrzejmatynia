import unittest
from library_reservation import Queue, Reservation

class TestReservationSystem(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()
        self.reservation1 = Reservation("a", "1234")
        self.reservation2 = Reservation("b", "4321")

    def test_enqueue(self):
        self.queue.enqueue(self.reservation1)
        self.queue.enqueue(self.reservation2)
        self.assertEqual(self.queue.peek().user_name, "a")

    def test_dequeue(self):
        self.queue.enqueue(self.reservation1)
        self.queue.enqueue(self.reservation2)
        dequeued = self.queue.dequeue()
        self.assertEqual(dequeued.user_name, "a")
        self.assertEqual(self.queue.peek().user_name, "b")

if __name__ == "__main__":
    unittest.main()