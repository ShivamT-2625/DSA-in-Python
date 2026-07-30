#Implement Stack using Array 

class Stack:
    def __init__(self):
        self.stack = []
    def push(self,val):
        self.stack.append(val)
    
    def pop(self):
        if not self.stack:
            return "Stack is empty"
        else:
            return self.stack.pop()
    
    def peek(self):
        if not self.stack:
            return "Self is empty"
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
s = Stack()
s.push(67)
print(s.pop())
print(s.pop())

# Implement queue using list 

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        if not self.queue:
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if not self.queue:
            return "Queue is empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0