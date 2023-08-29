# TIP Calculator : 

# If the bill was $150.00, split between 5 people, with 12% Tip. 

# Each person should pay (150.00 / 5) * 1.12

# Round the result tgo 2 decimal places = 33.60

print("Welcome to the tip Calculator!")
bill = float(input("What was the Total Bill? $ ")) # Set Variable to store Data & input always has str format
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}") 



