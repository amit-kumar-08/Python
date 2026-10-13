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