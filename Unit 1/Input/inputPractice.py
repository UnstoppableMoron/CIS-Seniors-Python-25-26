'''
Filename: inputPractice.py
Author: Owen Baker
Class: CIS Seniors
Date: 9/19/2025

Ask:
First Name
Last Name
Favorite Color
First Number
Second Number
Favorite TV Show
Favorite Movie
Favorite Song
Favorite Food

- Write out a paragraph outlining the user data using variables. Using the first and
    second numbers, create 3 separate math equations, and print out the values
    from the expressions.
'''

first_name = input("Enter your first name. ")
last_name = input("Enter your last name. ")
favorite_color = input("What is your favorite color? ")
first_number = input("Enter a number. ")
second_number = input("Enter another number. ")
favorite_show = input("What is your favorite TV show? ")
favorite_movie = input("What is your favorite movie? ")
favorite_song = input("What is your favorite song? ")
favorite_food = input("What is your favorite food? ")

print("Your name is " + first_name , last_name , ". Your favorite color is " + favorite_color + ". Your favorite show is " + favorite_show + ". Your favorite movie is " + favorite_movie + ". Your favorite song is " + favorite_song + ". Your favorite food is " + favorite_food + ".")

sum = int(first_number) + int(second_number)
product = int(first_number) * int(second_number)
quotient = int(first_number) / int(second_number)
print(sum)
print(product)
print(quotient)