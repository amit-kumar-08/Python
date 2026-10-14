#SECTION A
#A1
#Output Prediction

#==================================Question 1====================================
for i in range(1, 8):
    if i == 5:
        break
    print(i)
print("Finished")

#output
# 1
# 2
# 3
# 4
# Finished

#==================================Question 2====================================
word = "skyline"

for ch in word:
    if ch in "aeiou":
        break
    print(ch)

#Output
# s
# k
# y
# l

#==================================Question 3====================================
n = 2

while n <= 10:
    print(n)
    if n == 6:
        break
    n += 2

#output
# 2
# 4
# 6


#A2
#==================================Question 4====================================
limit = int(input("enter limit:- "))

for i in range(1,limit+1):
    if i == 7:
        break
    print(i,end=" ")
print()


#==================================Question 5====================================
str1 = input("enter any string:- ").strip().lower()
target = input("enter any one character:- ").strip().lower()

for ch in str1:
    print("Checked character:-",ch)
    if ch == target:
        break
print()

#==================================Question 6====================================
numbers = map(int,input("enter multiple numbers:- ").split())
for i in numbers:
    if i < 0:
        break
    print(i)


#A3
#==================================Question 7====================================
for row in range(1, 4):
    for col in range(1, 5):
        if col == 3:
            break
        print(row, col)

#Output 
# 1 1
# 1 2
# 2 1
# 2 2
# 3 1
# 3 2
# Outer loop continues because break statement only terminate nearest loop 


#==================================Question 8====================================
sentence = input("Enter any sentence:- ").lower().split()
target = input("Enter any word for find that word in sentence:- ")

for i in sentence:
    if i == target:
        print("Found")
        break
else:
    print("Not Found")


#SECTION B
#B1
#Output prediction
#==================================Question 9====================================
for i in range(1, 7):
    if i == 4:
        continue
    print(i)

#Output
# 1
# 2
# 3
# 5
# 6


#==================================Question 10====================================
for ch in "education":
    if ch in "aeiou":
        continue
    print(ch, end="")

#Output
# dctn


#==================================Question 11====================================
n = 0

while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)

# Output
# 1
# 2
# 4
# 5

#B2
#==================================Question 12====================================
n = int(input("Enter any number:- "))
for i in range(1,n+1):
    if i%3==0:
        continue
    print(i)

#==================================Question 13====================================
str1 = input("enter any string:- ")
ch = input("Enter any one character:- ")

for i in str1:
    if i == ch:
        continue
    print(i,end="")

#==================================Question 14====================================
marks = map(int,input("Enter your marks of each subject separated by space:- ").split())

for i in marks:
    if i < 40:
        continue
    print(i)


B3
#==================================Question 15====================================
for i in range(1, 5):
    if i == 2:
        continue
    print("A", i)        #Skipped when i==2
    print("B", i)        #Skipped when i==2

#Output
# A 1
# B 1
# A 3
# B 3
# A 4
# B 4

#==================================Question 16====================================
n = 1

while n <= 5:
    if n == 3:
        n += 1
        continue
    print(n)
    n += 1
    

#Output
1
2
3
5

#==================================Question 17====================================
new = ""
word = input("Enter any word:- ").lower()
for i in word:
    if i in "aeiou":
        continue
    new += i

print(len(new))


#SECTION C
#C1
#Output predict
#==================================Question 18====================================
for i in range(1, 4):
    print(i)
else:
    print("Done")

# Output
# 1
# 2
# 3
# Done

#==================================Question 19====================================
for i in range(1, 5):
    if i == 2:
        continue
    print(i)
else:
    print("Completed")

#Output
# 1
# 3
# 4
# Completed

#==================================Question 20====================================
for i in range(1, 5):
    if i == 3:
        break
    print(i)
else:
    print("Completed")
print("Outside loop")

# Output
# 1
# 2
# Outside loop

#==================================Question 21====================================
for item in []:
    print("Inside")
else:
    print("Else block")

# Output
# Else block


#c2
#==================================Question 22====================================
numbers = map(int, input("Enter multiple numbers separated by space:- ").split())
target = int(input("Enter any one number to target in list:- "))

