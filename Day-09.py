# Day 9 - 30DaysOfPython Challenge

# a = 0
# if a > 0:
#     print("A is a positive number.")
# elif a < 0:
#     print("A is a negative number.")
# else:
#     print("A is zero.")

# # shorthand
# a = 3
# print("A is positive.") if a > 0 else print("A is negative")

# # nested condition
# a = 446
# if a > 0:
#     if a % 2 == 0:
#         print("A is positive and even integer.")
#     else:
#         print("A is a positive number.")
# elif a == 0:
#     print("A is zero.")
# else:
#     print("A is negative.")

# # if condition with logical operators
# a = 2
# if a > 0 and a % 2 == 0:
#     print("A is positive and even integer.")
# elif a > 0 and a % 2 != 0:
#     print("A is positive integer.")
# else:
#     print("A is negative.")

# user = 'james'
# access_level = 3
# if user == 'admin' or access_level >= 4:
#     print("Access Granted!")
# else:
#     print("Access denied!")

# # Exercise Level - 1
# # 1
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are older enough to drive.")
# else:
#     print("You need",18 - age,"more years to drive.")

# # 2
# my_age = 15
# print("My age is 15.")
# your_age = int(input("Enter your age: "))
# if my_age > your_age:
#     print("You are", my_age - your_age,"years younger than me.")
# elif my_age < your_age:
#     print("You are", your_age - my_age, "years older than me.")
# else:
#     print("We are the same age!")

# # 3
# num_1 = int(input("Enter first number: "))
# num_2 = int(input("Enter second number: "))
# if num_1 > num_2:
#     print(num_1,"is greater than", num_2)
# elif num_1 < num_2:
#     print(num_1, "is smaller than", num_2)
# else:
#     print(num_1, "and", num_2,"are equal")

# # Exercises: Level 2
# # 1
# marks = int(input("Enter your marks: "))
# if marks >= 90 and marks <= 100:
#     print("A Grade!")
# elif marks >= 80 and marks <= 89:
#     print("B Grade!")
# elif marks >= 70 and marks <= 79:
#     print("C Grade!")
# elif marks >= 60 and marks <= 69:
#     print("D Grade!")
# else:
#     print("Fail!")

# # 2
# month = input("Enter the month: ")
# if month == 'December' or month == 'January' or month == 'February':
#     print("The season is Winter.")
# elif month == 'march' or month == 'april' or month == 'may':
#     print("The season is Summer.")
# elif month == 'June' or month == 'July' or month == 'August':
#     print("The season is Spring.")
# else:
#     print("The season is Autumn.")

# # 3

# fruit_list = ['Banana','mango','orange','apple']
# fruit = input("Enter 2 fruits name separated by space: ")
# fruits = fruit.split()
# if fruit in fruit_list:
#     print("That fruit already exists in the list.")
# else:
#     fruit_list.extends(fruits)
#     print("The modified list is: ", fruit_list)

# # Exercises: Level 3
# # 1
# #  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# #  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
# #  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
# #  * If the person is married and if he lives in Finland, print the information in the following format:

# person = {
#     'first_name': 'Arshi',
#     'last_name': 'Khan',
#     'age': 20,
#     'country': 'Finland',
#     'is_married': True,
#     'skills': ['React', 'MongoDB', 'Node', 'Javascript'],
#     'address':{
#         'street': 'Space street',
#         'zipcode': '302026'
#     }
# }
# if 'skills' in person:
#     skills = person['skills']
#     middle = len(skills) // 2
#     print("Middle Value: ", skills[middle])
#     if 'Python' in skills:
#         print("Python is a skill")
#     else:
#         print("Python is not a skill")
# else:
#     print("Skills is not in person dictionary....")

# skills = person['skills']
# if 'skills' in person:
#     if 'Javascript' in skills and 'React' in skills:
#         print("He is a front-end developer.")
#     elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
#         print("He is a back-end developer.")
#     elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
#         print("He is a full-stack developer.")
#     else:
#         print("Unknown Title")
# else:
#     print("Skills not in person dictionary")

