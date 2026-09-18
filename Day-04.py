# Day 4
# Strings
    # Creating a String
    # String Concatenation
    # Escape Sequences in Strings
    # String formatting
        # Old Style String Formatting (% Operator)
        # New Style String Formatting (str.format)
        # String Interpolation / f-Strings (Python 3.6+)
    # Python Strings as Sequences of Characters
        # Unpacking Characters
        # Accessing Characters in Strings by Index
        # Slicing Python Strings
        # Reversing a String
        # Skipping Characters While Slicing
# String Methods

# Creating a String

letter = 'P'
print(letter)
print(len(letter))
greeting = 'Hello, World!'
print(greeting)
print(len(greeting))
sentence = 'I hope you are enjoying 30 days of Python Challenge'
print(sentence)
print(len(sentence))

# Multiline String
multiline_string = '''I am a teacher and enjoy teaching. 
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

# String Concatenation

first_name = 'Arshi'
last_name = 'Khan'
space = ' '
full_name = first_name + space + last_name
print(full_name)
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))

# Escape Sequence

print('I hope everyone is enjoying the Python Challenge.\n Are you ?')
print('Days\tTopics\tExercises')
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash symbol(\\)')
print('In every porgramming language it starts with \"Hello, World!\"')

# String formatting
# Old style string formatting(% Operator)
# Strings only

first_name = 'Arshi'
last_name = 'Khan'
age = 20
language = 'Python'
formatted_string = 'I am %s %s. I teach %s'%(first_name,last_name,language)
print(formatted_string)

# if there is no string formatting
print("My name is " + first_name + " and I am " + str(age)+ " years old.")

# Strings and numbers

radius = 10
pi = 3.14
area = pi * radius ** 2
formatted_string = 'The area of circle with a radius %d is %.3f.'%(radius, area)
print(formatted_string)

python_libraries = ['Django', 'Flask', 'Numpy', 'Matplotlib', 'Pandas']
formatted_string = 'The following are python libraries:%s'%(python_libraries)
print(formatted_string)

# New style string formatting (str.format)

first_name = 'Arshi'
last_name = 'Khan'
language = 'Python'
formatted_string = "I am {} {}. I teach {}." .format(first_name,last_name,language)
print(formatted_string)

a = 4
b = 3
print('{} + {} = {}' .format(a, b, a + b))
print('{} - {} = {}' .format(a, b, a - b))
print('{} * {} = {}' .format(a, b, a * b))
print('{} / {} = {:.2f}' .format(a, b, a / b))
print('{} ** {} = {}' .format(a, b, a ** b))
print('{} % {} = {}' .format(a, b, a % b))

r = 10
pi = 3.14
area = pi * r ** 2
formatted_string = 'The area of circle with radius {} is {:.2f}' .format(r, area)
print(formatted_string)

# String Interpolation / f-Strings 

a = 4
b = 3
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} ** {b} = {a ** b}')
print(f'{a} % {b} = {a % b}')

first_name = 'Arshi'
last_name = 'Khan'
language = 'Python'
formatted_string = f'I am {first_name} {last_name}. I teach {language}'
print('String Interpolation:', formatted_string)

# Unpacking Strings
language = 'Python'
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Accessing Characters in strings by Index

language = 'Python'
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
third_letter = language[2]
print(third_letter)
forth_letter = language[3]
print(forth_letter)
fifth_letter = language[4]
print(fifth_letter)
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)

# If we want to start from right end we can use negative indexing. -1 is the last index

language = 'Python'
last_letter = language[-1]
print(last_letter)
last_second = language[-2]
print(last_second)
last_third = language[-3]
print(last_third)
last_forth = language[-4]
print(last_forth)
last_index = -len(language)
first_letter = language[last_index]
print("first_letter", first_letter)

# Slicing Python Strings

language = 'Python'
first_three = language[0 : 3]
print(first_three)
last_three = language[3 : 6]
print(last_three)
# Another way
last_three = language[-5 : -2]
print(last_three)
last_three = language[3 : ]
print(last_three)

# Reversing a string

greeting = 'Arshi'
print("Reverse a sting\n")
print(greeting[::-1]) # string [start:stop:step]

# Skipping Characters While Slicing

language = 'Python'
pto = language[0:6:2]
print("pto: ",pto)
# Using negative
print(language[::-2])
print(language[-5::2])
print(language[1::2])
print(language[-2:-5:-1])

# String Methods
# Capitalize()
challenge = 'thirty days of python'
print(challenge.capitalize())

# Count(substring, start=..,end=..)
challenge = 'thirty days of python'
print(challenge.count('y'))
print(challenge.count('y',7, 14))
print(challenge.count('th'))
print(challenge.count('d'))

# endswith()
challenge = 'thirty dayd of python'
print(challenge.endswith('on'))
print(challenge.endswith('tion'))

# expandtabs()
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(10))

# find()
challenge = 'thirty days of python'
print(challenge.find('y'))
print(challenge.find('th'))

# rfind()

challenge = 'thirty days of python'
print(challenge.rfind('y'))
print(challenge.rfind('th'))

# format()
first_name = 'Arshi'
last_name = 'Khan'
age = 20
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name,job, age, country)
print(sentence)

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of circle with radius {} is {}.'.format(str(radius), str(area))
print(result)

# index()
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))
sub_string = 'da'
print(challenge.index(sub_string))
print(challenge.index(sub_string))

# rindex()
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))
print(challenge.rindex('on', 8))

# isalnum() - Like in passwords (alphanumeric is the combination of numbers and letters)
challenge = 'ThirtyDaysPython'
print(challenge.isalnum())

challenge = '30DaysPython'
print(challenge.isalnum())

challenge = 'thirty days of python'
print(challenge.isalnum())

challenge = 'thirty days of python 2019'
print(challenge.isalnum())

# isalpha()
challenge = 'thirty days of python'
print(challenge.isalpha())
challenge = 'ThirtyDaysPython'
print(challenge.isalpha())
num = '123'
print('num', num.isalpha())

# isdecimal()
challenge = 'thirty days of python'
print(challenge.isdecimal())
challenge = '123'
print(challenge.isdecimal())
challenge = '\u00B2'
print(challenge.isdigit())
challenge = '12.3'
print(challenge.isdecimal())

# isdigit()
challenge = ''
print(challenge.isdigit())
challenge = '30'
print(challenge.isdigit())
challenge = '\u00B2'
print(challenge.isdigit())

# isnumeric() (just same as isdigit() accepts more values)
num = '10'
print(num.isnumeric())
num = '\u00BD'
print(num.isnumeric())
num = '10.5'
print(num.isnumeric())

# isidentifier()
challenge = '30DaysOfPython'
print(challenge.isidentifier())
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())

# islower()
challenge = 'thirty days of python'
print(challenge.islower())
challenge = 'Thirty days of python'
print(challenge.islower())

# isupper()
challenge = 'thirty days of python'
print(challenge.isupper())
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())

# join()
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result)

web_tech = ['HTML', 'CSS', 'Javascript', 'React']
result = '# '.join(web_tech)
print(result)

# strip()
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth'))

# replace()
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))

# split()
challenge = 'thirty days of python'
print(challenge.split())
challenge = 'thirty, days, of, python'
print(challenge.split('. '))

# title()
challenge = 'thirty days of python'
print(challenge.title())

# swapcase()
challenge = 'thirty days of python'
print(challenge.swapcase())
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())

# startwith()
challenge = 'thirty days of python'
print(challenge.startswith('thirty'))

challenge = '30 days of python'
print(challenge.startswith('of'))


