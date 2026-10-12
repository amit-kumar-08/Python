#===============================Problem 1=========================================

# print('''
# ===Menu===
# 1. Pizza
# 2. Burger
# 3. Pasta
# 4. Sandwich
# ''')

# choice = int(input("Enter your choice:- "))

# match choice:
#     case 1:
#         print("You Selected Pizza")
    
#     case 2:
#         print("You Selected Burger")

#     case 3:
#         print("You Selected Pasta")

#     case 4:
#         print("You Selected Sandwich")

#     case _:
#         print("Invalid Menu Choice")

# #===============================Problem 2=========================================
# print('''
# ===Mobile Setting===
# 1 → Wi-Fi
# 2 → Bluetooth
# 3 → Mobile Data
# 4 → Airplane Mode
# 5 → Exit
# '''
# )
# choice = int(input("Enter your choice:- "))

# match choice:
#     case 1:
#         print("Wi-Fi Selected")
#     case 2:
#         print("Bluetooth Selected")
#     case 3:
#         print("Mobile Data Selected")
#     case 4:
#         print("Airplane Mode Selected")
#     case 5:
#         print("Exit Selected")
#     case _:
#         print("Invalid setting")

# #===============================Problem 3=========================================
# print('''
# ===ATM Main Menu===
# 1 → Check Balance
# 2 → Withdraw Money
# 3 → Deposit Money
# 4 → Change PIN
# 5 → Exit
# '''
# )
# choice = int(input("Enter your choice:- "))

# match choice:
#     case 1:
#         print("Check Balance Selected")
#     case 2:
#         print("Withdraw Money Selected")
#     case 3:
#         print("Deposit Money Selected")
#     case 4:
#         print("Change PIN Selected")
#     case 5:
#         print("Exit Selected")
#     case _:
#         print("Invalid choice")

# #===============================Problem 4=========================================

# print('''
# ===Traffic Signal===
# red
# yellow
# green
# ''')

# choice = input("Enter signal:- ").strip().lower()

# match choice:
#     case "red":
#         print("Stop")
    
#     case "Yellow":
#         print("Wait")

#     case "green":
#         print("Go")

#     case _:
#         print("Invalid Signal")

# #===============================Problem 5=========================================
# print('''
# ===Student Portal===
# 1 → View Profile
# 2 → View Courses
# 3 → View Marks
# 4 → View Attendance
# 5 → Logout
# '''
# )
# choice = int(input("Enter your choice:- "))

# match choice:
#     case 1:
#         print("Opening Profile")
#     case 2:
#         print("Opening Courses")
#     case 3:
#         print("Opening Marks")
#     case 4:
#         print("Opening Attendance")
#     case 5:
#         print("Logout")
#     case _:
#         print("Invalid choice")

# #===============================Problem 6=========================================
# print('''
# ===Online Shoping Menu===
# 1 → Electronics
# 2 → Clothing
# 3 → Books
# 4 → Grocery
# 5 → Exit
# '''
# )
# choice = int(input("Enter category:- "))

# match choice:
#     case 1:
#         print("Opening Electronics")
#     case 2:
#         print("Opening Clothing")
#     case 3:
#         print("Opening Books")
#     case 4:
#         print("Opening Grocery")
#     case 5:
#         print("Exit")
#     case _:
#         print("Invalid category")

# #===============================Problem 7=========================================
# print('''
# ===Bank Service===
# 1 → Account Balance
# 2 → Mini Statement
# 3 → Fund Transfer
# 4 → Bill Payment
# 5 → Customer Support
# '''
# )
# choice = int(input("Enter your choice:- "))

# match choice:
#     case 1:
#         print("Opening Account Balance")
#     case 2:
#         print("Opening Mini Statement")
#     case 3:
#         print("Opening Fund Transfer")
#     case 4:
#         print("Opening Bill Payment")
#     case 5:
#         print("Opening Customer Support")
#     case _:
#         print("Invalid Service")

# #===============================Problem 8=========================================
# print('''
# ===Movie Booking Menu===
# 1 → Morning Show
# 2 → Afternoon Show
# 3 → Evening Show
# 4 → Night Show
# '''
# )
# choice = int(input("Enter your choice:- "))

