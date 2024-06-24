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
