str1 = ['Thirty', 'Days', 'Of', 'Python']
print(' '.join(str1))

str2 = ['Coding', 'For', 'All']
print(' '.join(str2))

company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[ : 6])
sub_string = 'Coding'
print(company.index(sub_string))
print(company.find('Coding'))
print(company.replace('Coding', 'Python'))
str3 = 'Python for Everyone'
print(str3.replace(str3, 'Python for All'))
print(company.split())
str4 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(str4.split(', '))
print(company[0])
print(company.index('All'))
print(company.find('All'))
print(company[10])
phrase = 'Python For Everyone'
res = "".join(word[0].upper() for word in phrase.split())
print(res)

sentence = 'Coding For All'
abbreviation = "".join(word[0].upper() for word in sentence.split())
print(abbreviation)

print(company.index('C'))
print(company.index('F'))

str5 = 'Coding For All People'
print(str5.rfind('I'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
print(sentence.rindex('because'))
print(sentence[31 : 54])
print(sentence.find('because'))
print(company.startswith('Coding'))
print(company.endswith('coding'))
str6 = '  Coding For All  '
print(str6.strip())
str7 = '30DaysOfPython'
str8 = 'thirty_days_of_python'
print(str7.isidentifier())
print(str8.isidentifier())
str9 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(str9))
print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\tCountry\tCity\nArshi\t250\tIndia\tJaipur')
radius = 10
area = 3.14 * radius ** 2
formatted_string = 'The area of a circle with radius {} is {} meters square.'.format(radius, area)
print(formatted_string)

a = 8
b = 6

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
str1 = ['Thirty', 'Days','Of','Python.']
res = ' '.join(str1)
print(res)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
str2 = ['Coding','For', 'All.']
res = ' '.join(str2)
print(res)

# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All."

# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().
print(len(company))

# Change all the characters to uppercase letters using upper() method.
print(company.upper())

# Change all the characters to lowercase letters using lower() method.
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string.
print(company[0:6])

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
sub_string = 'Coding'
print(company.index(sub_string))
# or other method can be
print(company.find('Coding'))

# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

# Change "Python for Everyone" to "Python for All" using the replace method or other methods.
str3 = 'Python for Everyone'
print(str3.replace('Python for Everyone', 'Python for All'))

# Split the string 'Coding For All' using space as the separator (split()) .
str4 = 'Coding for All'
print(str4.split(' '))

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = 'Facebook , Google, Microsoft, Apple, IBM, Oracle, Amazon'
res = companies.split(", ")
print(res)

# What is the character at index 0 in the string Coding For All.
print(str4[0])

# What is the last index of the string Coding For All.
print(str4.index('All'))
print(str4.find('All'))

# What character is at index 10 in "Coding For All" string.
print(str4[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
phrase = "Python For Everyone"
acronym = "".join(word[0].upper() for word in phrase.split())

print(acronym)

# Create an acronym or an abbreviation for the name 'Coding For All'.
phrase = "Coding for All"
acronym = "".join(word[0].upper() for word in phrase.split())
print(acronym)

# Use index to determine the position of the first occurrence of C in Coding For All.
print(phrase.index('C'))

# Use index to determine the position of the first occurrence of F in Coding For All.
phrase = 'Coding For All'
print(phrase.index('F'))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
phrase = 'Coding For All People'
print(phrase.rfind('I'))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index('because'))
print(sentence.find('because'))

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rfind('because'))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:55])

# Does 'Coding For All' start with a substring Coding?
print(phrase.startswith('Coding'))

# Does 'Coding For All' end with a substring coding?
print(phrase.endswith('Coding'))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
phrase = '     Coding For All       '
print(phrase.strip('    '))

# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python

phrase = '30DaysOfPython'
print(phrase.isidentifier())
phrase = 'thirty_days_of_python'
print(phrase.isidentifier())

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(('# '.join(python_libraries)))

# Use the new line escape sequence to separate the following sentences.
print("I am enjoying this challenge.\nI just wonder what is next.")

# Use a tab escape sequence to write the following lines.
print("Name\t\tAge\tCountry\t\tCity\nAsabeneh\t250\tFinland\t\tHelsinki")

# Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print("The area of circle with radius {} is {} meters square.".format(radius, area))

# Make the following using string formatting methods:
a = 8
b = 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
