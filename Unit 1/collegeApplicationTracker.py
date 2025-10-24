'''
Program: collegeApplicationTracker.py
Author: Owen Baker
Class: CIS Seniors
Date: 10/24/2025
'''

# Import statements
import math
# Constants (ALL_CAPS naming convention)
APPLICATION_FEE = 75.00
AVG_ACCEPTANCE_RATE = 55.0
MAX_IDEAL_DISTANCE = 500
# Welcome message
print("=" * 50)
print("COLLEGE APPLICATION TRACKER")
print("=" * 50)

# Variables for student info
studentName = input("What is your name? ")
print("Welcome, " + studentName + "! Let's track your college applications!")
print("Please enter information for 3 colleges you're considering: ")

# Lists to store college data
college_one = []
college_two = []
college_three = []

# Data collection loop or individual inputs
print("----- College #1 -----")
college_name1 = input("College name: ")
location1 = input("College location (City, State): ")
annual_tutition1 = int(input("Annual tutition ($): "))
distance1 = int(input("Distance from home: "))
acceptance_rate1 = int(input("Acceptance rate: "))
total_tuition1 = annual_tutition1 * 4

college_one = [college_name1, location1, annual_tutition1, distance1, acceptance_rate1]

print("\n")
print("----- College #2 -----")
college_name2 = input("College name: ")
location2 = input("College location (City, State): ")
annual_tutition2 = int(input("Annual tutition ($): "))
distance2 = int(input("Distance from home: "))
acceptance_rate2 = int(input("Acceptance rate: "))
total_tuition2 = annual_tutition2 * 4

college_two = [college_name2, location2, annual_tutition2, distance2, acceptance_rate2]

print("\n")
print("----- College #3 -----")
college_name3 = input("College name: ")
location3 = input("College location (City, State): ")
annual_tutition3 = int(input("Annual tutition ($): "))
distance3 = int(input("Distance from home: "))
acceptance_rate3 = int(input("Acceptance rate: "))
total_tuition3 = annual_tutition3 * 4

college_two = [college_name3, location3, annual_tutition3, distance3, acceptance_rate3]


# Print college data

# College 1 data
print("----- College #1 -----")
print("College 1: " + college_name1)
print("Location: " + location1)
print("Annual tutition:" , annual_tutition1)
print("Distance in miles:" , distance1)
print("Acceptance rate:" , acceptance_rate1)
print("Four year total cost:", total_tuition1)

# College 2 data
print("----- College #2 -----")
print("College 2: " + college_name2)
print("Location: " + location2)
print("Annual tutition:" , annual_tutition2)
print("Distance in miles:" , distance2)
print("Acceptance rate:" , acceptance_rate2)
print("Four year total cost:", total_tuition2)

# College 3 data
print("----- College #3 -----")
print("College 3: " + college_name3)
print("Location: " + location3)
print("Annual tutition:" , annual_tutition3)
print("Distance in miles:" , distance3)
print("Acceptance rate:" , acceptance_rate3)
print("Four year total cost:", total_tuition3)

# Calculations using Math module
print("=" * 50)

print("=" * 50)

# Summary report with f-strings
# Your code here