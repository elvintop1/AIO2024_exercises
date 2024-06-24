class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = []
        
    def is_empty(self):
        return len(self.arr) == 0

    def is_full(self):
        return len(self.arr) == self.capacity

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue is full")
        self.arr.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.arr.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self.arr[0]

# Example usage
queue1 = Queue(capacity=5)

queue1.enqueue(1)
queue1.enqueue(2)
print(queue1.is_full())  # False

print(queue1.front())  # 1

print(queue1.dequeue())  # 1

print(queue1.front())  # 2

print(queue1.dequeue())  # 2

print(queue1.is_empty())  # True
