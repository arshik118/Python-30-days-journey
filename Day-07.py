# Creating a Set
# To create an empty set, we use the set() function. Empty curly brackets {} will create a dictionary.

# Creating an empty set
st = set()
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits))

# Checking an Item

collection = {'world!' ,1, 2, 3, 4, 5, 'hello'}
print('world!' in collection)

# Adding Items to a Set
fruits.add('lime')
print(fruits)

# Removing Items from a Set
fruits.remove('lime')
print(fruits)
fruits.discard('apple')
print(fruits)
removed_item = fruits.pop()
print(removed_item)
print(fruits)

# Clearing Items in a Set
# fruits.clear()
# print(fruits)

# Deleting a Set
# del fruits

# Converting List to Set
fruit = list(fruits)
print(fruit)

# Joining Sets (union())
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables))

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2))
print(set1.intersection(set2))

# update()
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits)

# using | symbol
print(fruits | vegetables)

# Finding Intersection Items

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
number = whole_numbers.intersection(even_numbers)
print(number)

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
pyth = python.intersection(dragon)
print(pyth)

# Checking Subset and Super Set
setA = {1, 2, 3}
setB = {1,2}

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.issubset(even_numbers))
print(whole_numbers.issuperset(even_numbers))

print(python.issubset(dragon))
print(python.issuperset(dragon))

# Checking the Difference Between Two Sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.difference(even_numbers))
print(whole_numbers - even_numbers)
print(dragon.difference(python)) # Give me everything that is in the First set but not in the second set
print(python.difference(dragon))

# Finding Symmetric Difference Between Two Sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
print(python.symmetric_difference(dragon))

# Joining Sets

even_numbers = {0, 2, 4, 6, 8, 10}
odd_numbers = {1, 3, 5, 7, 9, 11}
print(even_numbers.isdisjoint(odd_numbers))

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
print(it_companies.add('Twitter'))
print(it_companies)
print(it_companies.update(['Accenture', 'Infosys', 'Cognizant', '(TCS)']))
print(it_companies.pop())
print(it_companies.remove('Microsoft'))
print(it_companies)
print(it_companies.discard('Facebook'))
print(it_companies)
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))
print(A.difference(B))
del A
del B
del it_companies
ages = [19, 23, 54, 53, 21, 34, 65]
age = list(ages)
print(age)
print(len(age)-len(ages))

st = set()
print(st)