# match choice:
#     case 1:
#         print("Morning Show Selected")
#     case 2:
#         print("Afternoon Show Selected")
#     case 3:
#         print("Evening Show Selected")
#     case 4:
#         print("Night Show Selected")
#     case _:
#         print("Invalid choice")

# #===============================Problem 9=========================================

# print('''
# ===Weather===
# sunny
# rainy
# cloudy
# snowy
# ''')

# choice = input("Enter Weather:- ").strip().lower()

# match choice:
#     case "sunny":
#         print("Wear sunglasses")
    
#     case "rainy":
#         print("Carry an umbrella")

#     case "cloudy":
#         print("Weather may change")

#     case "snowy":
#         print("Wear warm clothes")

#     case _:
#         print("Unknown Weather")

# #===============================Problem 10=========================================

# print('''
# ===Payment Method===
# upi
# card
# cash
# wallet
# ''')

# choice = input("Enter Payment method:- ").strip().lower()

# match choice:
#     case "upi":
#         print("UPI Payment Selected")
    
#     case "card":
#         print("CARD payment selected")

#     case "cash":
#         print("CASH payment selected")

#     case "wallet":
#         print("WALLET payment selected")

#     case _:
#         print("Invalid payment method")


# #===============================Problem 11=========================================

# print('''
# ===Extension===
# pdf
# jpg
# png
# mp3
# mp4
# ''')

# choice = input("Enter extension:- ").strip().lower()

# match choice:
#     case "pdf":
#         print("Document File")
    
#     case "jpg":
#         print("Image file")

#     case "png":
#         print("Image file")

#     case "mp3":
#         print("Audio file")
    
#     case "mp4":
#         print("video file")

#     case _:
#         print("Unknown File Type")

# #===============================Problem 12=========================================

# print('''
# ===User role===
# admin
# teacher
# student
# guest
# ''')

# choice = input("Enter Your role:- ").strip().lower()

# match choice:
#     case "admin":
#         print("Full Access")
    
#     case "teacher":
#         print("Teacher Dashboard")

#     case "student":
#         print("Student Dashboard")

#     case "guest":
#         print("Limited Access")
    
#     case _:
#         print("Invalid Role")

#===============================Problem 13=========================================
print('''
===week day===
1 → Monday
2 → Tuesday
3 → Wednesday
4 → Thursday
5 → Friday
6 → Saturday
7 → Sunday
'''
)
choice = int(input("Enter day number:- "))

match choice:
    case 1|2|3|4|5:
        print("Weekday")
    case 6|7:
        print("Weekend")
    case _:
        print("Invalid day")
        
#===============================Problem 14=========================================
print('''
===Priority===
1 → Low
2 → Medium
3 → High
4 → Critical
'''
)
choice = int(input("Enter Priority number:- "))

match choice:
    case 1|2:
        print("Normal Priority")
    case 3|4:
        print("Urgent Priority")
    case _:
        print("Invalid priority")

#===============================Problem 15=========================================
print('''
===Membership levels===
1 → Bronze
2 → Silver
3 → Gold
4 → Platinum
'''
)
choice = int(input("Enter Priority number:- "))

match choice:
    case 1|2:
        print("Basics Membership")
    case 3|4:
        print("Premium Membership")
    case _:
        print("Invalid Membership level")

#===============================Problem 16=========================================
choice=int(input("1.Student\n2.Teacher"))
match choice:
    case 1:
        status=int(input("1.View Courses\n2.View Marks\nView Attendance\nEnter Any Serial Number"))
        match status:
            case 1:
                print("Opening Courses")
            case 2:
                print("Opening Marks")
            case 3:
                print("Opening Attendence")
            case _:
                print("Invalid Input")
    case 2:
        status=int(input("1.View Students\n2.Enter Marks\nView Attendance\nEnter Any Serial Number"))
        match status:
            case 1:
                print("Opening Students Informance")
            case 2:
                print("Enter Marks")
            case 3:
                print("View Attendance")
            case _:
                print("Invalid Input")


#===============================Problem 17=========================================
account=int(input("1.Savings\n2.Current\nEnter Account Type: "))