# if person['is_married'] == True and person['country'] == 'Finland':
#     print(person['first_name'],person['last_name'],"lives in Finland. He is married.")

# Triangle Validity
# side_1 = int(input("Enter side 1: "))
# side_2 = int(input("Enter side 2: "))
# side_3 = int(input("Enter side 3: "))

# if side_1 + side_2 > side_3 and side_2 + side_3 > side_1 and side_1 + side_3 > side_2:
#     print("This is a Triangle")
#     if side_1 == side_2 and side_2 == side_3 and side_1 == side_3:
#         print("Equilateral Triangle")
#     elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3:
#         print("Isosceles")
#     else:
#         print("Scalene")
# else:
#     print("It's not a Triangle")

# Simple Login System
# correct_username = 'admin'
# correct_password = 1234
# username = input("Enter username: ")
# password = int(input("Enter password: "))
# if username == correct_username and password == correct_password:
#     print("Login Successful")
# elif username == correct_username and password != correct_password:
#     print("Incorrect Password")
# else:
#     print("User not found")

# Electricity Bill Calculator ⚡
# unit = int(input("Enter unit: "))
# if unit > 0 and unit <= 100:
#     total_unit = unit * 5
#     print("Total Unit when ₹5/unit: ", total_unit)
# elif unit >= 101 and unit <= 200:
#     total_unit = unit * 7
#     print("Total unit when ₹7/unit: ", total_unit)
# elif unit >= 201 and unit <= 300:
#     total_unit = unit * 10
#     print("Total unit when ₹10/unit: ", total_unit)
# else:
#     total_unit = unit * 15
#     print("Total unit when ₹15/unit: ", total_unit)

hours = int(input("Enter hours per day: "))
total_hours_per_week = hours * 7
print("I work",total_hours_per_week,"per week.")

# ATM Withdrawal 💳
balance = float(input("Enter balance: "))
amount = int(input("Enter withdrawal amount: "))
if amount > 0 and amount <= balance:
    if amount % 100 == 0:
        remain = balance - amount
        print("Withdrawal successful\nRemaining Amount: ", remain,"\nThank You")
    else:
        remain = balance - amount
        print("Can't withdrawal",remain, "this amount.")
else:
    print("Your amount is invalid, ensure your amount must not exceed balance.")

# Password Strength Checker 🔐
# password = input("Enter password: ")
# if password == '123456' or password == 'password':
#     print("Too Common")
# elif len(password) > 6 and len(password) < 9:
#     print("Medium Password")
# elif len(password) < 6:
#     print("Weak Password")
# else:
#     print("Strong")

# # Movie Ticket Pricing 🎬
# age = int(input("Enter your age: "))
# day_of_week = input("Enter day of the week: ")
# if age < 5:
#     print("Free")
# elif age >= 5 and age <= 12:
#     if day_of_week == 'Wednesday' or 'wednesday':
#         original = 100
#         discount = 50
#         final = original - discount
#         print("original = ₹100\ndiscount = ₹50\nfinal = ",final)
#     else:
#         print("original = 100")
# elif age >= 13 and age <= 59:
#     if day_of_week == 'Wednesday' or 'wednesday':
#         original = 200
#         discount = 50
#         final = original - discount
#         print("original = 100\ndiscount = 50\nfinal = ",final)
#     else:
#         print("original = 200")
# else:
#     print("Original = 120")

# Shopping Discount 🛒
# shopping = int(input("Enter your total shopping amount: "))
# if shopping >= 0 and shopping <= 999:
#     print("No Discount!")
# elif shopping >= 1000 and shopping <= 4999:
#     discount = 0.10
#     final = shopping * discount
#     final_amount = shopping - final 
#     print("Original Amount = ",shopping,"\nDiscount = 10% \nFinal Amount = ",final_amount)
# elif shopping >= 5000 and shopping <= 9999:
#     discount = 0.20
#     final = shopping * discount
#     final_amount = shopping - final 
#     print("Original Amount = ", shopping, "\nDiscount = 20%\nFinal = ", final_amount)
# else:
#     discount = 0.30
#     final = shopping * discount
#     final_amount = shopping - final 
#     print("Original Amount = ",shopping, "\nDiscount = 30%\nFinal Amount = ", final_amount)


