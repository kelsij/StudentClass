"""
Program: test_employee.py
Author: Kelsi Jurik
Last date modified: 04/03/2023

This program is used to test the program student.py
"""

import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student1 = Student("Lovelace", "Ada", "Computer Science", 3.5)
        self.student2 = Student("Hopper", "Grace", "Mathematics", 3.9)

    def tearDown(self):
        pass

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student1.last_name, "Lovelace")
        self.assertEqual(self.student1.first_name, "Ada")
        self.assertEqual(self.student1.major, "Computer Science")
        self.assertEqual(self.student1.gpa, 3.5)

    def test_object_created_all_attributes(self):
        self.assertEqual(self.student2.last_name, "Hopper")
        self.assertEqual(self.student2.first_name, "Grace")
        self.assertEqual(self.student2.major, "Mathematics")
        self.assertEqual(self.student2.gpa, 3.9)

    def test_student_str(self):
        self.assertEqual(str(self.student1), "Lovelace, Ada has major Computer Science with gpa: 3.5")
        self.assertEqual(str(self.student2), "Hopper, Grace has major Mathematics with gpa: 3.9")

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(TypeError):
            student = Student(123, "Ada", "Computer Science", 3.5)

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(TypeError):
            student = Student("Lovelace", 123, "Computer Science", 3.5)

    def test_object_not_created_error_major(self):
        with self.assertRaises(TypeError):
            student = Student("Lovelace", "Ada", 123, 3.5)

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(TypeError):
            student = Student("Lovelace", "Ada", "Computer Science", "3.5")

        with self.assertRaises(ValueError):
            student = Student("Lovelace", "Ada", "Computer Science", 5.0)


if __name__ == '__main__':
    unittest.main()
