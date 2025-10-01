'''
Program: gradeTracker.py
Author: Owen Baker
Class: CIS Seniors
Date: 10/1/2025
'''

print("\n===== Grade Tracker =====")

students = int(input("How many students are in your class? "))

print("\nPlease enter student information: ")
print("----------------------------------------------")

nameLst = []
scoreLst = []

# Gather student information

for student in range(1, students + 1):
    print("Student #" , student , ":")
    name = str(input("  Enter student's name: "))
    score = int(input("  Enter test score (0-100): "))
    nameLst.append(name)
    scoreLst.append(name)

# Grading results and statistics

print("\n===== Grading Results =====")
print("Class Summary: ")
print("  Total Students:" , students)
pointTotal = sum(scoreLst)
print("Total Points:" , pointTotal)