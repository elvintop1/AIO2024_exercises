from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str, yob: int) -> None:
        self.name = name
        self.yob = yob

    @abstractmethod
    def describe(self):
        pass

class Student(Person):
    def __init__(self, name: str, yob: int, grade: str) -> None:
        super(Student, self).__init__(name, yob)
        self.grade = grade
    
    def describe(self):
        print(f"Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}")
    
class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str) -> None:
        super().__init__(name, yob)
        self.subject = subject

    def describe(self) -> None:
        print(f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}")


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str) -> None:
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self) -> None:
        print(f"Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}")


class Ward():
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.people: list = []
    
    def add_person(self, person: Person) -> None:
        self.people.append(person)

    def describe(self):
        print(f"Ward name: {self.name}")
        for person in self.people:
            person.describe()
        
    def count_doctor(self):
        return sum(isinstance(person, Doctor) for person in self.people)

    def sort_age(self) -> None:
        self.people.sort(key=lambda person: person.yob)
    
    def compute_average(self) -> float:
        sum_of_year = sum(person.yob if isinstance(person, Teacher) else 0 for person in self.people)
        len_teacher = sum(isinstance(person, Teacher) for person in self.people)
        return float(sum_of_year / len_teacher)