# num1 = int(input("First number: "))
# op = input("Operator (+, -, *, /, %): ")
# num2 = int(input("Second number: "))

# match op:
#     case '+':
#         print("Result: ",num1 + num2)
#     case '-':
#         print("Result: ",num1 - num2)
#     case '*':
#         print("Result: ",num1 * num2)
#     case '/':
#         if num2 == 0: 
#             print("Division by zero\nInvalid operator")
#         else:
#             print("Result: ",num1 / num2)
#     case '%':
#         print("Result: ",num1 % num2)
#     case _:
#         print("Invalid Operator!")

# Simple Calculator
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = int(input("Enter 1. for '+'\n2. for '-'\n3. for '*'\n4. for '/'\n5. for '%'\n6. for '//'\n"))

match op:
    case 1:
        print(num1,"+",num2,"=",num1+num2,"\n")
    case 2:
        print(num1,"-",num2,"=",num1-num2,"\n")
    case 3:
        print(num1,"*",num2,"=",num1*num2,"\n")
    case 4:
        if num2 == 0:
            print("Error: Division by zero\n")
        else:
            print(num1,"/",num2,"=",num1 / num2,"\n")
    case 5:
        print(num1,"%",num2,"=",num1 %num2,"\n")
    case 6:
        print(num1,"//",num2,"=",num1 // num2,"\n")
    case _:
        print("Invalid Operator !")

# Menu Driven Program
task = int(input("Enter a task (1 for Calculator\n2 for Triangle Checker\n3 for Electricity Bill Checker)"))

match task:
    case 1:
    # Simple Calculator
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        op = int(input("Enter 1. for '+'\n2. for '-'\n3. for '*'\n4. for '/'\n5. for '%'\n6. for '//'\n"))

        match op:
            case 1:
                print(num1,"+",num2,"=",num1+num2,"\n")
            case 2:
                print(num1,"-",num2,"=",num1-num2,"\n")
            case 3:
                print(num1,"*",num2,"=",num1*num2,"\n")
            case 4:
                if num2 == 0:
                    print("Error: Division by zero\n")
                else:
                    print(num1,"/",num2,"=",num1 / num2,"\n")
            case 5:
                print(num1,"%",num2,"=",num1 %num2,"\n")
            case 6:
                print(num1,"//",num2,"=",num1 // num2,"\n")
            case _:
                print("Invalid Operator !")
    case 2:
    # Triangle Validity
        side_1 = int(input("Enter side 1: "))
        side_2 = int(input("Enter side 2: "))
        side_3 = int(input("Enter side 3: "))

        if side_1 + side_2 > side_3 and side_2 + side_3 > side_1 and side_1 + side_3 > side_2:
            print("This is a Triangle")
            if side_1 == side_2 and side_2 == side_3 and side_1 == side_3:
                print("Equilateral Triangle")
            elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3:
                print("Isosceles")
            else:
                print("Scalene")
        else:
            print("It's not a Triangle")
    case 3:
        # Electricity Bill Calculator ⚡
        unit = int(input("Enter unit: "))
        if unit > 0 and unit <= 100:
            total_unit = unit * 5
            print("Total Unit when ₹5/unit: ", total_unit)
        elif unit >= 101 and unit <= 200:
            total_unit = unit * 7
            print("Total unit when ₹7/unit: ", total_unit)
        elif unit >= 201 and unit <= 300:
            total_unit = unit * 10
            print("Total unit when ₹10/unit: ", total_unit)
        else:
            total_unit = unit * 15
            print("Total unit when ₹15/unit: ", total_unit)