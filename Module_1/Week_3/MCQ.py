# Question 2
import torch
import torch.nn as nn

class MySoftmax(nn.Module):
    def __init__(self):
        super(MySoftmax, self).__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        return exp_x / torch.sum(exp_x)

# Example usage
data = torch.Tensor([5, 2, 4])
my_softmax = MySoftmax()
output = my_softmax(data)
print(output)

# Question 4
data = torch.Tensor([1, 2, 300000000])
my_softmax = MySoftmax()
output = my_softmax(data)
print(output)


# Question 5
import torch
import torch.nn as nn

class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdim=True)
        x_exp = torch.exp(x - x_max.values)
        partition = x_exp.sum(dim=0, keepdim=True)
        return x_exp / partition

# Example usage
data = torch.Tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output = softmax_stable(data)
print(output)

#Question 9
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass

class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        print(f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}")

class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        print(f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}")

class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        print(f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}")

class Ward:
    def __init__(self, name: str):
        self.__name = name
        self.__list = list()

    def add_person(self, person: Person):
        self.__list.append(person)

    def describe(self):
        print(f"Ward Name: {self.__name}")
        for p in self.__list:
            p.describe()

    def count_doctor(self):
        return sum(1 for p in self.__list if isinstance(p, Doctor))

# Example usage
student1 = Student(name="studentA", yob=2010, grade="7")
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")

ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)

ward1.describe()
print(f"Number of doctors: {ward1.count_doctor()}")

# Question 11

class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_empty(self):
        return len(self.__stack) == 0

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack is full")
        self.__stack.append(value)

    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.__stack[-1]

# Example usage
stack1 = MyStack(capacity=5)
stack1.push(1)
assert stack1.is_full() == False
stack1.push(2)
print(stack1.top())  # 2


#Question 12

class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue is full")
        self.__queue.append(value)

# Example usage
queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False
queue1.enqueue(2)
print(queue1.is_full())  # False


class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue is full")
        self.__queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.__queue.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self.__queue[0]

# Example usage
queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False
queue1.enqueue(2)
print(queue1.front())  # 1


