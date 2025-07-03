#Write a program that checks if a number is positive or negative.
# if it is zero, print "Zero".
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
#Input a number from the user and print whether it is even or odd.
a= int(input("Enter a number: "))
if a % 2 == 0:
    print("Even") 
else:
    print("Odd")
#Ask the user to enter their age.
#👉 If age is 18 or above, print "Eligible to vote"
#👉 Else, print "Not eligible"
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
# Enter a number and check whether it is divisible by:
#✔ 3
#✔ 5
#✔ Both
#Print an appropriate message.
x = int(input("Enter a number: "))
if x % 3 == 0 and x % 5 == 0:
    print("Divisible by both 3 and 5")  
elif x % 3 == 0:
    print("Divisible by 3")
elif x % 5 == 0:
    print("Divisible by 5")
#**Ask for a student's marks and assign a grade:
#90+ → "A+"
#80+ → "A"
#70+ → "B"
#Otherwise → "Fail"**
marks = int(input("Enter student's marks: "))
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
else:
    print("Fail")
#**Take a temperature input:
#Above 40 → "Too hot"
#Below 10 → "Too cold"
#Otherwise → "Moderate weather"**
temprture = float(input("Enter temperature: "))
if temprture > 40:
    print("Too hot")   
elif temprture < 10:
    print("Too cold")   
else:
    print("Moderate weather")
# Ask the user to enter a year.
#👉 Check whether it is a leap year or not.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
#Input three numbers and print the largest one.
i= int(input("Enter first number: "))
j= int(input("Enter second number: "))
k= int(input("Enter third number: "))
if i >= j and i >= k:
    print("Largest number is:", i)
elif j >= i and j >= k:
    print("Largest number is:", j)
elif k >= i and k >= j:
    print("Largest number is:", k)
elif i == j and i == k:
    print("All numbers are equal")
# Ask the user to enter a password.
#👉 If password matches "admin123" → print "Access granted"
#👉 Else → "Access denied"
password = input("Enter password: ")
if password == "admin123":
    print("Access granted") 
else:
    print("Access denied")  
#**Take an integer input.
#If number > 0, check if it’s less than 100
#Print appropriate messages for both checks**
num = int(input("Enter an integer: "))
if num > 0:
    if num < 100:
        print("Number is positive and less than 100")
    else:
        print("Number is positive but not less than 100")   
else:
    print("Number is not positive")