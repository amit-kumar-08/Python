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




#practice Questions
#=================1==================
multiply = lambda a ,b: a*b

print(multiply(5,9))

#=================2=================
cube = lambda n: n*n*n

print(cube(5))

#=================3=================
check = lambda a: "positive" if a>0 else "negative" if a<0 else "zero"

print(check(45))

#=================4=================
smaller = lambda a, b: a if a < b else b

print(smaller(45, 32))

#=================5=================
area = lambda l,b : f"{l*b} Sq unit"

print(area(10,5))

#=================6=================
lowercase = lambda text: text.lower()

print(lowercase("HELLO WORLD"))

#=================7=================
check_vowel = lambda a : "vowel" if a in "aeiou" else "consonant"

print(check_vowel("e"))

#=================8=================
word = "coding"

result = map(lambda ch: ch.upper(), word)

print("".join(result))

#=================9=================
word = "programming"

result = filter(lambda ch: ch in "aeiou", word)

print("".join(result))