print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
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








