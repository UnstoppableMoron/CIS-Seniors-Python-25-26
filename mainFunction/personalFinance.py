"""
Personal Finance Manager
Program: personalFinance.py
Author: Owen Baker
Date: 11/18/2025

This program demonstrates proper Python program structure using a main() function and helper functions to coordinate program flow.
"""

def display_header():
    """
    Display the program header and welcome message

    This function has no parameters and returns nothing.
    It's purely for display purposes.
    """
    print("\n\n\n")
    print("=" * 50)
    print("            PERSONAL FINANCE MANAGER")
    print("            Plan Your College Budget!")
    print("=" * 50)


def get_user_name():
    """
    Get the user's name

    Returns:
        name (str): The user's name
    NOTE: We use a separate function for this to keep each function doing ONE specific task
    """
    name = input("What is your name? ")
    return name

def get_income():
    """
    Get and return the user's monthly income
    
    Returns:
        income (float): Monthly income in dollars

    NOTE: We convert to a float to handle decimal values and to enable mathmatical operations
    """
    print("\nEnter your monthly income: $", end="")
    income_str = input()
    income = float(income_str)
    return income

def get_expenses():
    """
    Collect all expense categories from the user
    
    Returns:
        expenses_dict (dict): Dictionary with expense categories
        total_expenses (float): Sum of all expenses

        NOTE: This function demonstrates collecting multiple related inputs and organizing them in a dictionary for easy access later
    """
    print("\n--- EXPENSE TRACKING ---")

    # Dictionary to store all expenses
    expenses = {}

    # Get each expense category
    print("Enter your monthly rent/housing cost: $", end="")
    expenses['Rent/Housing'] = float(input())

    print("Enter your food/groceries budget: $", end="")
    expenses['Food/Groceries'] = float(input())

    print("Enter your transportation costs: $", end="")
    expenses['Transportation'] = float(input())

    print("Enter your entertainment budget: $", end="")
    expenses['Entertainment'] = float(input())

    print("Enter your savings goal: $", end="")
    expenses['Savings'] = float(input())

    print("Emter miscellaneous expenses: $", end="")
    expenses['Miscellaneous'] = float(input())

    # Calculate total expenses
    total = sum(expenses.values())

    # Return both the dictionary and the total
    return expenses, total

def calculate_remaining(income, expenses):
    pass

def provide_feedback(remaining, income):
    pass

def display_summary(name, income, expenses_dict, total_expenses, remaining, feedback):
    pass

def main():
    """
    Main Function - coordinates the entire program

    Notice how main() reads like a story:
    1. Display header
    2. Get user information
    3. Get expenses
    4. Calculate results
    5. Get feedback
    6. Display summary
    7. Say goodbye

    Each step is one function call, making the logic easy to follow.
    """
    
    # Display welcome
    display_header()
    print("Welcome! Let's track your monthly finances.\n")

    # Get user information
    user_name = get_user_name()
    monthly_income = get_income()

    # Get expense information
    # NOTE: This function returns TWO values (tuple unpacking)
    expense_categories, total_categories = get_expenses() 

if __name__ == "__main__":
    main()