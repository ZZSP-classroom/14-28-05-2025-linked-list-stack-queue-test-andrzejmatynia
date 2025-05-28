class Reservation:
    def __init__(self, user_name, book_title):
        self.user_name = user_name
        self.book_title = book_title

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, reservation):
        self.queue.append(reservation)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None

    def peek(self):
        return self.queue[0] if self.queue else None


q = Queue()
q.enqueue(Reservation("a", "1234"))
print(q.peek().user_name)
q.dequeue()
print(q.peek())