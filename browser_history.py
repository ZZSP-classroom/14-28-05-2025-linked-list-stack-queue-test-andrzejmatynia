class Stack:
    def __init__(self):
        self.stack = []

    def push(self, url):
        self.stack.append(url)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def peek(self):
        return self.stack[-1] if self.stack else None

history = Stack()
history.push("link1")
history.push("link2")
print(history.peek())
history.pop()
print(history.peek())