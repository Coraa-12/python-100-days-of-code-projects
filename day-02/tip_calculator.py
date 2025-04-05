# 05 April 2025

# Tip Calculator
# 1. Ask the user for the total bill
# 2. How much tip percentage they would like to give
# 3. How many people split the total bill
# 4. Finally giving the result.

print("Welcome to the tip calculator program!")
total_bill = float(input("What was the total bill? "))
tip_percentage = int(input("How much tip percentage would you like to give (10, 12 or 15)? "))
number_of_people = int(input("How many people to split the bill? "))

tip_multiplier = (tip_percentage / 100)
total_tip_amount = (total_bill * tip_multiplier)
total_bill_including_tip = (total_bill + total_tip_amount)
amount_per_person = (total_bill_including_tip / number_of_people)

print(f"Each person should pay: ${round(amount_per_person, 2)}")