match account:
    case 1:
        operation=int(input("1.Check Balance\n2.Deposit\n3.Withdraw\nEnter Operation: "))

        match operation:
            case 1:
                print("Savings Account")
                print("Check Balance Selected")
            case 2:
                print("Savings Account")
                print("Deposit Selected")
            case 3:
                print("Savings Account")
                print("Withdraw Selected")
            case _:
                print("Invalid Input")

    case 2:
        operation=int(input("1.Check Balance\n2.Deposit\n3.Withdraw\nEnter Operation: "))

        match operation:
            case 1:
                print("Current Account")
                print("Check Balance Selected")
            case 2:
                print("Current Account")
                print("Deposit Selected")
            case 3:
                print("Current Account")
                print("Withdraw Selected")
            case _:
                print("Invalid Input")

    case _:
        print("Invalid Input")


#===============================Problem 18=========================================
category=int(input("1.Electronics\n2.Clothing\nEnter Category: "))

match category:
    case 1:
        product=int(input("1.Mobile\n2.Laptop\n3.Headphones\nEnter Product: "))

        match product:
            case 1:
                print("Mobile Selected")
            case 2:
                print("Laptop Selected")
            case 3:
                print("Headphones Selected")
            case _:
                print("Invalid Input")

    case 2:
        product=int(input("1.Shirt\n2.Jeans\n3.Shoes\nEnter Product: "))

        match product:
            case 1:
                print("Shirt Selected")
            case 2:
                print("Jeans Selected")
            case 3:
                print("Shoes Selected")
            case _:
                print("Invalid Input")

    case _:
        print("Invalid Input")


#===============================Problem 19=========================================
category=int(input("1.Vegetarian\n2.Non-Vegetarian\nEnter Category: "))

match category:
    case 1:
        food=int(input("1.Paneer\n2.Dal\n3.Veg Biryani\nEnter Food: "))

        match food:
            case 1:
                print("Paneer Selected")
            case 2:
                print("Dal Selected")
            case 3:
                print("Veg Biryani Selected")
            case _:
                print("Invalid Input")

    case 2:
        food=int(input("1.Chicken Biryani\n2.Chicken Curry\n3.Fish Fry\nEnter Food: "))

        match food:
            case 1:
                print("Chicken Biryani Selected")
            case 2:
                print("Chicken Curry Selected")
            case 3:
                print("Fish Fry Selected")
            case _:
                print("Invalid Input")

    case _:
        print("Invalid Input")

#===============================Problem 20=========================================
num1=int(input("Enter The First Number:-"))
num2=int(input("Enter The Second Number:-"))
operation=int(input("1.Addition(+)\n2.Subtraction\n3.Multiplication\n4.Division\nEnter The Operator Serial Number:- "))
match operation:
    case 1:
        print(num1+num2)
    case 2:
        print(num1-num2)
    case 3:
        print(num1*num2)
    case 4:
        print(num1/num2)
    case _:
        print("Invalid Input")

#===============================Problem 21=========================================
choice = int(input("Enter choice: "))

temperature = float(input("1.Celcius to Fahrenheit\n2.Fahrenheit to Celsius\nEnter temperature: "))

match choice:
    case 1:
        fahrenheit = (temperature * 9 / 5) + 32
        print("Temperature =", fahrenheit, "F")

    case 2:
        celsius = (temperature - 32) * 5 / 9
        print("Temperature =", celsius, "C")

    case _:
        print("Invalid choice")


#===============================Problem 22=========================================
choice = int(input("Enter choice: "))
value = float(input("Enter value: "))

match choice:
    case 1:
        meters = value * 1000
        print(meters, "meters")

    case 2:
        kilometers = value / 1000
        print(kilometers, "kilometers")

    case 3:
        grams = value * 1000
        print(grams, "grams")

    case 4:
        kilograms = value / 1000
        print(kilograms, "kilograms")

    case _:
        print("Invalid choice")

#===============================Problem 23=========================================
# ATM Withdrawal

account = int(input("Enter account type: "))
amount = float(input("Enter amount: "))

match account:
    case 1:
        if amount > 0:
            print("Savings Account")
            print("Withdrawal Request Accepted")
        else:
            print("Invalid Amount")

    case 2:
        if amount > 0:
            print("Current Account")
            print("Withdrawal Request Accepted")
        else:
            print("Invalid Amount")

    case _:
        print("Invalid Account Type")

