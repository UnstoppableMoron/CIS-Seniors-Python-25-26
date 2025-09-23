'''
Program: fitnessTracker.py
Author: Owen Baker
Class: CIS Seniors
Date: 9/23/2025

Create a program that:
    Collects the user's personal fitness information using
    Stores all data in appropriately named variables
    Performs calculations on the collected data
    Displays a formatted fitness report using

Specific Data to Collect:
    User's name
    Age (integer)
    Weight in pounds (float)
    Height in inches (integer)
    Weekly exercise hours (float)
    Fitness goal (string)

Calculations to Perform:
    Calculate BMI (Body Mass Index)
    Determine daily exercise minutes
    Calculate calories burned per week (estimate)

BMI Formula:
BMI = (weight_in_pounds / (height_in_inches²)) × 703
'''
print("Welcome to your personal fitness tracker!" + "\n")

# Collect user data
userName = input("Enter your first and last name: ")
userAge = int(input("Enter your age: "))
userWeight = float(input("Enter your weight in pounds: "))
userHeight = int(input("Enter your height in inches: "))
weeklyExercise = float(input("How many hours do you exercise per week? "))
fitnessGoal = str(input("What is your main fitness goal? "))
print("\n")

# Compute fitness data
bmi = (userWeight / (userHeight * userHeight)) * 703
dailyExercise = (weeklyExercise * 60) / 7
caloriesBurned = (weeklyExercise * 300)

# Print personal information
print("=" * 25)
print("Name: " + userName)
print("Age:" , userAge)
print("Weight:" , userWeight)
print("Height:" , userHeight)
print("\n")

# Print fitness data
print("=" * 25)
print("Your BMI is" , bmi)
print("Your daily exercise in minutes is" , dailyExercise)
print("You burned" , caloriesBurned , "calories this week.")
print("Fitness goal: " + fitnessGoal)