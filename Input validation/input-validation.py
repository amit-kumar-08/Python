#=========================================Question 1===================================

marks = int(input("Enter marks: "))

while marks < 0 or marks > 100:
    print("Invalid marks!")
    marks = int(input("Enter marks: "))

print("Accepted marks:", marks)


#=========================================Question 2===================================

num = int(input("Enter a positive integer: "))

while num <= 0:
    print("Enter a number greater than 0")
    num = int(input("Enter a positive integer: "))

print("Accepted number:", num)

#=========================================Question 3===================================

age = int(input("Enter your age: "))

while age < 0 or age > 120:
    print("Invalid age!")
    age = int(input("Enter your age: "))

print("Accepted age:", age)

#=========================================Question 4===================================

choice = 0

while choice < 1 or choice > 4:
    print("\n1. View profile")
    print("2. Edit profile")
    print("3. Settings")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice < 1 or choice > 4:
        print("Invalid choice!")

print("Selected option:", choice)

#=========================================Question 5===================================

password = input("Enter password: ")

while len(password.strip()) < 8:
    print("Password must have at least 8 characters")
    password = input("Enter password: ")

print("Password accepted!")

#=========================================Question 6===================================

temp = float(input("Enter temperature: "))

while temp < -20 or temp > 45:
    print("Temperature must be between -20 and 45")
    temp = float(input("Enter temperature: "))

print("Accepted temperature:", temp)

#=========================================Question 7===================================

balance = 5000

amount = float(input("Enter withdrawal amount: "))

while amount <= 0 or amount > balance:
    print("Invalid withdrawal amount!")
    amount = float(input("Enter withdrawal amount: "))

balance = balance - amount

print("Remaining balance:", balance)

#=========================================Question 8===================================

username = input("Enter username: ").strip()

while len(username) < 5 or " " in username or username == "":
    print("Invalid username!")
    username = input("Enter username: ").strip()

print("Accepted username:", username)

#=========================================Question 9===================================

num = int(input("Enter a positive number divisible by 3 and 5: "))

while num <= 0 or num % 3 != 0 or num % 5 != 0:
    print("Invalid number!")
    num = int(input("Enter a positive number divisible by 3 and 5: "))

print("Accepted number:", num)

#=========================================Question 10===================================

pin = 2468
attempts = 0

while attempts < 3:
    entered_pin = int(input("Enter PIN: "))
    attempts = attempts + 1

    if entered_pin == pin:
        print("Access granted!")
        break
    else:
        print("Incorrect PIN!")

if attempts == 3 and entered_pin != pin:
    print("Access denied!")

#=========================================Question 11===================================

num = int(input("Enter a number between 10 and 50: "))

