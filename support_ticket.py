class Ticket:
    def __init__(self, ticket_id, issue_description):
        self.ticket_id = ticket_id
        self.issue_description = issue_description

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, ticket):
        self.queue.append(ticket)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, ticket):
        self.stack.append(ticket)
    
    def pop(self):
        return self.stack.pop() if self.stack else None

q = Queue()
s = Stack()

ticket1 = Ticket(1, "Issue1")
ticket2 = Ticket(2, "Issue2")

q.enqueue(ticket1)
q.enqueue(ticket2)

s.push(q.dequeue())
print(s.pop().issue_description)