class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = []
        
    def is_empty(self):
        return len(self.arr) == 0

    def is_full(self):
        return len(self.arr) == self.capacity

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack is full")
        self.arr.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.arr.pop()

    def top(self):
        if self.is_empty():
            raise IndexError("Top from empty stack")
        return self.arr[-1]

# Example usage
stack1 = Stack(capacity=5)

stack1.push(1)
stack1.push(2)
print(stack1.is_full())  # False

print(stack1.top())  # 2

print(stack1.pop())  # 2

print(stack1.top())  # 1

print(stack1.pop())  # 1

print(stack1.is_empty())  # True
