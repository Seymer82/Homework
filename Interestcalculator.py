# File Name: <Homework1.py>
# Author: <Spencer Seymer>
# Version: <09/15/2023>
# Section: CC 111 Online
# Description: <Building an interest calculator to calculate compound interest after 1, 5, 10, 25, 40 and x amount of years,
# as well as calculating how much the individual may spend per year for a given amount of years, while in retirement







Savings = int(input("Please enter your current savings"))
Interest_rate = float(input("Enter the current interest rate"))
Years = int(input("How many years will you be saving?"))
Final_amount = Savings * (1 + Interest_rate) ** Years

# Interest calculated after 1 year
Years_1 = Savings * (1 + Interest_rate) ** 1

# Interest calculated after 5 years
Years_5 = Savings * (1 + Interest_rate) ** 5

# Interest calculated after 10 years
Years_10 = Savings * (1 + Interest_rate) ** 10

# Interest calculated after 25 years
Years_25 = Savings * (1 + Interest_rate) ** 25

# Interest calculated after 40 years
Years_40 = Savings * (1 + Interest_rate) ** 40

print (f"After 1 year, you will have ${Years_1:,.2f}")
print (f"After 5 years, you will have ${Years_5:,.2f}")
print (f"After 10 years, you will have ${Years_10:,.2f}")
print (f"After 25 years, you will have ${Years_25:,.2f}")
print (f"After 40 years, you will have ${Years_40:,.2f}")
print (f"After {Years} years, you will have ${Final_amount:,.2f}")

Retirement_spending = int(input("How much will you be spending yearly in retirement?"))

# Initialize variables for retirement
Years_in_retirement = 0
Amount_left_over = Final_amount

# Calculate how long the savings will last in retirement

while Amount_left_over >= Retirement_spending:
    Amount_left_over -= Retirement_spending
    Years_in_retirement += 1

print(f"You will be able to spend ${Retirement_spending:,.2f} per year for {Years_in_retirement} years.")
print(f"You will have ${Amount_left_over:,.2f} left over after {Years_in_retirement} years.")
