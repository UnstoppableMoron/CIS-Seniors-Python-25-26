'''
Program: investmentBook.py
Author: Owen Baker
Compute an investment report.
1. The inputs are:
    - starting investment amount
    - number of years
    - interest rate (an integer percent)

2. The report is displayed in tabular form with a header

3. Computations and outputs:
    - for each year of the investment:
        - compute the interest and add it to the investment
        - print a formatted row of results for that year

4. The ending investment and interest you have paid in total are also displayed
'''
print("\n\n")
print("=" * 40)
print("\n\nMy Investment Tracker")
print("=" * 40)

# Accept the inputs
startBalance = float(input("Enter the investment amount: "))
years = int(input("Enter the number of years: "))
rate = int(input("Enter the interest rate as a percentage: "))

# Convert the rate to a decimal number
rate = rate / 100

# Initialize the accumaltor for the interest
totalInterest = 0.0

# Display the header for the table

print("%4s%18s%10s%16s" % ("Year", "Starting balance", "Interest", "Ending balance"))

# Compute and display the results for each year
for year in range(1, years + 1):
    interest = startBalance * rate
    endBalance = startBalance + interest
    print("%4d%18.2f%10.2f%16.2f" % (year, startBalance, interest, endBalance))
    startBalance = endBalance
    totalInterest += interest

# Display the totals for the period
print("Ending balance: $%0.2f" % endBalance)
print("Total interest earned: $%0.2f" % totalInterest)