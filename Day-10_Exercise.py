# Exercise: Level 1
# 1.Iterate 0 to 10 using for loop, do the same using while loop.

# Using for loop
for i in range(11):
    print(i)

#  Using While loop
i = 0

while i <= 10:
    print(i)
    i += 1

# 2.Iterate 10 to 0 using for loop, do the same using while loop.

# Using for loop
for number in range(10, 0, -1):
    print(number)

# Using While Loop
i = 10

while i >= 0:
    print(i)
    i -= 1

# 3.Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######

for i in range(1,8):
    print("#"*i)

# 4.Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

for i in range(9):
    for j in range(9):
        print("#", end=" ")
    print()

# 5.Print the following pattern:
for i in range(11):
    print(i,"x",i,"=",i*i)

# 6.Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

lst = ['Python', 'Numpy', 'Pandas', 'Django','Flask']

for i in lst:
    print(i)

# 7.Use for loop to iterate from 0 to 100 and print only even numbers

for i in range(0,101,2):
    print(i,end=" ")
print()

# 8.Use for loop to iterate from 0 to 100 and print only odd numbers

for i in range(1,101,2):
    print(i,end=" ")
print()

# Exercise: Level 2
# 1.Use for loop to iterate from 0 to 100 and print the sum of all numbers.

sum = 0
for i in range(101):
    sum += i

print("The sum of all numbers is", sum,".")

# 2.Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_even = 0
for i in range(0,101,2):
    sum_even += i
print("The sum of all evens is",sum_even,end=" ")

sum_odd = 0

for i in range(1,101,2):
    sum_odd += i
print("And the sum of all odds is", sum_odd,".")

#Exercises:Level 3
# 1.Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

# from countries import countries

# for country in countries:
#     if "land" in country:
#         print(country)
    
# 2.This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit_list = ['banana', 'orange', 'mango', 'lemon']
i = len(fruit_list)-1

while i >= 0:
    print(fruit_list[i])
    i -= 1

fruit_list = ['banana', 'orange', 'mango', 'lemon']
for i in range(len(fruit_list)-1,-1,-1):
    print(fruit_list[i])

# 3.Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world

from countries_data import countries

all_languages = set()

for country in countries:
    for language in country['languages']:
        all_languages.add(language)

print(len(all_languages))

#2.
from countries_data import countries

language_count = {}

for country in countries:
    for language in country['languages']:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1

# Step 2: Convert dictionary into a sortable list
sorted_languages = sorted(
    language_count.items(),
    key=lambda item: item[1],
    reverse=True
)

# Step 3: Print first 10
for language, count in sorted_languages[:10]:
    print(language, count)