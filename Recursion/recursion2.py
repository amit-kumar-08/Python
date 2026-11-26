# Intermediate Recursion Assignments
#================================Question 1=============================
# 1. Sum of Digits at Even Positions

def sum_even(n):
    if n < 10:
        return n
    s = n%100
    return s//10 + sum_even(n//100)

print(sum_even(58324656))  #17
print(sum_even(583246))    #12


#================================Question 2=============================
# Reverse a Number Without Converting It to a String

def reverse(n , rev=0):
    if n == 0:
        return rev
    return reverse(n//10, rev*10+ n%10)
print(reverse(4827))


def reverse2(n):
    if n == 0:
        return
    print(n%10, end="")
    return reverse2(n//10)

reverse2(48277)
print()


total = 0
def reverse3(n):
    global total
    if n == 0:
        return 
    total = total*10 + (n%10)
    reverse3(n//10)
    return total

print(reverse3(8957))

#================================Question 3=============================