#===============================Problem 24=========================================
choice = int(input("Enter choice: "))
match choice:
    case 1:
        age = int(input("Enter age: "))

        if age >= 18:
            print("You can start the exam")
        else:
            print("You cannot start the exam")

    case 2:
        print("View Result Selected")

    case 3:
        print("Exit Selected")

    case _:
        print("Invalid choice")

#===============================Problem 25=========================================
match int(input("Select ticket type (1-Regular, 2-Premium, 3-VIP): ")):
    case 1:
        ticket = "Regular Ticket"
    case 2:
        ticket = "Premium Ticket"
    case 3:
        ticket = "VIP Ticket"
    case _:
        ticket = "Invalid Ticket"

age = int(input("Enter age: "))

if age < 5:
    print("Free Entry")
else:
    print(ticket)


#===============================Problem 26=========================================
choice = int(input("Enter device (1-Light, 2-Fan, 3-AC, 4-TV): "))

match choice:
    case 1:
        print("Light Controller Opened")
    case 2:
        print("Fan Controller Opened")
    case 3:
        print("AC Controller Opened")
    case 4:
        print("TV Controller Opened")
    case _:
        print("Invalid Device")

#===============================Problem 27=========================================
choice = int(input("Enter department: "))

match choice:
    case 1:
        print("General Medicine Selected")
    case 2:
        print("Cardiology Selected")
    case 3:
        print("Orthopedics Selected")
    case 4:
        print("Pediatrics Selected")
    case 5:
        print("Emergency Selected")
    case _:
        print("Invalid Department")

#===============================Problem 28=========================================
choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Booking Ticket")
    case 2:
        print("Cancelling Ticket")
    case 3:
        print("Checking PNR")
    case 4:
        print("Showing Train Schedule")
    case 5:
        print("Exiting Railway System")
    case _:
        print("Invalid Choice")

#===============================Problem 29=========================================
choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Searching Book")
    case 2:
        print("Issuing Book")
    case 3:
        print("Returning Book")
    case 4:
        print("Viewing Issued Books")
    case 5:
        print("Exiting Library System")
    case _:
        print("Invalid Choice")

#===============================Problem 30=========================================
status = input("Enter status: ").lower()

match status:
    case "placed":
        print("Your order has been placed")
    case "confirmed":
        print("Your order is confirmed")
    case "preparing":
        print("Your order is being prepared")
    case "out_for_delivery":
        print("Your order is on the way")
    case "delivered":
        print("Your order has been delivered")
    case "cancelled":
        print("Your order has been cancelled")
    case _:
        print("Invalid Order Status")

#===============================Problem 31=========================================
bank = int(input("1. Personal Banking\n2. Business Banking\nEnter banking type: "))

match bank:
    case 1:
        option = int(input("1. Balance\n2. Transfer\n3. Loan\nEnter option: "))

        match option:
            case 1:
                print("Personal Balance Selected")
            case 2:
                print("Personal Transfer Selected")
            case 3:
                print("Personal Loan Selected")
            case _:
                print("Invalid Option")

    case 2:
        option = int(input("1. Balance\n2. Payroll\n3. Business Loan\nEnter option: "))

        match option:
            case 1:
                print("Business Balance Selected")
            case 2:
                print("Payroll Selected")
            case 3:
                print("Business Loan Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Banking Type")

#===============================Problem 32=========================================
role = int(input("1. Student\n2. Teacher\n3. Parent\nEnter role: "))

match role:
    case 1:
        option = int(input("1. Marks\n2. Attendance\n3. Homework\nEnter option: "))

        match option:
            case 1:
                print("Opening Student Marks")
            case 2:
                print("Opening Student Attendance")
            case 3:
                print("Opening Student Homework")
            case _:
                print("Invalid Option")

    case 2:
        option = int(input("1. Enter Marks\n2. Attendance\n3. Assign Homework\nEnter option: "))

        match option:
            case 1:
                print("Entering Marks")
            case 2:
                print("Managing Attendance")
            case 3:
                print("Assigning Homework")
            case _:
                print("Invalid Option")

    case 3:
        option = int(input("1. Child Marks\n2. Child Attendance\n3. Contact Teacher\nEnter option: "))

        match option:
            case 1:
                print("Opening Child Marks")
            case 2:
                print("Opening Child Attendance")
            case 3:
                print("Contacting Teacher")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Role")

