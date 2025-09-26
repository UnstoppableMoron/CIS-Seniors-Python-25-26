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
counter = 0
totalCorrect = 0

lst = []
print("Enter student's answers, 1 for true, 0 for false. ")
for counter in range(1, questions + 1):
    answer = list((input("Question " + str(counter) + ": ")))
    lst.append(answer)

correctLst = []
print("Enter the correct answers., 1 for true, 0 for false. ")
for counter in range(1, questions + 1):
    correctAnswer = list(input("Question " + str(counter) + ": "))
    correctLst.append(correctAnswer)

for counter in range(1, (questions + 1)):
    if lst[counter - 1] == correctLst[counter - 1]:
        print("Question " + str(counter) + ":" + " Correct")
        totalCorrect += 1 
    elif lst[counter - 1] != correctLst[counter - 1]:
        print("Question " + str(counter) + ":" + " Incorrect")

print("\n=== Quiz results for: " + studentName + " ===")
print("Correct answers:" , totalCorrect)
totalCorrect = (totalCorrect / questions) * 100
print("Quiz percentage:" , totalCorrect , "%")

if totalCorrect >= 70: 
    print("Final status: PASS")
else:
    print("Final status: FAIL")