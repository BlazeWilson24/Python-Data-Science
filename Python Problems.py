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
    print(year,"Its not a leap year.")   

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

# Q11. Program to check if the number is prime or not.

num = int(input("Enter a number:"))        
if num==1:
   print("It is not a prime number.")
if num>1:
    for i in range(2,num):
     if num%i==0:
       print("It is not a prime number")
       break
    else:
        print("Its a prime number")


# Q12. Program to generate a random number.

import random

num = random.randint(0,10)
print(num)


# Q13. Python program to print all the prime numbers in an interval.

lower = int(input("Enter a number: "))
upper = int(input("Enter a number: "))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

# Q14. Program to convert celsius to fahrenheit.

celsius = int(input("Enter a number in celsius: "))
fahrenheit = (celsius*(9/5))+32
print("The converted value is ",fahrenheit,"fahreheit.")


# Q15. Program to find the factorial of a number.

num = int(input("Enter a number: "))
fact = 1
if num<0:
    print("It doesnot exist.")
if num==0:
    print("Factorial of 0 is",1)
if num>0:
    for i in range(1,num+1):
        fact = fact*i
print("The factorial of the given number is",fact)                

# Using Recursion

def fact(a):
    if a==0:
        return 1
    else: 
        return((a)*fact(a-1))

num = int(input("Enter a number here: "))
result = fact(num)
print("The factorial of the given number is ",result)    

# 16Q. Program to display the multiplication table.

n = int(input("Enter a number here: "))
for i in range(1,11):
    print(n,"x",i,"=",n*i)

# Using while loop

n= 9
i=1
while i<=10:
    print(n,"x",i,"=",n*i)
    i+=1

# 17Q. Program to print the fibonacci sequence.

a= 0
b= 1
num = int(input("Enter a number: "))
if num==1:
    print(a)
else:
    print(a)
    print(b)
    for i in range (2, num):
        c= a+b
        a=b
        b=c
        print(c)

# 18Q. Program to check armstrong number.

num = int(input("Enter a number here: "))
sum = 0
temp = num
while temp>0:
    digit=temp%10
    cube= digit**3
    sum=sum+cube
    temp//=10
if sum==num:
    print("It is an armstrong number. ")
else:
    print("It is not an armstrong number.")        

# 19Q. Program to find armstrong number in an interval.

lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

for num in range(lower, upper+1):
    order = len(str(num))
    sum=0
    temp=num
    while temp>0:
        digit = temp%10
        sum+=digit**order
        temp//=10
    if num == sum:
        print(num)    

# 20Q. Program to find the sum of natural numbers.

num= int(input("Enter a number here: "))        
if num<0:
    print("Please enter the positive number.")
else:
    sum=0
    while num>0:
        sum+=num
        num-=1
    print(sum)    






        
            



     

























