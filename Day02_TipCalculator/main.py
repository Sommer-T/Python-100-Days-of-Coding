# Day 2 - Tip Calculator

print("Welcome to the Tip Calculator!")

bill = input("What was the total bill? $")
tip_percent = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

bill = float(bill)
tip_percent = int(tip_percent)
people = int(people)

tip_multiplier = 1 + tip_percent / 100
total_bill = bill * tip_multiplier
amount_per_person = total_bill / people

final_amount = f"{amount_per_person:.2f}"
print(f"Each person should pay: ${final_amount}")