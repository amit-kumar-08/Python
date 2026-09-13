#Part 3 — String Creation and Basic Operations

#================================ Task 1 ===================================
'''my_name = "Amit kumar"
my_city = "bangalore"
my_fav_programming_lan = 'python'
short_message = 'python is beginner-friendly language'

print(my_name)
print(my_city)
print(my_fav_programming_lan)
print(short_message)

#================================ Task 2 ===================================
empty_str = ""

print(empty_str)
print(len(empty_str))
print(type(empty_str))

#================================ Task 3 ===================================
a = "python programming"

print(a)
print(len(a))
print(a[0])
print(a[len(a)-1])
print(a[2])
print(a[len(a)-2])

#================================ Task 4 ===================================
b = "programming"

print(b[0])
print(b[1])
print(b[4])
print(b[len(b)-1])

#================================ Task 5 ===================================
b = "programming"

print(b[-1])
print(b[-2])
print(b[-3])
print(b[-len(b)])

#================================ Task 6 ===================================
name = "Amit kumar"

print(name[0])
print(name[-1])
print(name[5])

#================================ Task 7 ===================================
c = "python programming"

print(c[:6])
print(c[7:])
print(c[:])
print(c[0:5])
print(c[13:])

#================================ Task 8 ===================================
a = "ABCDEFGHIJKL"

print(a[::2])
print(a[::3])
print(a[1:8:2])
print(a[::-1])

#================================ Task 9 ===================================
a = "python programming"

print(a[-5:])
print(a[-10:])
print(a[::-1])

#================================ Task 10 ===================================
u = "characters"

print(u[:3])
print(u[-3:])
print(u[::2])
print(u[::-1])
print(u[1:-1])

#================================ Task 11 ===================================
a = "python"
b = "python is high level interpreted programming language"
c = "python is    user-friendly programming        language"

print(len(a))
print(len(b))
print(len(c))

#================================ Task 12 ===================================
text = "Python Programming"

print(len(text))
print(text[17])

#================================ Task 13 ===================================
first_name = "Amit"
last_name = "kumar"

full_name = first_name+" "+last_name

print(full_name)

#================================ Task 14 ===================================
name = "Amit kumar"
age = "18"
city = "bangalore"
prog_lang = "python"

print("my self "+name+" and I'm "+age+" years old. I'm from "+city+" and learning "+prog_lang)

#================================ Task 15 ===================================
a = "python"
b = 18

#print(a+b)    TypeError

b = str(b)
print(a+b)

#================================ Task 16 ===================================
p = "@python"

print(p*3)
print(5*p)
print(10*p)

#================================ Task 17 ===================================
a ="*"

print(a*10)

#================================ Task 18 ===================================
c = "python programming language"

print(c.upper())
print(c.lower())
print(c.capitalize())
print(c.title())
print(c.swapcase())

#================================ Task 19 ===================================
a = "Python"
b = "python"

print(a==b)

print(a.casefold()==b.casefold())

#================================ Task 20 ===================================
v = "Python is a programming language"

print("Python" in v)
print("programming" in v)
print("Java" in v)
print("language" in v)

#================================ Task 21 ===================================
v = "Python is a programming language"

print(v.find("Python"))
print(v.find("programming"))
print(v.find("language"))
print(v.find("Java"))

#================================ Task 22 ===================================
v = "Python is a programming language"

print(v.index("Python"))
print(v.index("programming"))
print(v.index("language"))
#print(v.index("Java"))     #ValueError

#================================ Task 23 ===================================
b = "banana"

print(b.count("a"))
print(b.count("n"))
print(b.count("b"))

#================================ Task 24 ===================================
filename = "student_notes.pdf"

print(filename.startswith("student"))
print(filename.endswith(".pdf"))
print(filename.endswith(".txt"))

#================================ Task 25 ===================================
text = "I am learning Java"

print(text.replace("Java","Python"))

#================================ Task 26 ===================================
text = "apple apple apple"

print(text.replace("apple","mango"))

#================================ Task 27 ===================================
text = "apple apple apple"

print(text.replace("apple","mango",1))

#================================ Task 28 ===================================
text = "Python"

text.upper()

print(text)

text = text.upper()

print(text)

#================================ Task 29 ===================================
text = "   Python Programming   "

print(text.strip())
print(text.lstrip())
print(text.rstrip())

#================================ Task 30 ===================================
a = input("Enter your name :- ")

print(a.strip())

#================================ Task 31 ===================================
b = "Python is easy to learn"

print(b.split())

#================================ Task 32 ===================================
c = "apple,banana,mango,orange"

print(c.split(","))

#================================ Task 33 ===================================
words = ["Python", "is", "easy"]

print(" ".join(words))

#================================ Task 34 ===================================
words = ["Python", "is", "easy"]

print("-".join(words))
print("/".join(words))

#================================ Task 35 ===================================
name = "Amit kumar"
age = "18"
city = "bangalore"

print(f"My self {name} and I'm {age} Years old. I'm from {city}")

#================================ Task 36 ===================================
a = 10
b = 20

print(f"The sum is {a+b}")

#================================ Task 37 ===================================
#text = "Python"
#print(text[20])    #indexError

#corrected order
text = "python"
print(text[5])


#text = "Python"
#text[0] = "J"    #TypeError 


#age = 20
#print("Age: " + age)    #TypeError

age = 20
print("Age: " , age)

#text = "Python"
#print(text.index("Java"))   #ValueError

text = "Python"
print(text.index("Python"))'''


