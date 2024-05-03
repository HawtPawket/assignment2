# Task 1: Leap Year Checker
# Write a Python program that prompts the user to input a year. 
# The program should determine if the given year is a leap year or not 
# and then display an appropriate message. Please note that this is the definition of a 
# leap year: Every year that is exactly divisible by four is a leap year, except for years that are exactly 
# divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.


print("Enter the year here to see if it is a Leap Year!")

year = int(input("Which year would you like to check?"))

if (year % 4 == 0) and (year % 100 != 0):
    print("This is a Leap Year!")

elif (year % 100 == 0) and (year % 400 == 0):
    print("This is a Leap Year!")

else:
    print("This is not a Leap Year!")