for i in numbers:
    if i == target:
        print("Found")
        break
else:
    print("Not found")

#==================================Question 23====================================
str2 = input("Enter any string:- ")
ch = input("Enter any one character:- ")

for i in str2:
    if i == ch:
        print("Character exists")
        break
else:
    print("Character missing")

#==================================Question 24====================================
n = int(input("Enter any number for check prime greater than 1:- "))

if n > 1:
    for i in range(2,n-1):
        if n % i == 0:
            print("Not prime")
            break
    
    else:
        print("Prime")
else:
    print("not prime, invalid value") 


#C3
#==================================Question 25====================================
values = [2, 4, 6, 8]

for value in values:
    if value % 2 != 0:
        print("Odd found")
        break
else:
    print("All are even")

# Output
# All are even


#==================================Question 26====================================
#CASE A
for x in range(3):
    continue
else:
    print("A")
#Here else part execute because for loop iterate completely

#CASE B
for x in range(3):
    break
else:
    print("B")

#CASE C
for x in range(0):
    print(x)
else:
    print("C")

#Here also else part execute because for loop iterate completely

#==================================Question 27====================================
count = 0
str3 = input("Enter any string:- ")
ch = input("enter any one character to check for repeatition:- ")

for i in str3:
    if i == ch:
        count += 1
        if count > 1:
            print("reapeated")
            break
else:
    print("No repeated character")


#SECTION D
#D1
#Output prediction
#==================================Question 28====================================
for i in range(1, 4):
    if i == 2:
        pass
    print(i)

#Output
# 1
# 2
# 3


#==================================Question 29====================================
x = 10

if x > 5:
    pass

print("Finished")

#Output
# Finished


#==================================Question 30====================================
for letter in "cat":
    pass

print("Loop ended")

# Output
# Loop ended


#D2
#==================================Question 31====================================
for i in range(1,6):
    if i % 2 == 0:
        pass
    print(i)

#==================================Question 32====================================
option = int(input("Enter menu option:- "))
if option == 1:
    print("The message for option 1 ")
elif option == 2:
    pass
elif option == 3:
    print("No action for option 3")
else:
    print("The message for an unknown option")

print("Program closed")

#D3
#==================================Question 33====================================
# Program A
for i in range(1, 5):
    if i == 3:
        pass
    print(i)

#Ouutput
# 1
# 2
# 3
# 4


# program B
for i in range(1, 5):
    if i == 3:
        continue
    print(i)

#Ouutput
# 1
# 2
# 4


#==================================Question 34====================================
for i in range(1, 6):
    if i == 3:
        continue            # here we only put continue statement because we want output in which 3 is missing. 
    print(i)                # and not use pass and break bacause these statement not give favorable outputs.


#SECTION E
#==================================Question 35====================================
for i in range(1, 6):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
else:                        # else part not execute bacause loop break without complete all iteration.
    print("Finished")

#Output
# 1
# 3


#==================================Question 36====================================
numbers = map(int, input("Enter numbers separated by space:- ").split())
target = int(input("Enter any one number for find in list:- "))

for i in numbers:
    if i < 0:
        continue
    if i == target:
        print("Target Found")
        break
else:
    print("Target Not found")

#==================================Question 37====================================
integer = map(int, input("Enter numbers separated by space:- ").split())

for i in integer:
    if i == 0:
        continue
    if i  < 0:
        break
    print(i)
else:
    print("All value processed")



#==================================Question 38====================================

for row in range(1, 4):
    for col in range(1, 4):
        if col == 2:
            continue
        if row == 3:
            break
        print(row, col)
    else:
        print("Inner loop completed")

# Output
# 1 1
# 1 3
# Inner loop completed
# 2 1
# 2 3
# Inner loop completed


#==================================Question 39====================================
numbers = map(int, input("Enter numbers separated by space:- ").split())

for i in numbers:
    if i < 0:
        continue
    if i % 4 == 0 and i % 6 == 0:
        print("Found:",i)
        break
else:
    print("No matching number")


#==================================Question 40====================================
# 1. using break
# 2. using continue
# 3. using for-else
# 4. using pass
# 5. using continue
# 6. using break
# 7. using break and for-else
# 8. using pass