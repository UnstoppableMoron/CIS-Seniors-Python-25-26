'''
Program: luckyNumber.py
Author: Owen Baker
Class: CIS Seniors
Date: 10/2/2025
'''

import random

# Game statistics
totalRounds = 0
totalWins = 0
totalGuesses = 0

print("=" * 50)
print("  WELCOME TO THE LUCKY NUMBER GUESSING GAME!")
print("=" * 50)
print()

# Main game loop - play multiple rounds
while True:
    # Generate random lucky number
    luckyNumber = random.randint(1, 50)

    # Set maximum attempts
    maxAttempts = 7

    # Initialize attempt counter
    attempts = 0

    totalRounds += 1
    print(f"\nRound {totalRounds}")
    print("I'm thinking of a lucky number between 1 and 50...")
    print(f"You have {maxAttempts} attempts to guess it!")
    print()

    # Guessing loop
    while attempts < maxAttempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid number between 1 and 50.")
            continue

        if guess < 1 or guess > 50:
            print("Your guess is out of bounds. Please choose between 1 and 50.")
            continue

        attempts += 1
        totalGuesses += 1

        if guess == luckyNumber:
            print(f"Correct! The lucky number was {luckyNumber}. You guessed it in {attempts} attempts.")
            totalWins += 1
            break
        elif guess < luckyNumber:
            print("Too low.")
        else:
            print("Too high.")

    # If loop ends without a correct guess
    if guess != luckyNumber:
        print(f"Out of attempts. The lucky number was {luckyNumber}.")

    # Round summary
    print(f"Round {totalRounds} complete. Attempts used: {attempts}")
    if guess == luckyNumber:
        print("Correct! The lucky number was", luckyNumber)
    else:
        print("You lost this round.")

    # Ask to play again
    playAgain = input("\nDo you want to play another round? (yes/no): ").strip().lower()
    if playAgain not in ("yes", "y"):
        break

# Display final statistics
averageGuesses = totalGuesses / totalRounds if totalRounds > 0 else 0
print("\n" + "=" * 50)
print("GAME OVER - FINAL STATISTICS")
print("=" * 50)
print(f"Total Rounds Played: {totalRounds}")
print(f"Total Wins: {totalWins}")
print(f"Average Guesses per Round: {averageGuesses:.2f}")
print("=" * 50)
print("Thanks for playing!")