# syntax
# Declaring a function
# def function_name():
    # codes
    # codes
# Calling a function
# function_name()

# Functions without Parameters

def generate_full_name():
    first_name = 'Arshi'
    last_name = 'Khan'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name()

def add_two_numbers():
    num_one = 3
    num_two = 5
    total = num_one + num_two
    print(total)
add_two_numbers()

# Function Returning a Value - Part 1

def generate_full_name():
    first_name = 'Arshi'
    last_name = 'Khan'
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())

def add_two_numbers ():
    num_one = 3
    num_two = 5
    total = num_one + num_two
    return total

print(add_two_numbers())

# Function with Parameters
# Single Parameter: 

def greeting (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greeting('Arshi'))

def add_ten(num):
    ten = 10
    return num + 10
print(add_ten(80))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area
print('Area of circle: ', area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total += i
    return total
print(sum_of_numbers(10))
print(sum_of_numbers(100))

# Two Parameter:

def generate_full_name(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name:', generate_full_name('Arshi', 'Khan'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age:', calculate_age(2026, 2006))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity) + 'N'
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))

# Passing Arguments with Key and Value

def print_fullname(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
print_fullname(first_name = 'Arshi', last_name = 'Khan')

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num2 = 3, num1 = 8))

# Returning a number:
def add_two_numbers (num1, num2):
    total = num1 + num2
    return total

print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age

print('Age:',calculate_age(2026, 2005))

# Returning a boolean: Example:

def is_even (n):
    if n % 2 == 0:
        return True
    return False
print(is_even(10))
print(is_even(87))

# Returning a list: Example:
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))

# Function with Default Parameters

def greetings (name = 'Peter'):
    message = name + ', welcome to Python For Everyone!'
    return message
print(greetings())
print(greetings('Arshi'))

def generate_full_name (first_name = 'Arshi', last_name = 'Khan'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())
print(generate_full_name('David', 'Smith'))

def calculate_age (birth_year, current_year = 2026):
    age = current_year - birth_year
    return age
print('Age:', calculate_age(2006))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity) + 'N'
    return weight
print('Weight of an object in Newtons:', weight_of_object(100))
print('Weight of an object in Newtons:', weight_of_object(100, 1.61))

# Arbitrary(unspecified) Number of Arguments

def sum_all_nums (*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sum_all_nums(2, 3, 5))

# Default and Arbitrary Number of Parameters in Functions
def generate_groups (team, *args):
    print(team)
    for i in args:
        print(i)
generate_groups('Team-1', 'Arshi','Brook', 'David', 'Eyob')

# Dictionary unpacking
def greet(name, location):
    print("Hi there", name, "how is the weather in", location)

my_dict = {'name': 'Alice', 'location': 'New York'}
greet(**my_dict)

# Arbitrary Number of Named Arguments
def arbitrary_named_args(**args):
    print("I received an arbitratry number of arguments, totaling", len(args))
    print("They are provided as a dictionary in my function:", type(args))
    print("Let's print them:")
    for k, v in args.items():
        print("* key:", k, "value:", v)

arbitrary_named_args(Name = 'Arshi', Age = 20, City = 'Jaipur')

# Function as a Parameter of Another Function
def square_number (n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3))

def cube (n):
    return n ** 3
def double(n):
    return n * 2
print(do_something(cube, 3))
print(do_something(double, 3))








