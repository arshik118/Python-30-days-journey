# Introduction
# Day 1 - 30DaysOfPython Challenge
print("Hello, World!")

print(2 + 3)    # addition(+)
print(3 - 1)    # subtraction(-)
print(2 * 3)    # Multiplication(*)
print(3 / 2)    # Divison(/)
print(3 ** 2)   # exponential(**)
print(3 % 2)    # modulus(%)
print(3 // 2)   # Floor Divison Operator(//)

# Checking Data Types
print(type(10))     # Int
print(type(3.14))   # Float
print(type(1 + 3j)) # Complex Number
print(type('Arshi'))    # String
print(type([1, 2, 3]))  # List
print(type({'name':'Arshi'}))   # Dictionary
print(type({9.8, 3.14, 2.7}))   # Set
print(type((9.8, 3.14, 2.7)))   # Tuple

# Day 1 - Exercise
# Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.

number = 10
dec = 3.14
com = 1 - 3J
string = 'Arshi'
li = ['Arshi', 'Khan', 'India', 'age']
se = {2.4, 4.54, 6.45}
tu = (2, 3, 64,3.64)
dic = {'country':'India',
       'age':'20'}
boolean = False

print(number)
print(dec)
print(com)
print(string)
print(li)
print(se)
print(tu)
print(dic)
print(boolean)

# Exercise - Find an Euclidean distance between (2, 3) and (10, 8)
# Euclidean Distance is the shortest straight-line distance between two points.

import math

x1, y1 = 2, 3
x2, y2 = 10, 8

distance = math.sqrt((x2 - x1)** 2 + (y2 - y1)** 2)
print("Euclidean Distance is: ", distance)
# END