#================================ Task 38 ===================================
name = input("Enter your full name: ")

# 1. Remove extra spaces from beginning and end
cleaned_name = name.strip()

# 2. Display original input
print("Original name:", name)

# 3. Display cleaned name
print("Cleaned name:", cleaned_name)

# 4. Display name in uppercase
print("Uppercase:", cleaned_name.upper())

# 5. Display name in lowercase
print("Lowercase:", cleaned_name.lower())

# 6. Display name in title case
print("Title case:", cleaned_name.title())

# 7. Display length of the name
print("Length:", len(cleaned_name))

# 8. Display first character
print("First character:", cleaned_name[0])

# 9. Display last character
print("Last character:", cleaned_name[-1])

# 10. find particular character
print("find character:", cleaned_name.find("a"))

#================================ Task 39 ===================================
sentence = input("Enter a sentence: ")

# 1. Original sentence
print("Original sentence:", sentence)

# 2. Number of characters
print("Number of characters:", len(sentence))

# 3. Number of words
words = sentence.split()
print("Number of words:", len(words))

# 4. First character
print("First character:", sentence[0])

# 5. Last character
print("Last character:", sentence[-1])

# 6. Sentence in uppercase
print("Uppercase:", sentence.upper())

# 7. Sentence in lowercase
print("Lowercase:", sentence.lower())

#8. Sentence in title case
print("Title case:", sentence.title())

#9. "Python" in Sentence 
print("python" in sentence)

#10. character occurs
print("character occurs:", sentence.count("a"))


#================================ Task 40 ===================================
# Taking information from the user

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
city = input("Enter your city: ")
course = input("Enter your course: ")
age = int(input("Enter your age: "))


# 1. Remove unnecessary spaces from text inputs

first_name = first_name.strip()
last_name = last_name.strip()
city = city.strip()
course = course.strip()


# 2. Create the full name

full_name = first_name + " " + last_name


# 3. Full name in title case

print("Title case:", full_name.title())


# 4. Full name in uppercase

print("Uppercase:", full_name.upper())


# 5. Full name in lowercase

print("Lowercase:", full_name.lower())


# 6. Length of the full name

print("Length of full name:", len(full_name))


# 7. First character of the full name

print("First character:", full_name[0])


# 8. Last character of the full name

print("Last character:", full_name[-1])


# 9. Display city and course

print("City:", city)
print("Course:", course)


# 10. Display age using f-string

print(f"Age: {age}")


# 11. Check whether the course contains "Python"

print ("Python" in course)

# 12. Replace one word in the course name

new_course = course.replace("Python", "Java")
print("Updated course:", new_course)


# 13. Number of words in the course name

number_of_words = len(course.split())
print("Number of words in course:", number_of_words)