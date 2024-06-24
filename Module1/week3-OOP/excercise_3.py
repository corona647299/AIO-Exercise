class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        return len(self.stack) == self.capacity
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack.pop()
    
    def push(self, value):
        if self.is_full():
            raise Exception("Stack is full")
        self.stack.append(value)
    
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[-1]


stack = Stack(5)  


stack.push(1)
stack.push(2)
stack.push(3)


print("Top element:", stack.top())

print("Popped element:", stack.pop())

print("Is stack empty?", stack.is_empty())

stack.push(4)
print("Top element after push:", stack.top())

print("Is stack full?", stack.is_full())

stack.push(5)
stack.push(6) 