#===============================Problem 33=========================================
transport = int(input("1. Flight\n2. Train\n3. Bus\nEnter transport: "))

match transport:
    case 1:
        option = int(input("1. Economy\n2. Business\nEnter option: "))

        match option:
            case 1:
                print("Flight Economy Selected")
            case 2:
                print("Flight Business Selected")
            case _:
                print("Invalid Option")

    case 2:
        option = int(input("1. Sleeper\n2. AC\nEnter option: "))

        match option:
            case 1:
                print("Train Sleeper Selected")
            case 2:
                print("Train AC Selected")
            case _:
                print("Invalid Option")

    case 3:
        option = int(input("1. Ordinary\n2. Volvo\nEnter option: "))

        match option:
            case 1:
                print("Bus Ordinary Selected")
            case 2:
                print("Bus Volvo Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Transport")

#===============================Problem 34=========================================
choice = int(input("1. Start Game\n2. Load Game\n3. Settings\n4. Exit\nEnter choice: "))

match choice:
    case 1:
        print("Starting Game")
    case 2:
        print("Loading Game")
    case 3:
        setting = int(input("1. Sound\n2. Graphics\n3. Controls\nEnter setting: "))

        match setting:
            case 1:
                print("Opening Sound Settings")
            case 2:
                print("Opening Graphics Settings")
            case 3:
                print("Opening Control Settings")
            case _:
                print("Invalid Setting")

    case 4:
        print("Exiting Game")
    case _:
        print("Invalid Choice")


#===============================Problem 35=========================================
category = int(input("1. Starters\n2. Main Course\n3. Desserts\n4. Drinks\nEnter category: "))

match category:
    case 1:
        item = int(input("1. Soup\n2. Spring Roll\n3. Garlic Bread\nEnter item: "))

        match item:
            case 1:
                print("Soup Ordered")
            case 2:
                print("Spring Roll Ordered")
            case 3:
                print("Garlic Bread Ordered")
            case _:
                print("Invalid Item")

    case 2:
        item = int(input("1. Pizza\n2. Pasta\n3. Biryani\nEnter item: "))

        match item:
            case 1:
                print("Pizza Ordered")
            case 2:
                print("Pasta Ordered")
            case 3:
                print("Biryani Ordered")
            case _:
                print("Invalid Item")

    case 3:
        item = int(input("1. Ice Cream\n2. Cake\n3. Gulab Jamun\nEnter item: "))

        match item:
            case 1:
                print("Ice Cream Ordered")
            case 2:
                print("Cake Ordered")
            case 3:
                print("Gulab Jamun Ordered")
            case _:
                print("Invalid Item")

    case 4:
        item = int(input("1. Coffee\n2. Tea\n3. Juice\nEnter item: "))

        match item:
            case 1:
                print("Coffee Ordered")
            case 2:
                print("Tea Ordered")
            case 3:
                print("Juice Ordered")
            case _:
                print("Invalid Item")

    case _:
        print("Invalid Category")

#===============================Problem 36=========================================
payment = int(input("1. UPI\n2. Card\n3. Wallet\nEnter payment type: "))

match payment:
    case 1:
        option = int(input("1. Scan QR\n2. Enter UPI ID\nEnter option: "))

        match option:
            case 1:
                print("Opening QR Scanner")
            case 2:
                print("Enter UPI ID")
            case _:
                print("Invalid Option")

    case 2:
        option = int(input("1. Credit Card\n2. Debit Card\nEnter option: "))

        match option:
            case 1:
                print("Credit Card Selected")
            case 2:
                print("Debit Card Selected")
            case _:
                print("Invalid Option")

    case 3:
        option = int(input("1. Add Money\n2. Pay Using Wallet\nEnter option: "))

        match option:
            case 1:
                print("Adding Money to Wallet")
            case 2:
                print("Paying Using Wallet")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Payment Type")

#===============================Problem 37=========================================
subject = int(input("1. Programming\n2. Mathematics\n3. Communication\nEnter subject: "))

