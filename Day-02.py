# Day 2 - 30DaysOfPython Challenge
# Variables in Python

first_name = 'Arshi'
last_name = 'Khan'
country = 'India'
city = 'Jaipur'
age = 20
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'first_name':'Arshi',
    'last_name':'Khan',
    'country':'India',
    'city':'Jaipur'
}

print('First name:', first_name)
print('First name length:',len(first_name))
print('last_name', last_name)
print('Last name Length:',len(last_name))
print('Country:', country)
print('Country Length:',len(country))
print('City:',city)
print('City Length:',len(city))
print('Age:',age)
print('Is married :',is_married)
print('Skills:',skills)
print("Personnal Information:",person_info)

print('Hello',',', 'World', '!')

# Declaring Multiple Variables in a line
first_name, last_name, country, age, is_married = 'Arshi', 'Khan', 'India', 20, False
print(first_name, last_name, country, age, is_married)

# Getting user input using input() built-in-function. Let us assign the data we get from the user into first_name and age variable
first_name = input("What is your name: ")
age = input("How old are you? ")

print(first_name)
print(age)

# Different python data types
# Let's declare variables with various data types

first_name = 'Arshi'
last_name = 'Khan'
country = 'India'
city = 'Helsinki'
age = 250

# Printing out types
print(type('Arshi'))
print(type(first_name))
print(type(10))
print(type(3.14))
print(type(1 + 1j))
print(type(True))
print(type([1, 2, 3, 4]))
print(type({'name': 'Arshi'}))
print(type((1,2)))
print(type(zip([1,2],[3,4])))

# Casting
# int to float
num_int = 10
print('num_int', num_int)
num_float = float(num_int)
print('num_float', num_float)


# Float to int
gravity = 9.81
print(int(gravity))

# int to str
num_int = 10
print(num_int)
num_str = str (num_int)
print(num_str)

# str to int or float
num_str = '10.6'
num_float = float(num_str)
num_int = int(num_str)
print('num_int', num_int)
print('num_float', num_float)

# str to list
first_name = 'Arshi'
print(first_name)
first_name_to_list = list(first_name)
print(first_name_to_list)

# Exercise - Level 1
# Day 2: 30 Days of python programming
first_name = 'Arshi'
last_name = 'Khan'
full_name = 'Arshi Khan'
country = 'India'
city = 'Jaipur'
age = 20
year = 2026
is_married = True
is_true = True
is_light_on = True

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(len(first_name))

diff = len(first_name) - len(last_name)
print(diff)

# Execise - Day 2
num_one = 5
num_two = 4
total = num_one + num_two
print("Total : ", total)

diff = num_one - num_two
print("Difference : ", diff)

product = num_one * num_two
print("Product : ", product)

division = num_one / num_two
print("Division : ", division)

rem = num_one % num_two
print("Remainder : ", rem)

exp = num_one ** num_two
print ("Exponential : ", exp)

floor_division = num_one // num_two              # floor-division mean go toward negative infinity
print("Floor division : ", floor_division)

radius = 30
pi = 3.141592653589793
area_of_circle = pi * radius ** 2
print("Area of circle : ", area_of_circle)

circum_of_circle = 2 * pi * radius
print("Circumference of a circle is : ", circum_of_circle) 

radius = int(input("Enter a radius: "))
pi = 3.141592653589793
area = pi * radius ** 2
print('Area of Circle: ',area)

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))

print("Your name is: ", first_name + " " + last_name)
print("Your country: ", country)
print("Your age: ", age)

# END



