#Section A — Understand Recursion
#================================Question 1=============================
def show(n):
    if n == 0:
        print("Stop")
        return

    print(n)
    show(n - 1)
    print(n)

show(2)

#Expected Output
# 2
# 1
# Stop
# 1
# 2

#================================Question 2=============================
def total(n):
    if n == 0:       #Base case
        return 0

    return n + total(n - 1)

#In this function base case stops recursion because when n equals to 0, condition true then function return 0  

#================================Question 3=============================
def count(n):
    if n == 0:
        return

    count(n + 1)

# this function does not reach its base case when called with count(2) because recursive case is not reach to base case condition 
# in this function recursive case must be decrease towards base case.
def count(n):
    if n == 0:
        return

    count(n - 1)
count(2)

#================================Question 4=============================
def answer(n):
    if n == 0:
        return 0

    return(n + answer(n - 1))

print(answer(3))


# this function return 6 when called as answer(3)



# Section B — Basic Recursive Problems
#================================Question 5=============================
def countdown(n):
    if n == 0:
        print("Done!")
        return
    print(n)
    countdown(n-1)

countdown(5)


#================================Question 6=============================
def countup(n):
    if n == 0:
        return

    countup(n-1)
    print(n)

countup(5)


#================================Question 7=============================
def sum_to(n):
    if n == 0:
        return 0
    return n + sum_to(n-1)

print(sum_to(5))
print(sum_to(0))

#================================Question 8=============================
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))
print(factorial(0))


#================================Question 9=============================
def digit_sum(n):
    if n < 10:
        return n
    return n%10 + digit_sum(n//10)

print(digit_sum(583))  # 16
print(digit_sum(7))    # 7
print(digit_sum(0))    # 0


#================================Question 10=============================
def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n-1)

print(power(2, 5))  # 32
print(power(9, 0))  # 1
print(power(3, 1))  # 3

#================================Question 11=============================
def count_digits(n):
    if n < 10:
        return 1
    
    return 1 + count_digits(n//10)

print(count_digits(5382))  # 4
print(count_digits(6))     # 1
print(count_digits(0))     # 1


# Section C — Apply and Analyze
#================================Question 12=============================
def reverse_text(n):
    if n == "":
        return ""
    return n[len(n)-1] + reverse_text(n[0:(len(n)-1)])

print(reverse_text("catpac"))  # "captac"
print(reverse_text("a"))    # "a"
print(reverse_text(""))     # ""


#================================Question 13=============================
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(0))  # 0
print(fibonacci(1))  # 1
print(fibonacci(6))  # 8