match subject:
    case 1:
        option = int(input("1. Python\n2. Java\n3. C++\nEnter course: "))

        match option:
            case 1:
                print("Python Course Selected")
            case 2:
                print("Java Course Selected")
            case 3:
                print("C++ Course Selected")
            case _:
                print("Invalid Course")

    case 2:
        option = int(input("1. Algebra\n2. Calculus\n3. Statistics\nEnter course: "))

        match option:
            case 1:
                print("Algebra Selected")
            case 2:
                print("Calculus Selected")
            case 3:
                print("Statistics Selected")
            case _:
                print("Invalid Course")

    case 3:
        option = int(input("1. English\n2. Presentation\n3. Interview Skills\nEnter course: "))

        match option:
            case 1:
                print("English Selected")
            case 2:
                print("Presentation Selected")
            case 3:
                print("Interview Skills Selected")
            case _:
                print("Invalid Course")

    case _:
        print("Invalid Subject")

#===============================Problem 38=========================================
choice = int(input("1. Engine\n2. Lights\n3. Music\n4. Navigation\nEnter choice: "))

match choice:
    case 1:
        option = int(input("1. Start\n2. Stop\nEnter option: "))

        match option:
            case 1:
                print("Engine Started")
            case 2:
                print("Engine Stopped")
            case _:
                print("Invalid Option")

    case 2:
        option = int(input("1. Headlights\n2. Indicators\n3. Hazard Lights\nEnter option: "))

        match option:
            case 1:
                print("Headlights Selected")
            case 2:
                print("Indicators Selected")
            case 3:
                print("Hazard Lights Selected")
            case _:
                print("Invalid Option")

    case 3:
        option = int(input("1. Play\n2. Pause\n3. Next\n4. Previous\nEnter option: "))

        match option:
            case 1:
                print("Playing Music")
            case 2:
                print("Music Paused")
            case 3:
                print("Playing Next Song")
            case 4:
                print("Playing Previous Song")
            case _:
                print("Invalid Option")

    case 4:
        option = int(input("1. Start Navigation\n2. Stop Navigation\nEnter option: "))

        match option:
            case 1:
                print("Navigation Started")
            case 2:
                print("Navigation Stopped")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Choice")

#===============================Problem 39=========================================
role = int(input("1. Employee\n2. Manager\nEnter role: "))

match role:
    case 1:
        option = int(input("1. View Profile\n2. Apply Leave\n3. View Salary\nEnter option: "))

        match option:
            case 1:
                print("Opening Employee Profile")
            case 2:
                days = int(input("Enter leave days: "))

                if days > 0:
                    print("Leave Request Submitted")
                else:
                    print("Invalid Leave Days")

            case 3:
                print("Viewing Salary")
            case _:
                print("Invalid Option")

    case 2:
        option = int(input("1. View Team\n2. Approve Leave\n3. View Reports\nEnter option: "))

        match option:
            case 1:
                print("Viewing Team")
            case 2:
                print("Approving Leave")
            case 3:
                print("Viewing Reports")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Role")

#===============================Problem 40=========================================
role = int(input("1. Student\n2. Teacher\n3. Administration\nEnter role: "))

match role:
    case 1:
        option = int(input("1. Profile\n2. Marks\n3. Attendance\n4. Courses\nEnter option: "))

        match option:
            case 1:
                print("Opening Student Profile")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("Opening Student Attendance")
            case 4:
                print("Opening Student Courses")
            case _:
                print("Invalid Option")

    case 2:
        option = int(input("1. Students\n2. Enter Marks\n3. Attendance\n4. Courses\nEnter option: "))

        match option:
            case 1:
                print("Opening Students")
            case 2:
                print("Opening Enter Marks")
            case 3:
                print("Opening Teacher Attendance")
            case 4:
                print("Opening Teacher Courses")
            case _:
                print("Invalid Option")

    case 3:
        option = int(input("1. Fees\n2. Admissions\n3. Notices\n4. Departments\nEnter option: "))

        match option:
            case 1:
                print("Opening Fees")
            case 2:
                print("Opening Admissions")
            case 3:
                print("Opening Notices")
            case 4:
                print("Opening Departments")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Role")

