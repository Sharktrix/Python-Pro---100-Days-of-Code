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





# Day 3.4 Exercise

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
