"""
Program: test_employee.py
Author: Kelsi Jurik
Last date modified: 04/04/2023

This program creates the class Student and checks to make sure all required attributes exist in creation
"""


class Student:

    def __init__(self, lname, fname, major, gpa=0.0):
        if not isinstance(lname, str):
            raise TypeError("Last name must be a string")
        if not isinstance(fname, str):
            raise TypeError("First name must be a string")
        if not isinstance(major, str):
            raise TypeError("Major must be a string")
        if not isinstance(gpa, float) and not isinstance(gpa, int):
            raise TypeError("GPA must be a float or an integer")
        if gpa < 0.0 or gpa > 4.0:
            raise ValueError("GPA must be between 0.0 and 4.0")
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa
