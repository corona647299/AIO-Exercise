class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self.queue.pop(0)

    def enqueue(self, value):
        if self.is_full():
            raise ValueError("Queue is full")
        self.queue.append(value)

    def front(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self.queue[0]


queue = MyQueue(5)

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Front element:", queue.front())

print("Dequeued element:", queue.dequeue())

print("Is queue empty?", queue.is_empty())

queue.enqueue(4)
print("Front element after enqueue:", queue.front())

print("Is queue full?", queue.is_full())

queue.enqueue(5)
queue.enqueue(6)
