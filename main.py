print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

percent_tip = tip / 100
total_tip = bill * percent_tip
total_bill = bill + total_tip
bill_per_person = total_bill / people
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay ${final_amount}")
