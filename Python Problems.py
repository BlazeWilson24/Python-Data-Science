# Q1. Program to print 'hello world'

print("hello world")

# Q2. Program to add two numbers 

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
sum = num1 + num2
print("The sum of the provided two number is: ",sum)

# Q3. Program to find the square root of the number.

num = int(input("Enter a number: "))
sr = num**(0.5)
print("The square root of the given number is: ",sr)

# uSING MATH MODULE 

import math
num = int(input("enter a number: "))
sr = math.sqrt(num)
print("The square root of the givcen number is: ",sr)

# Q4. Python program to calculate area of triangle.

height = float(input("Enter height :"))
base = float (input("Enter base :" ))
area = (0.5)*height*base
print("The area of the triangle is: ",area)

# Q5. Program to swap two variables.

x = 13
y = 12
temp = 13
x=y
y= temp

print(" The value of x is ", x)
print(" The value of y is ", y)

# Q6. Program to convert km to miles.

km = float(input("Enter a number:"))
miles = (0.621371)*km
print(km, "km in miles will be: ",miles)

# Q7. Program to check if a number is positive, negative or zero.

num = float(input( "Enter a number: "))
if num >0:
    print("It is a positive number.")
elif num<0:
    print("It is a negative number.")
else:
    print("It is a zero")       

# Q8. Program to check if the number is odd or even. 

num = float(input("Enter a number: "))
if num%2==0:
    print("It is an even number.")
else:
    print("It is an odd number. ")

# Q9. Program to check leap year.

year = int(input("Enter a year: "))
if (year%400==0) and (year%100==0):
    print(year," is a leap year.")
elif (year%4==0) and (year%100!=0):
    print(year, "is a leap year.")   
else: 
    print(year,"Its not a leap year.")    \

# Q10. Find the largest among three numbers.

num1= float(input("Enter your first number: "))
num2= float(input("Enter your second number: "))
num3= float(input("Enter third number: "))
if (num1>num2) and (num1>num3):
    print(num1, "is greater.")
elif (num2>num1) and (num2>num3):
    print(num2, "is greater.")
else: 
    print(num3,"is greater.")        





        
            



     

























