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
