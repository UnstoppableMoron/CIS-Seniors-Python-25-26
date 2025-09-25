'''
Program: quizScorer.py
Author: Owen Baker
Class: CIS Seniors
Date: 9/25/2025

Project Requirements:
    Ask for the student's name
    Ask how many quiz questions there are (5-10)
    Use a for loop to ask for each answer (True/False or 1/0)
    Use a for loop to ask for each correct answer
    Calculate and display:
    Total correct answers (using +=)
    Quiz percentage
    Pass/Fail status (70% to pass)
'''
print("=== QUIZ SCORER ===")
print("This program will score a 5-10 question true/false quiz.")
studentName = input("What is the student's name? ")
questions = int(input("How many quiz questions are there? (5-10) "))
totalScore = 0

lst = []
print("Enter student's answers, 1 for true, 0 for false. ")
for question in range(1, questions + 1):
    answer = int(input("Question " + str(question) + ": "))
    lst.append(answer)

correctLst = []
print("Enter the correct answers., 1 for true, 0 for false. ")
for question in range(1, questions + 1):
    correctAnswer = int(input("Question " + str(question) + ": "))
    correctLst.append(correctAnswer)

if answer == correctAnswer:
    print("Question " + str(question) + " Correct")
else:
    print("Question " + str(question) + " Incorrect")