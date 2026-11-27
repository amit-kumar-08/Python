# Lambda Functions
#====================================Question 1=================================
add = lambda a, b: a + b

print(add(10, 20))


#====================================Question 2=================================
square = lambda number: number * number

print(square(6))


#====================================Question 3=================================
cube = lambda n: n*n*n

print(cube(3))


#====================================Question 4=================================
check = lambda n: "Even" if n % 2 == 0 else "Odd"

print(check(8))
print(check(7))


#====================================Question 5=================================
greater = lambda a, b: a if a > b else b

print(greater(45, 32))


#====================================Question 6=================================
convert = lambda c: (c * 9/5) + 32

print(convert(25))


#====================================Question 7=================================
length = lambda str1: len(str1)

print(length("Python"))


#====================================Question 8=================================
uppercase = lambda text: text.upper()

print(uppercase("hello world"))


#====================================Question 9=================================
last_chr = lambda str2: str2[-1]

print(last_chr("Coding"))


#====================================Question 10=================================
final_price = lambda price,discount: price - (price*discount/100) 

print(final_price(2000, 10))


#================Using if elif else=========
check = lambda a: "positive" if a>0 else "negative" if a<0 else "zero"

print(check(0))