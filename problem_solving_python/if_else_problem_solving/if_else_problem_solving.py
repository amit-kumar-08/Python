#Python If-Else Problem Solving — 30 Problems

#LEVEL 1
#========================================== problem 1 =============================================
'''number = int(input("Enter any number:- "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

#========================================== problem 2 =============================================
number = int(input("Enter any number:- "))

if number > 0 and number %2 == 0:
    print("Positive Even")
elif number > 0 and number %2 != 0:
    print("Positive Odd")
elif number < 0 and number %2 == 0:
    print("Negative Even")
elif number < 0 and number %2 != 0:
    print("Negative Odd")
else:
    print("Zero")

#========================================== problem 3 =============================================
num1 = int(input("enter first number:- "))
num2 = int(input("enter second number:- "))

if num1 > num2:
    print(num1," is the larger number")
elif num1 < num2:
    print(num2, " is the larger number")
else:
    print("Both are equal")

#========================================== problem 4 =============================================
a , b , c = map(int, input("enter any three number:- ").split()) 

if a <= b and a < c:
    print("smallest number = ",a)

elif  b <= a and b < c:
    print("smallest number = ",b)

elif c <= b and c < a:
    print("smallest number = ",c)
    
else:
    print("all numbers are equal")


#========================================== problem 5 =============================================
a , b , c = map(int, input("enter any three number:- ").split()) 

if a >= b and a > c:
    print(a, " is the largest")

elif  b >= a and b > c:
    print(b, " is the largest")

elif c >= b and c > a:
    print(c, " is the largest")
else:
    print("all numbers are equal")


#========================================== problem 6 =============================================
num = int(input("Enter any number:- "))

if num % 5 == 0 and num % 11 == 0:
    print(f"{num} is divisible by both 5 and 11")

elif num % 5 == 0:
    print(f"{num} is divisible by only 5")

elif num % 11 == 0:
    print(f"{num} is divisible by only 11")

else:
    print(f"{num} is divisible by neither 5 nor 11")


#========================================== problem 7 =============================================
num = int(input("Enter any number:- "))

if num % 3 == 0 and num % 7 == 0:
    print(f"{num} is divisible by both 3 and 7")

elif num % 3 == 0:
    print(f"{num} is divisible by only 3")

elif num % 7 == 0:
    print(f"{num} is divisible by only 7")

else:
    print(f"{num} is divisible by neither 3 nor 7")


#========================================== problem 8 =============================================
marks = int(input("Enter your marks:- "))
if marks >= 40 and marks <= 100:
    print("Pass")

elif marks >=0 and marks < 40:
    print("Fail")

else:
    print("Invalid marks")


#========================================== problem 9 =============================================
marks = int(input("Enter your marks:- "))
if marks >= 90 and marks <= 100:
    print("Grade A")

elif marks >=80 and marks < 90:
    print("Grade B")

elif marks >=70 and marks < 80:
    print("Grade C")

elif marks >=60 and marks < 70:
    print("Grade D")

elif marks >=40 and marks < 60:
    print("Grade E")  

elif marks >=0 and marks < 40:
    print("Fail")  

else:
    print("Invalid marks")

#========================================== problem 10 =============================================
age = int(input("Enter your age:- "))

if age >= 18 and age <= 120:
    print("Can Vote")

elif age >= 0 and age < 18:
    print("Cannot Vote")

else:
    print("Invalid age")


#LEVEL 2
#========================================== problem 11 =============================================
year = int(input("Enter any year:- "))

if year % 4 == 0 and year % 100 != 0:
    print("Leap year")

elif year % 400 == 0:
    print("Leap year")

else:
    print("Not a leap year")


#========================================== problem 12 =============================================
char = input("Enter one character: ")

if len(char) != 1:
    print("Please enter exactly one character")

elif 'A' <= char <= 'Z':
    print("Uppercase alphabet")

elif 'a' <= char <= 'z':
    print("Lowercase alphabet")

elif '0' <= char <= '9':
    print("Digit")

else:
    print("Special character")


#========================================== problem 13 =============================================
char = input("Enter one character: ").lower()

if len(char) != 1:
    print("Please enter exactly one character")

elif ("A" <= char <= "Z") or ("a" <= char <= "z"):
    if char in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
        
else:
    print("Invalid input")


#========================================== problem 14 =============================================
cost_price = int(input("Enter cost price in rupee:- "))
selling_peice = int(input("Enter selling price in rupee:- "))

if selling_peice > cost_price:
    print(f"Profit = {selling_peice-cost_price}RS")

elif cost_price > selling_peice:
    print(f"Loss = {cost_price-selling_peice}RS")

else:
    print("No profit No loss")


#========================================== problem 15 =============================================
cost_price = int(input("Enter cost price in rupee:- "))
selling_peice = int(input("Enter selling price in rupee:- "))

profit = selling_peice - cost_price
loss = cost_price - selling_peice

if cost_price > 0:
    if selling_peice > cost_price:
        print(f"Profit = {profit}RS and profit percentage = {profit/cost_price*100}")

    elif cost_price > selling_peice:
        print(f"Loss = {loss}RS and loss percentage = {(loss/cost_price*100):.2f}")
    else:
        print("No profit No loss")
else:
    print("Invalid cost price")


#========================================== problem 16 =============================================
units = int(input("Enter your electricity bill unit:- "))

if 0 <= units <= 100:
    print(f"Electricity bill = {units*5}RS")

elif 100 < units <=200:
    print(f"Electricity bill = {(100*5)+(units-100)*7}RS")

else:
    print(f"Electricity bill = {100*5 + 100*7 + (units - 200)*10}RS")


#========================================== problem 17 =============================================
operation = input("Enter any operation that you want to use (+, -, *, /):- ").strip()

if operation == "+" or operation == "-" or operation == "*" or operation == "/":

    a = int(input("Enter first number:- "))
    b = int(input("Enter second number:- "))

    if operation == "+":
        print(f"sum of {a} and {b} is {a+b}")

    elif operation == "-":
        print(f"subtraction of {a} and {b} is {a-b}")

    elif operation == "*":
        print(f"multiplication of {a} and {b} is {a*b}")

    elif operation == "/" and b != 0:
        print(f"division of {a} and {b} is {a/b}")

    elif operation == "/" and b == 0:
        print("division by zero not allowed ")

else:
    print("invalid operation")


#========================================== problem 18 =============================================
temprature = float(input("Enter temprature in celsius:- "))

if temprature < 0:
    print("Freezing")
elif 0 <= temprature <= 15:
    print("Very cold")
elif 15 < temprature <= 25:
    print("Cold")
elif 25 < temprature <= 35:
    print("Normal")
else:
    print("Hot")


#========================================== problem 19 =============================================
num = int(input("Enter any number:- "))
if num < 0:
    print("Negative")

elif 0 <= num <= 10:
    print("Number belongs to 0 to 10")

elif 10 < num <= 50:
    print("Number is between 10 and 51")

elif 50 < num <= 100:
    print("Number is between 50 and 101")

else:
    print("Number is greater than 100")'''

#========================================== problem 20 =============================================
a = float(input("Enter first side of triangle:- "))
b = float(input("Enter Second side of triangle:- "))
c = float(input("Enter Third side of triangle:- "))

if a + b > c and a + c > b and b + c > a:
    print("Valid triangle")

else:
    print("Invalid triangle")


#LEVEL 3
#========================================== problem 21 =============================================