while num < 10 or num > 50:
    print("Invalid number!")
    num = int(input("Enter a number between 10 and 50: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#=========================================Question 12===================================

balance = 2000

amount = float(input("Enter deposit amount: "))

while amount <= 0:
    print("Deposit must be greater than 0")
    amount = float(input("Enter deposit amount: "))

balance = balance + amount

print("New balance:", balance)

#=========================================Question 13===================================

num = int(input("Enter a number between 1 and 100: "))

while num < 1 or num > 100:
    print("Invalid number!")
    num = int(input("Enter a number between 1 and 100: "))

print("Accepted number:", num)

#=========================================Question 14===================================

marks = int(input("Enter marks: "))

while marks < 0 or marks > 100:
    print("Invalid marks!")
    marks = int(input("Enter marks: "))

if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")

#=========================================Question 15===================================

username = input("Enter username: ").strip()
password = input("Enter password: ").strip()

while len(username) < 5 or " " in username or len(password) < 8:
    print("Invalid username or password!")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

print("Login details accepted!")

#=========================================Question 16===================================

a = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")

while operator != "+" and operator != "-" and operator != "*" and operator != "/":
    print("Invalid operator!")
    operator = input("Enter operator (+, -, *, /): ")

b = float(input("Enter second number: "))

while operator == "/" and b == 0:
    print("Cannot divide by zero!")
    b = float(input("Enter second number: "))

if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
else:
    print("Result:", a / b)

#=========================================Question 17===================================

balance = 10000
choice = 0

while choice != 4:
    print("\n1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))

        while amount <= 0:
            print("Amount must be greater than 0")
            amount = float(input("Enter deposit amount: "))

        balance = balance + amount
        print("Updated balance:", balance)

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        while amount <= 0 or amount > balance:
            print("Invalid withdrawal amount!")
            amount = float(input("Enter withdrawal amount: "))

        balance = balance - amount
        print("Updated balance:", balance)

    elif choice == 4:
        print("Thank you!")

    else:
        print("Invalid choice!")
        choice = 0

#=========================================Question 18===================================

month = int(input("Enter month (1-12): "))
day = int(input("Enter day (1-31): "))

while month < 1 or month > 12 or day < 1 or day > 31:
    print("Invalid month or day!")
    month = int(input("Enter month (1-12): "))
    day = int(input("Enter day (1-31): "))

print("Accepted month:", month)
print("Accepted day:", day)

#=========================================Question 19===================================

quantity = int(input("Enter quantity: "))

while quantity <= 0:
    print("Quantity must be positive")
    quantity = int(input("Enter quantity: "))

price = float(input("Enter unit price: "))

while price <= 0:
    print("Price must be greater than 0")
    price = float(input("Enter unit price: "))

total = quantity * price

print("Total cost:", total)

#=========================================Question 20===================================

count = int(input("How many numbers do you want to enter? "))

while count < 1 or count > 20:
    print("Enter a count between 1 and 20")
    count = int(input("How many numbers do you want to enter? "))

total = 0
i = 1

while i <= count:
    num = float(input("Enter number: "))
    total = total + num
    i = i + 1

average = total / count

print("Average:", average)

#=========================================Question 21===================================

password = input("Enter password: ")

while (len(password) < 8 or
       not any(ch.isupper() for ch in password) or
       not any(ch.islower() for ch in password) or
       not any(ch.isdigit() for ch in password) or
       any(ch.isspace() for ch in password)):

    print("Password does not meet all rules")

    if len(password) < 8:
        print("Must have at least 8 characters")
    if not any(ch.isupper() for ch in password):
        print("Must have an uppercase letter")
    if not any(ch.islower() for ch in password):
        print("Must have a lowercase letter")
    if not any(ch.isdigit() for ch in password):
        print("Must have a digit")
    if any(ch.isspace() for ch in password):
        print("Must not contain whitespace")

    password = input("Enter password again: ")

print("Password accepted!")

#=========================================Question 22===================================

num = 0

while num < 1 or num > 10:
    num = int(input("Enter a number from 1 to 10: "))

    if num < 1 or num > 10:
        print("Invalid number!")

print("Accepted number:", num)

#=========================================Question 23===================================

score1 = int(input("Enter first score: "))

while score1 < 0 or score1 > 100:
    print("Invalid score!")
    score1 = int(input("Enter first score: "))

score2 = int(input("Enter second score: "))

while score2 < 0 or score2 > 100:
    print("Invalid score!")
    score2 = int(input("Enter second score: "))

score3 = int(input("Enter third score: "))

while score3 < 0 or score3 > 100:
    print("Invalid score!")
    score3 = int(input("Enter third score: "))

total = score1 + score2 + score3
average = total / 3

print("Total:", total)
print("Average:", average)

#=========================================Question 24===================================

balance = 10000

amount = int(input("Enter withdrawal amount: "))

while amount <= 0 or amount > balance or amount % 100 != 0:
    print("Invalid amount!")
    print("Amount must be positive, within balance, and a multiple of 100.")
    amount = int(input("Enter withdrawal amount: "))

balance = balance - amount

print("Withdrawn amount:", amount)
print("Remaining balance:", balance)
