#Practice Problems
#Beginner
#===================================Question 1===================================
def address():
    city = "Bangalore"
    print(city)

address()

#===================================Question 2===================================
school = "JNV"
def sch():
    print(school)

sch()

#===================================Question 3===================================
if True:
    name = "Amit"

print(name)

#===================================Question 4===================================
for number in range(5):
    pass

print(number)

#===================================Question 5===================================


#Intermediate
#Pridict Output
#===================================Question 6===================================
value = 100
def test():
    value = 200
    print(value)
test()
print(value)

#Expected Output
# 200
# 100

#===================================Question 7===================================
clicks = 0
def click():
    clicks += 1

#Expected Output
# nothing


#===================================Question 8===================================
# name = "Asha"
# def show():
#     print(name)
#     name = "Ravi"
# show()

#Expected Output
# UnboundLocalError


#===================================Question 9===================================
def outer():
    message = "enclosing"

    def inner():
        print(message)

    inner()

outer()


#===================================Question 10===================================
def make_list():
    list = [1,2,8,10]
    return list

new_list = make_list()
new_list.append(5)

print(new_list)


#===================================Question 11===================================
def make_counter():
    count = 0
    def incriment():
        nonlocal count
        count += 1
        return count

    return incriment

counter = make_counter()
print(counter())
print(counter())
print(counter())

#===================================Question 12===================================
x = 1
def outer():
    x = 2
    def inner():
        x = 3
        print(x)
    
    inner()
    print(x)

outer()
print(x)

# Expected Output
# 3
# 2
# 1

#===================================Question 13===================================



#===================================Question 14===================================
def outer():
    message = "Hello, Amit!"

    def inner():
        print(message)

    return inner


my_function = outer()

my_function()

#message variable remains avialable because the concept of the closure.

#===================================Question 15===================================
# Variable names such as list, str, and sum should usually be avoided because they are predefined 
# built-in names in Python. Using them as variable names overwrites their original references and 
# makes their built-in functions or classes inaccessible through those names. Therefore, we should 
# use meaningful alternative names to avoid unexpected errors and improve code readability.