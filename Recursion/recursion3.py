#===================================Question 1=================================
def p_message(message,n):
    if n == 0:
        return
    print(message)
    p_message(message,n-1)

p_message("Hello",3)

#===================================Question 2=================================
def even(n):
    if n == 0:
        return
    even(n-1)
    if n%2==0:
        print(n)

even(15)

#===================================Question 3=================================
add = 0
def sum_odd(n):
    global add
    if n==0:
        return 
    if n%2 != 0:
        add += n
    sum_odd(n-1)
    return add

print(sum_odd(21))

#===================================Question 4=================================
a = 0
def count(n,target):
    global a
    if n == 0:
        return
    if n%10 == target:
        a += 1
    count(n//10,target)
    return a

print(count(525255484855,5))


#===================================Question 5=================================
def digit_product(n):
    if n == 0:
        return 1
    return n%10 * digit_product(n//10)

print(digit_product(23854))


#===================================Question 6=================================
def first_digit(n):
    if n < 10:
        return n
    return first_digit(n//10)

print(first_digit(5884))


#===================================Question 7=================================
flag = False
def find(n,target):
    global flag
    if n == 0:
        return
    if n%10 == target:
        flag = True
    find(n//10,target)
    return flag

print(find(4826 , 8))

#===================================Question 8=================================
def length(str1):
    if str1 == "":
        return 0
    return 1 + length(str1.replace(str1[0],"",1))

print(length("coding"))



def length(str2):
    if str2 == "":
        return 0
    return 1 + length(str2[1:])

print(length("coding"))


#===================================Question 9=================================
count = 0
def length(str1):
    global count
    if str1 == "":
        return 0
    if str1[0] in "aeiou":
        count += 1
    length(str1.replace(str1[0],"",1))
    return count
print(length("education"))

count2 = 0
def length(str2):
    global count2
    if str2 == "":
        return 0
    if str2[0] in "aeiou":
        count2 += 1
    length(str2[1:])
    return count2

print(length("coding"))

#===================================Question 10=================================
