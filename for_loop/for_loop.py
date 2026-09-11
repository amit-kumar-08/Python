#=======================================Question = 1 =========================================
for i in range(1,6):
    print("Hello")

#=======================================Question = 2 =========================================
for i in range(0,10):
    print(i,end=" ")

#=======================================Question = 3 =========================================
for i in range(1,11):
    print(i)

#=======================================Question = 4 =========================================
for i in range(10,0,-1):
    print(i)

#=======================================Question = 5 =========================================
for i in range(5,51,5):
    print(i)

#=======================================Question = 6 =========================================
for i in range(2,21,2):
    print(i)

#=======================================Question = 7 =========================================
for i in range(1,20,2):
    print(i)

#=======================================Question = 8 =========================================
for i in range(3,20,3):
    print(i, end=" ")

#=======================================Question = 9 =========================================
for i in range(20,1,-2):
    print(i)

#=======================================Question = 10 =========================================
n = int(input("Enter any positive integer:- "))

for i in range(1,n+1):
    print(i)

#=======================================Question = 11 =========================================
n = int(input("Enter any number:- "))
for i in range(1,n+1):
    if i % 2==0:
        print(i)

    
#=======================================Question = 12 =========================================
n = int(input("Enter any number:- "))
for i in range(1,n+1):
    if i % 2!=0:
        print(i)


#=======================================Question = 13 =========================================
n = int(input("Enter any number:- "))
for i in range(1,n+1):
    if i % 3 == 0:
        print(i)


#=======================================Question = 14 =========================================
n = int(input("Enter any number:- "))
for i in range(1,n+1):
    if i % 2 == 0 and i % 3 == 0:
        print(i)


#=======================================Question = 15 =========================================
count = 0
n = int(input("Enter any number:- "))
for i in range(1,n+1):
    if i % 2==0:
        count = count + 1
print(f"Total {count} numbers from 1 to {n} are even.")

#=======================================Question = 16 =========================================
num = int(input("Enter any number to sum of all numbers:- "))
sum = 0
for i in range(1,num+1):
    sum = sum + i
print(sum)


#=======================================Question = 17 =========================================
num = int(input("Enter any number to sum of all even numbers:- "))
sum_even = 0
for j in range(1,num+1):
    if j % 2 == 0:
        sum_even = sum_even + j

print(sum_even)


#=======================================Question = 18 =========================================
num = int(input("Enter any number to sum of all odd numbers:- "))
sum_odd = 0
for j in range(1,num+1):
    if j % 2 != 0:
        sum_odd = sum_odd + j

print(sum_odd)


#=======================================Question = 19 =========================================
num = int(input("Enter a number to get table of that number:- "))
for k in range(1,11):
    print(f"{num} * {k} = {num*k}")


#=======================================Question = 20 =========================================
n = int(input("Enter any number to multiply from 1 to given number:- "))
multiply = 1
for l in range(1,n+1):
    multiply = multiply * l
print(f"multiplication of all number from 1 to {n} is {multiply}")


#=======================================Question = 21 =========================================
word = input("Enter any word:- ")
for k in word:
    print(k)


#=======================================Question = 22 =========================================
word = input("Enter any word:- ")
for j in word:
    print(j, end="")


#=======================================Question = 23 =========================================
word = input("Enter any word:- ")
count = 0
for k in word:
    count = count + 1

print(count)


#=======================================Question = 24 =========================================
word = input("Enter any word:- ")
count = 0
for k in word:
    if k == "a":
        count = count + 1

print(count)

#=======================================Question = 25 =========================================
word = input("Enter any word:- ")
count = 0
for k in word:
    if k == k.upper():
        count = count + 1

print(count)


#=======================================Question = 26 =========================================
for row in range(3):
    for column in range(4):
        print("*", end="")
    print()

#=======================================Question = 27 =========================================
for row in range(4):
    for column in range(5):
        print("*", end="")
    print()


#=======================================Question = 28 =========================================
for row in range(1,6):
    for column in range(1,row+1):
        print("*", end="")
    print()


#=======================================Question = 29 =========================================
for row in range(1,6):
    for column in range(1,row+1):
        print(column , end="")
    print()

#=======================================Question = 30 =========================================
num = int(input("Enter any number to get table from 1 to entered number:- "))
for row in range(1,num+1):
    for column in range(1,11):
        print(row*column, end=" ")
    print()


#Final Practice Challenge
number = int(input("Enter any numbar:- "))

for row in range(1,number+1):
    for column in range(1,row+1):
        print(column, end="")
    print()


