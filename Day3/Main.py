print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult Tickets are $12.")

    wants_photo = input("Do you want your photo taken? Y or N.")    
    if wants_photo == "Y":
        bill += 3
    
    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you ride.")


# Day 3-1 : Exercise 

number = int(input("Which number do you want to change?"))

if number % 2 == 0:
    print("This is a even number.")
else:
    print("This is an odd number.")


# Day 3-2 Exercise 

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round( weight / height ** 2)
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight. ")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight. ")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")


# Exercise 3-3 Exercise Interactive Coding - Leap Year

year = int(input("Which year do you want to check?"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not Leap year.")
    else:
        print("Leap year.")
else:
    print("Not Leap year.")





# Day 3.4 Exercise Pizza Delivery

print("Welcome to Python Pizza Deliveries!")
size = input("What size do you want? S, M or L? ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")




# Day 3.5 Exercise Love Calculator

# Get names from the user
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Convert names to lowercase for uniformity
name1 = name1.lower()
name2 = name2.lower()

# Concatenate names to make it easier to count
combined_names = name1 + name2

# Count the occurrences of each letter in "TRUE"
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")

# Count the occurrences of each letter in "LOVE"
l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")  # Note: 'e' was already counted, but it's okay to count again

# Calculate the totals for TRUE and LOVE
total_true = t + r + u + e
total_love = l + o + v + e

# Combine the totals to make a two-digit number
love_score = int(str(total_true) + str(total_love))

# Generate and print the love score message
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")


