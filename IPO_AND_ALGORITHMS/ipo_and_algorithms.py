#================================= Problem 1 =======================================
#==========IPO MODEL===========#
# INPUT
#     first number
#     second number

# PROCESSING
#     add first and second number

# Output
#     sum

#===========ALGORITHM===========#
# 1. Start
# 2. Read first number
# 3. Read second number
# 4. Add the two numbers
# 5. Store the result
# 6. Display the result
# 7. Stop

#===========DRY RUN===========#
#INPUT:
# first number = 10
# second number = 20
#ADDITION:
# first number + second number
#  10 + 20 = 30
#OUTPUT:
#   30

#===========CODE=============#
first_number = int(input("Enter first number:- "))
second_number = int(input("Enter second number:- "))

add = first_number+second_number

print(add)

#================================= Problem 2 =======================================
#==========IPO MODEL===========#
# INPUT
#     number


# PROCESSING
#     check number % 2
#     if remainder equal to 0 then number is Even
#     otherwise number is Odd

# Output
#     Even or Odd

#===========ALGORITHM===========#
# 1. Start
# 2. Read number
# 3. check condition if number%2 == 0 
#       print -> Even
# 4. otherwise print -> Odd
# 5. Stop

#===========DRY RUN===========#
#input: 
#  number = 54

#Condition check:
#  check condition number % 2 remainder left 0
#  so number is even thus print -> "Even" 

#output
#  Even

#===========CODE=============#
num = int(input("Enter any number:- "))
if num%2 == 0:
    print("Even")
else:
    print("Odd")


#================================= Problem 3 =======================================
#==========IPO MODEL===========#
# INPUT
#     first number
#     second number
#     third number

# PROCESSING
#     compare each other to find largest number
#     if first number is greater than second and third number then largest is first number
#     if second number is greater than first and third number then largest is second number
#     if third number is greater than first and second number then largest is third number
#     otherwise all three numbers are equal

# Output
#     first or second or third number is largest or all are equal


#===========ALGORITHM===========#
# 1. Start
# 2. Read first,second and third number
# 3. compare all three numbers with each other with condition
# 4. if first number >= second and first number > third number then  print -> first number is largest
#    simillarly with second and third number
# 5. otherwise print -> all number are equall
# 6. Stop


#===========DRY RUN===========#


#===========CODE=============#
a = int(input("Enter first number:- "))
b = int(input("Enter second number:- "))
c = int(input("Enter third number:- "))

if a >= b and a > c:
    print(a, " is the largest")

elif  b >= a and b > c:
    print(b, " is the largest")

elif c >= b and c > a:
    print(c, " is the largest")
else:
    print("all numbers are equal")

#================================= Problem 4 =======================================
#==========IPO MODEL===========#
# INPUT
#     age    

# PROCESSING
#     check age >= 18

# Output
#     Eligible or not eligible


#===========ALGORITHM===========#
# 1. Start
# 2. Read age
# 3. check condition if age >= 18
#       print -> "Eligible for vote"
# 4. otherwise print -> "Not eligible for vote"
# 5. Stop


#===========DRY RUN===========#


#===========CODE=============#
age = int(input("Enter your age:- "))
if age >= 18:
    print("Eligible for vote")
else:
    print("Not Eligible for vote")


#================================= Problem 5 =======================================
#==========IPO MODEL===========#
# INPUT
#     price

# PROCESSING
#     check condition if price >= 2000
#     final_price = price-(price*0.20)

# Output
#     final price


#===========ALGORITHM===========#
# 1. Start
# 2. Read price
# 3. check condition if price >= 2000
#    final_price = price-(price*0.20)
# 4. Else, final_price = price
# 5. Print final_price
# 6. Stop

#===========DRY RUN===========#


#===========CODE=============#
price = float(input("enter item price:- "))
if price >= 2000:
    final_price = price-(price*0.20)
    print(final_price)
else:
    print(price)


#================================= Problem 6 =======================================
# INPUT
#     three subject's marks

# PROCESSING
#     calculate average of three subject's marks 
#     add all marks and then divide by three
#     check condition if avg >= 40
#     print -> "pass"
#     otherwise print -> fail

# Output
#     Pass or Fail


#===========ALGORITHM===========#
# 1. Start
# 2. Read marks a,b and c
# 3. calaculate avg = (a+b+c)/3
# 4. check condition if avg >=40  print -> "Pass"
# 5. otherwise print -> "Fail"
# 6. Stop


#===========DRY RUN===========#


#===========CODE===========#
a = int(input("Enter first subject's marks:- "))
b = int(input("Enter second subject's marks:- "))
c = int(input("Enter third subject's marks:- "))

avg = (a+b+c)/3
if avg >= 40:
    print('Pass')
else:
    print("Fail")