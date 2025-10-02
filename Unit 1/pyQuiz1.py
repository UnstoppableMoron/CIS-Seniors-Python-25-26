'''
Program: pyQuiz.py
Author: Owen Baker
Class: CIS Seniors
Date: 10/2/2025
'''

# Question 1
print("Question 1:")
number = -1
for count in range(-1, 5):
    number = number + 1
    print("\n", number)

# Question 2
print("\n\n\n")
print("Question 2:")
number = 2
for count in range(2, 8):
    number = number + 1
    print("\n", number)

# Question 3
print("\n\n\n")
print("Question 3:")
number = -2
for count in range(-2, 4):
    number = number + 2
    print("\n", number)

# Question 4
print("\n\n\n")
print("Question 4:")
number = 11
for count in range(0, 11):
    number = number - 1
    print("\n", number)

# Question 5
print("\n\n\n")
print("Question 5:")
number = 0
for count in range(0, 5):
    number = number + 1
    product = number * 5
    print("\n5 x", number, "=" , product)

# Question 6
print("\n\n\n")
print("Question 6:")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else: 
    print("You are a minor.")

# Question 7
print("\n\n\n")
print("Question 7:")
for number in range(1, 11):
    if number % 2 == 0:
        print(f"{number}: Even")
    else:
        print(f"{number}: Odd")

# Question 8
print("\n\n\n")
print("Question 8:")
number = 25
for count in range(0, 5):
    number = number - 5
    print("\nCountdown:", number)

# Question 9
print("\n\n\n")
print("Question 9:")
number = 0
for count in range(0, 6):
    number = number + 1
    if number < 4:
        print("Number", number, "is small.")
    else:
        print("Number", number, "is large.")

# Question 10
print("\n\n\n")
print("Question 10")
userNumber = input("Enter a number: ")
number = int(userNumber)
for i in range(1, number + 1, 2):
    if i < 5:
        print(f"Low: {i}")
    else:
        print(f"High: {i}")

# Bonus question
print("\n\n\n")
print("Bonus Question:")
number = 18

for count in range(0, 6):
    number = number - 3
    if number == 0:
        print("Blastoff!")
    else:
        print(number)