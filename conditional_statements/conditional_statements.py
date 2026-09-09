#Basic if
#===============================Question 1 ========================================
num = int(input("Enter a number:- "))

if num>10:
    print("The number is greater than 10")

#===============================Question 2 ========================================
age = int(input("Enter your age: "))

if age>= 18:
    print("Adult")

#===============================Question 3 ========================================
number = int(input("Enter a number:- "))
if number>0:
    print("The number is positive")

#===============================Question 4 ========================================
marks = int(input("Enter your marks:- "))
if marks >= 40:
    print("Pass")

#===============================Question 5 ========================================
number = int(input("Enter a number:- "))
if number == 0:
    print("zero")

#if-else
#===============================Question 6 ========================================
number = int(input("Enter a number:- "))
if number > 0:
    print("Positive")
else:
    print("Not positive")

#===============================Question 7 ========================================
your_age = int(input("Enter your age:- "))
if your_age >= 18:
    print("Adult")

else:
    print("Minor")

#===============================Question 8 ========================================
number = int(input("Enter any number:- "))
if number%2 == 0:
    print("Even")

else:
    print("odd")

#===============================Question 9 ========================================
marks = int(input("Enter your marks:- "))
if marks >= 40:
    print("Pass")

else:
    print("Fail")

#===============================Question 10 ========================================
a , b = map(int, input("Enter first and second number:- ").split())
if a>b:
    print("First number is greater")

else:
    print("Second number is greater")


#if-elif-else
#===============================Question 11 ========================================
marks = int(input("Enter your marks:- "))

if marks>=90 and marks<=100:
    print("A")

elif marks>=75 and marks<90:
    print("B")

elif marks>=60 and marks<75:
    print("C")

elif marks>=40 and marks<60:
    print("D")

elif marks>=0 and marks<40:
    print("F")
else:
    print("Invalid marks")
    

#===============================Question 12 ========================================
number = int(input("Enter a number:- "))
if number>0:
    print("Positive")
elif number<0:
    print("Negative")
else:
    print("Zero")


#===============================Question 13 ========================================
week_day = int(input("Enter a number between 1 to 5:- "))
if week_day == 1:
    print("Monday")

elif week_day == 2:
    print("Tuesday")

elif week_day == 3:
    print("Wednesday")

elif week_day == 4:
    print("Thursday")

elif week_day == 5:
    print("Friday")

else:
    print("Other")

#===============================Question 14 ========================================
student_marks = int(input("Enter your marks:- "))

if student_marks>=90 and student_marks<=100:
    print("Excellent")

elif student_marks>=75 and student_marks<90:
    print("Good")

elif student_marks>=40 and student_marks<75:
    print("pass")

elif student_marks>=0 and student_marks<40:
    print("Fail")

else:
    print("Invalid marks")

#===============================Question 15 ========================================
number = int(input("Enter a number:- "))
if number == 1:
    print("1")

elif number == 2:
    print("2")

elif number == 3:
    print("3")

else:
    print("Other")


#Nested conditions
#===============================Question 16 ========================================
age_check = int(input("Enter your age:- "))
if age_check>=18:
    if age_check<=60:
        print("Between 18 to 60")
    else:
        print("Greater than 60")

else:
    print("Not between 18 to 60")

#===============================Question 17 ========================================
exam_marks = int(input("Enter your marks:- "))
if exam_marks>=40:
    if exam_marks<=75:
        print("Good")
    else:
        print("passed")

else:
    print("Failed")

#===============================Question 18 ========================================
number = int(input("Enter a number:- "))
if number>0:
  
    if number > 100:
        print("Positive and Greater than 100")
    else:
        print("Positive and Less than or equal to 100")

else:
    print("Not Positive")


#===============================Question 19 ========================================
age = int(input("Enter your age:- "))
if age>=18:
   
    if age>=60:
        print("Senior Citizen")
    else:
        print("between 18 to 60")

else:
    print("Minor")

#===============================Question 20 ========================================
number = int(input("Enter a number:- "))
if number!=0:
   
    if number > 0:
        print("Positive")
    else:
        print("Negative")

else:
    print("Zero")      


#Multiple conditions  
#===============================Question 21 ========================================
age = int(input("Enter your age:- "))
marks = int(input("Enter your marks:- "))
if age>=18:
    if marks>=40:
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")


#===============================Question 22 ========================================
number = int(input("Enter a number:- "))            #number = int(input("Enter a number:- "))
if number< 10:                                      #if number < 10 or number > 100:
    print("special")                                    #print("special")
else:                                               #else:
    if number> 100:                                     #print("not special")
        print("special")
    else:
        print("not special")

#===============================Question 23 ========================================
user_age = int(input("Enter user's age:- "))
has_id = input("has_id?  (True/False): ").lower().strip()

if user_age >= 18:
    if has_id == "true" :
        print("Allowed")

    elif has_id != "true":
        print("Not Allowed")
    else:
        print("Enter valid value")
  
else:
    print("Not allowed")

#===============================Question 24 ========================================
first_number , second_number = map(int, input("Enter first and second number respectively:- ").split())
if first_number > 10:
    if second_number > 10:
        print("Both are greater than 10")
    else:
        print("only first number is greater than 10")
else:
    print("Both are smaller than 10")


#===============================Question 25 ========================================
number = int(input("Enter a number:- "))
if number < 0 or number > 100:
    print("condition satisfied")

else:
    print("not satisfied")

#conditions with logical operators
#===============================Question 26 ========================================
is_closed = False

if not is_closed:
    print("open")
#===============================Question 27 ========================================
number = int(input("Enter any number:- "))
if number > 10 and number < 50:
    print("number is between 10 and 50")

else:
    print("not between 10 and 50")


#===============================Question 28 ========================================
number = int(input("Enter any number:- "))
if number <=10 or number >= 50:
    print("number is outside the range 10 to 50")
else:
    print("number is between 10 and 50")


#===============================Question 29 ========================================
is_student = input("Are you a student? (True/False): ").lower().strip()
has_id = input("Do you have an ID? (True/False): ").lower().strip()
has_ticket = input("Do you have a ticket? (True/False): ").lower().strip()

if is_student == "true" and  has_id == "true"  and  has_ticket == "true":
    print("Allowed")

elif is_student != "true" and  has_id != "true"  and  has_ticket != "true":
    print("Not Allowed")

else:
    print("Enter valid value")


#===============================Question 30 ========================================
age = int(input("Enter your age:- "))
marks = int(input("Enter your marks:- "))
has_id = input("Do you have a ID?  (True/False): ") == "True"

if age >= 18 and marks >=40 and has_id:
    print("Eligible")

else:
    print("Not eligible")

# here 'and' is appropriate in that solution because we wnat to print output when all three condition is true so we use and logical operator.