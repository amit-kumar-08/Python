#============================== Problem 1 =====================================
i = 0
while i < 5:
    print("Hello")

    i += 1


#============================== Problem 2 =====================================
i = 0
while i <= 9:
    print(i, end=" ")
    i += 1
print()

#============================== Problem 3 =====================================
j = 1
while j < 11:
    print(j)

    j += 1


#============================== Problem 4 =====================================
i = 10
while i >=1:
    print(i)
    i -= 1

#============================== Problem 5 =====================================
i = 5
while i <= 50:
    print(i)

    i += 5


#============================== Problem 6 =====================================
i = 2
while i <= 20:
    print(i)

    i += 2

#============================== Problem 7 =====================================
i = 1
while i < 20:
    print(i)
    i += 2

#============================== Problem 8 =====================================
i = 3
while i <= 18:
    print(i, end=" ")

    i += 3
print()

#============================== Problem 9 =====================================
i = 20
while i >= 2:
    print(i)

    i -= 2


#============================== Problem 10 =====================================
n = int(input("Enter any number:- "))
i = 1
while i <= n:
    print(i)

    i += 1

#============================== Problem 11 =====================================
n = int(input("Enter any number:- "))
i = 1
while i <= n:
    if i%2 == 0:
        print(i)
    i += 1

#============================== Problem 12 =====================================
n = int(input("Enter any number:- "))
i = 1
while i <= n:
    if i%2 != 0:
        print(i)

    i += 1

#============================== Problem 13 =====================================
n = int(input("Enter any number:- "))
i = 1
while i <= n:
    if i%3 == 0:
        print(i)
    i += 1

#============================== Problem 14 =====================================
n = int(input("Enter any number:- "))
i = 1
while i <= n:
    if i%2 == 0 and i%3 == 0:
        print(i)
    i += 1


#============================== Problem 15 =====================================
n = int(input("Enter any number:- "))
i = 1
count = 0
while i <= n:
    if i%2 == 0:
        count += 1
    i += 1
print(f"Total even number from 1 to {n} are {count}")

#============================== Problem 16 =====================================
n = int(input("Enter any number:- "))
i = 1
total = 0
while i <= n:
    total += i
    i += 1

print(f"Total sum of number from 1 to {n} is {total}")


#============================== Problem 17 =====================================
n = int(input("Enter any number:- "))
i = 1
total = 0
while i <= n:
    if i%2 == 0:
        total += i
    i += 1
print(f"Total addition of even number from 1 to {n} are {total}")


#============================== Problem 18 =====================================
n = int(input("Enter any number:- "))
i = 1
total = 0
while i <= n:
    if i%2 != 0:
        total += i
    i += 1
print(f"Total addition of odd number from 1 to {n} are {total}")

#============================== Problem 19 =====================================
n = int(input("Enter any number:- "))
i = 1
while i <= 10:
    print(i*n)

    i += 1


#============================== Problem 20 =====================================
n = int(input("Enter any number:- "))
i = 1
total = 1
while i <= n:
    total *= i
    i += 1

print(f"Total sum of multiplication of number from 1 to {n} is {total}")


#============================== Problem 21 =====================================
word = input("Enter any word or sentence:- ")
i = 0
while i < len(word):
    print(word[i])

    i += 1

#============================== Problem 22 =====================================
word = input("Enter any word or sentence:- ")
i = 0
while i < len(word):
    print(word[i], end="")

    i += 1
print()

#============================== Problem 23 =====================================
word = input("Enter any word or sentence:- ")
i = 0
char_count = 0
while i < len(word):
    char_count += 1

    i += 1
print(f"Total number of character in {word} are {char_count}.")


#============================== Problem 24 =====================================
word = input("Enter any word or sentence:- ").lower()
i = 0
char_a_count = 0
while i < len(word):
    if word[i] == "a":
        char_a_count += 1

    i += 1
print(f"Total number of character 'a' in {word} are {char_a_count}.")


#============================== Problem 25 =====================================
word = input("Enter any word or sentence:- ")
i = 0
char_upper_count = 0
while i < len(word):
    if word[i].isupper():
        char_upper_count += 1

    i += 1
print(f"Total number of uppercase character in {word} are {char_upper_count}.")


#============================== Problem 26 =====================================
row = 1
while row <= 3:
    
    column = 1
    while column <=4:
        print("*" , end="")

        column += 1
    
    row += 1
    print()


#============================== Problem 27 =====================================
row = 1
while row <= 4:
    
    column = 1
    while column <=5:
        print("*" , end="")

        column += 1
    
    row += 1
    print()


#============================== Problem 28 =====================================
row = 1
while row <= 5:
    
    column = 1
    while column <= row:
        print("*" , end="")

        column += 1
    
    row += 1
    print()


#============================== Problem 29 =====================================
row = 1
while row <= 5:
    
    column = 1
    while column <= row:
        print(column , end="")

        column += 1
    
    row += 1
    print()


#============================== Problem 30 =====================================
row = 1
while row <= 5:
    
    column = 1
    while column <= 10:
        print(row*column , end=" ")

        column += 1
    
    row += 1
    print()


#============================== Final challenge =====================================
n = int(input("Enter any number for pattern print:- "))
row = 1
while row <= n:
    
    column = 1
    while column <= row:
        print(column , end="")

        column += 1
    
    row += 1
    print()