class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self, value):
        # Transfer all elements from stack1 to stack2
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())

        # Add the new element to the bottom of stack1
        self.stack1.append(value)
        
        # Transfer all elements back from stack2 to stack1
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
            
    def dequeue(self):
        # Check if the queue is empty
        if self.is_empty():
            return None
        else:
        # Remove and return the last element in stack1
        # which is the first element in the queue
            return self.stack1.pop()

    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0