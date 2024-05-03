# Task 1: Identify the Greatest:
# Write a Python program that prompts the user to enter three numbers.
# The program should then identify and print out the largest number among the three.

print("Enter 3 numbers to see which is the Largest!")



num1 = int(input("Your first number!"))
num2 = int(input("Your second number!"))
num3 = int(input("Your third number!"))

if (num1 >= num2) and (num1 >= num3):
 largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
   
print("The largest number is", largest)



# Task 2: Identify the Smallest
# Extend your program from Task 1 to also determine the smallest 
# number among the three and print it out.



print("Enter 3 numbers to see which is the Largest!")



num1 = int(input("Your first number!"))
num2 = int(input("Your second number!"))
num3 = int(input("Your third number!"))

if (num1 > num2) and (num1 > num3):
 largest = num1
 
elif (num2 > num1) and (num2 > num3):
   largest = num2
   
else:
   largest = num3

if (num1 < num2) and (num1 < num3):
    smallest = num1

elif (num2 < num1) and (num2 < num3):
    smallest = num2

else:
    smallest= num3
   
   
print("The largest number is!", largest, "The Smallest number is!",smallest)




# Task 3: Equality Check:
# Enhance your program to handle cases where two or all of the numbers are equal.
# The program should display appropriate messages like "Two numbers are equal 
# and the largest" or "All numbers are equal".



print("Enter 3 numbers to see which is the Largest!")



num1 = int(input("Your first number!"))
num2 = int(input("Your second number!"))
num3 = int(input("Your third number!"))

if (num1 > num2) and (num1 > num3):
    largest = num1
 
elif (num2 > num1) and (num2 > num3):
   largest = num2
   
else:
   largest = num3
print("The largest number is!", largest,)

if (num1 < num2) and (num1 < num3):
    smallest = num1

elif (num2 < num1) and (num2 < num3):
    smallest = num2

else:
    smallest= num3
print("The Smallest number is!",smallest,)

if (num1 == num2) and (num1 == num3):
    equal = num1

elif (num2 == num1) and (num2 == num3):
    equal = num2

else:
    equal = num3
print("These numbers is the same!",equal)