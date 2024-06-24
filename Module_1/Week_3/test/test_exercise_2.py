
import unittest
from Module_1.Week_3.Implement_of_Ward import Student, Teacher, Doctor, Ward
from io import StringIO
import sys

class TestWard(unittest.TestCase):
    def setUp(self):
        self.student1 = Student(name="studentA", yob=2010, grade="7")
        self.teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
        self.teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
        self.doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
        self.doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
        self.ward1 = Ward(name="Ward1")
        self.ward1.add_person(self.student1)
        self.ward1.add_person(self.teacher1)
        self.ward1.add_person(self.teacher2)
        self.ward1.add_person(self.doctor1)
        self.ward1.add_person(self.doctor2)

    def test_describe_student(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.student1.describe()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Student - Name: studentA - YoB: 2010 - Grade: 7")

    def test_describe_teacher(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.teacher1.describe()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Teacher - Name: teacherA - YoB: 1969 - Subject: Math")

    def test_describe_doctor(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.doctor1.describe()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Doctor - Name: doctorA - YoB: 1945 - Specialist: Endocrinologists")

    def test_describe_ward(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.ward1.describe()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Ward name: Ward1\n"
                                                            "Student - Name: studentA - YoB: 2010 - Grade: 7\n"
                                                            "Teacher - Name: teacherA - YoB: 1969 - Subject: Math\n"
                                                            "Teacher - Name: teacherB - YoB: 1995 - Subject: History\n"
                                                            "Doctor - Name: doctorA - YoB: 1945 - Specialist: Endocrinologists\n"
                                                            "Doctor - Name: doctorB - YoB: 1975 - Specialist: Cardiologists")

    def test_count_doctor(self):
        self.assertEqual(self.ward1.count_doctor(), 2)

    def test_sort_age(self):
        self.ward1.sort_age()
        self.assertEqual([person.yob for person in self.ward1.people],
                         [1945, 1969, 1975, 1995, 2010])

    def test_compute_average(self):
        self.assertAlmostEqual(self.ward1.compute_average(), 1982.0)


if __name__ == "__main__":
    unittest.main()