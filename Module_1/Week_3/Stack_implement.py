class Stack:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.list = []

    def is_empty(self):
        return len(self.list) == 0
    
    def is_full(self):
        return len(self.list) == self.capacity
    
    def pops(self):
        assert not self.is_empty(), "The list is empty"
        self.list.pop()
    
    def push(self, value: int):
        assert not self.is_full(), "The list is full"
        self.list.append(value)
    
    def top(self):
        return self.list[-1] if not self.is_empty() else None