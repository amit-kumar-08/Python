
#PART-3  practical programs
#============================== Task 1 ==============================
a = 15
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

#============================== Task 2 ==============================
a = 15
b = 5.0

print(a+b,type(a+b))
print(a-b,type(a-b))
print(a*b,type(a*b))
print(a/b,type(a/b))
print(a//b,type(a//b))
print(a%b,type(a%b))
print(a**b,type(a**b))

#============================== Task 3 ==============================
python = 100
html = 99
css = 98

total_marks = python+html+css
average_marks = total_marks/3

print(total_marks)
print(average_marks)


#============================== Task 4 ==============================
product_price = 200
quantity = 50

total_price = product_price*quantity

print(total_price)

#============================== Task 5 ==============================
a = 40

print(a%2 ,"If remainder is zero then 'a' is even number otherwise it is odd number")

#============================== Task 6 ==============================
# Division and Floor Division
a=25
b=5
print(a/b)
print(a//b)

#============================== Task 7 ==============================
# Negative Number Operation
a=-10
b=-5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)

#============================== Task 8 ==============================
# Subtraction Edge Cases

# positive - positive
result1 = 10 - 5
print("10 - 5 =", result1)

# positive - negative
result2 = 10 - (-5)
print("10 - (-5) =", result2)

# negative - positive
result3 = -10 - 5
print("-10 - 5 =", result3)

# negative - negative
result4 = -10 - (-5)
print("-10 - (-5) =", result4)

#============================== Task 9 ==============================
# Floor Division Edge Cases

#positive // positive
result1 = 10 // 3
print("10 // 3 =", result1)

#negative // positive
result2 = (-10) // 3
print("-10 // 3 =", result2)

#positive // negative
result3 = 10 // (-3)
print("10 // -3 =", result3)

#negative // negative
result4 = (-10) // (-3)
print("-10 // -3 =", result4)

#============================== Task 10 ==============================
# Modules Edge Cases

#positive % positive
result1 = 10 % 3
print("10 % 3 =", result1)

#negative % positive
result2 = (-10) % 3
print("-10 % 3 =", result2)

#positive % negative
result3 = 10 % (-3)
print("10 % -3 =", result3)

#negative % negative
result4 = (-10) % (-3)
print("-10 % -3 =", result4)


#============================== Task 11 ==============================

print(10 + 5 * 2)    #expected output = 20        * operator evaluate first
print(20-4/2)        #expected output = 18.0       / operator evaluate first
print(10+20/5*2)     #expected output = 18.0        / then * operator evaluate first
print(2+3*4**2)      #expected output = 50        ** operator evaluate first
print(100-20//5)     #expected output = 96        // operator evaluate first

#============================== Task 12 ==============================
# Parentheses
print(10+5*2)        #here parentheses change the result because in python 
print((10+5)*2)      # arithmetic operator first priority to solve parentheses first.

print(20 - 10/2)
print((20-10)/2)

print(2+3*4)
print((2+3)*4)

#============================== Task 13 ==============================

t=True
f=False

print(t+f, type(t+f))

print(t-f, type(t-f))

print(t*f, type(t*f))

#print(t/f, type(t/f))    in this line code gives output zeroDivision error because any number divided by zero gives output ZeroDivisionError
print(f/t, type(f/t))     # it gives output 0.0

#print(t//f, type(t//f))    it also give output zeroDivisonError
print(f/t, type(f/t))     # it gives output 0.0

#print(t%f, type(t%f))       it also give output zeroDivisonError
print(f%t, type(f%t))     # it gives output 0

print(t**f, type(t**f))


#============================== Task 14 ==============================
print(True+5)       # it gives output 6  

print(False+5)       # it gives output 5  

print(True*10)        # it gives output 10  

print(False*10)        # it gives output 0  

print(True-5)           # it gives output -4

print(False-5)           # it gives output -5

#============================== Task 15 ==============================
# String Operartions
first_name = "Amit"
last_name = " kumar"

print(first_name + last_name)

#============================== Task 16 ==============================

string = "Hello"

print(string*3)

#print(string*2.5)      TypeError Occurs

#============================== Task 17 ==============================

print("A"+"B")

#print('A'-'B')     TypeError Occurs

#print("A"*"B")     TypeError Occurs

#print("A"/"B")     TypeError Occurs

#============================== Task 18 ==============================

value=None

#print(value+1)      TypeError Occurs

#print(value-1)      TypeError Occurs

#print(value*1)      TypeError Occurs

#print(value/1)      TypeError Occurs

#print(value//1)     TypeError Occurs

#print(value%1)      TypeError Occurs

#print(value**1)     TypeError Occurs

#None in Python represents the absence of a value or no value. It is not a number, so it cannot be directly used in arithmetic operations.

#============================== Task 19 ==============================
# A=1
# B=0
# print(A/B)    ZeroDivisionError

# str1 = "A"
# str2 = "B"
# print(str1*str2)      TypeError

# a=None
# b=1
# print(a+b)          TypeError

#============================== Task 20 ==============================
# Create two numbers
num1 = 20
num2 = 6

# Perform calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
modulus = num1 % num2
exponentiation = num1 ** num2

# Display the results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Floor Division:", floor_division)
print("Modulus:", modulus)
print("Exponentiation:", exponentiation)

#============================== Task 21 ==============================
# Arithmetic Expression Analyzer
a = 10
b = -3
c = 2.5

# Expression 1
print("1.", a + b)           #expected output = 7

# Expression 2
print("2.", a - b)           #expected output = 13

# Expression 3
print("3.", a * c)            #expected output = 25.0

# Expression 4
print("4.", a / c)           #expected output = 4.0

# Expression 5
print("5.", a // b)          #expected output = -4

# Expression 6
print("6.", a % b)           #expected output = -2

# Expression 7
print("7.", a ** 2)          #expected output = 100

# Expression 8 - Parentheses
print("8.", (a + b) * c)      #expected output = 17.5

# Expression 9 - Multiple operators
print("9.", a + b * c)                   #expected output = 2.5

# Expression 10 - Multiple operators and parentheses
print("10.", (a - b) / c + 2)            #expected output = 7.2
