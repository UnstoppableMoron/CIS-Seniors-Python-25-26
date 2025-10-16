'''
Program: carpetSales.py
Author: Owen Baker
Class: CIS Seniors
Date: 10/16/2025

Program Specifications: Write a program to calculate the cost of hosting three pizza parties on Friday, Saturday and Sunday. Read from input the number of people attending, the average number of slices per person and the cost of one pizza. Dollar values are output with two decimals. For example, print(f"Cost: ${cost:.2f}"). 
'''

import math

SLICES = 8
TAX_RATE = 0.07
DELIVERY = 0.2

# Inputs

num_people = int(input("Enter the number of people attending: "))
avg_slices = float(input("Enter the average number of slices per person: "))
pizza_cost = float(input("Enter the cost of the pizza: "))

# Calculate cost
pizzas = (avg_slices * num_people) / SLICES
num_pizzas = math.ceil(pizzas)
cost = num_pizzas * pizza_cost
tax = cost * TAX_RATE
delivery_fee = (cost + tax) * DELIVERY
total_cost = cost + tax + delivery_fee
weekend_total = total_cost

# Output the bill summary
print("\nFriday Night Party")
print(f"{num_pizzas} Pizzas: ${cost:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Delivery: ${delivery_fee:.2f}")
print(f"Total: ${total_cost:.2f}")

print("\n\n")
# Input info for Saturday party
num_people = int(input("Enter the number of people attending: "))
avg_slices = float(input("Enter the average number of slices per person: "))
pizza_cost = float(input("Enter the cost of the pizza: "))

# Calculate cost
pizzas = (avg_slices * num_people) / SLICES
num_pizzas = math.ceil(pizzas)
cost = num_pizzas * pizza_cost
tax = cost * TAX_RATE
delivery_fee = (cost + tax) * DELIVERY
total_cost = cost + tax + delivery_fee
weekend_total += total_cost

# Output bill summary
print("\nSaturday Night Party")
print(f"{num_pizzas} Pizzas: ${cost:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Delivery: ${delivery_fee:.2f}")
print(f"Total: ${total_cost:.2f}")

print("\n\n")
# Input info for Sunday party
num_people = int(input("Enter the number of people attending: "))
avg_slices = float(input("Enter the average number of slices per person: "))
pizza_cost = float(input("Enter the cost of the pizza: "))

# Calculate cost
pizzas = (avg_slices * num_people) / SLICES
num_pizzas = math.ceil(pizzas)
cost = num_pizzas * pizza_cost
tax = cost * TAX_RATE
delivery_fee = (cost + tax) * DELIVERY
total_cost = cost + tax + delivery_fee
weekend_total += total_cost

# Output bill summary
print("\nSunday Night Party")
print(f"{num_pizzas} Pizzas: ${cost:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Delivery: ${delivery_fee:.2f}")
print(f"Total: ${total_cost:.2f}")

print("\n\n")
# Print out a weekend total
print(f"Weekend total: ${weekend_total:.2f}")