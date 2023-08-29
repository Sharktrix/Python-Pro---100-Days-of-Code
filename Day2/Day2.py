num_char = len(input("What is your name? "))

new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.")

# Type function

a = float(123)
print(type(a))

print(70 + float ("100.5")) #Floating numbers

print(str(70) + str(100)) #String characters

# Exercise 2.1

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")  #Input function
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

print(type(two_digit_number)) # Type finding to find the data type

first_digit = two_digit_number[0] # Using Subcript to locate the digits
second_digit = two_digit_number[1] # Using Subcript


result = int(first_digit) + int(second_digit) # Type Converting to convert from str to int 
print(result)


# Exercise 2.2 

# PEMDASLR 
# ()
# **
# * / 
# + - 

print (3 * (3 + 3) / 3 - 3)

# Exercise 2.3 

# Calculating Body Mass Index - BMI Calculator

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# BMI = weight (kg) / height squared (m2)

bmi = weight / height ** 2 # Using the exponent operator ** 
print(type(height)) # Type checking gives str is used as data types

bmi = float(weight) / float(height) ** 2 # Type converting to float
print(bmi) # Massive floating point number , should be a int whole number

bmi = float(weight) / float(height) ** 2 
bmi_as_int = int(bmi) #Convert float point number into int whole number
print(bmi_as_int)


# Alternate Way of the Same Code 

weight_as_int = int(weight)
height_as_float = float(height)

#Using the exponent operator ** 
bmi = weight_as_int / height_as_float ** 2 
# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)

print(bmi_as_int)


# Exercise 2.4  LIFE IN WEEKS

age = input("What is your current age?")

# Remember input always creates a string data type and we need to conver to int data type
# 1 year = 365 Days 
# 1 year = 52 Weeks 
# 1 year = 12 Months 

# Write your code here : 

# Age is never going to be float (16.5)
age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365 
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12 

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
print(message)




