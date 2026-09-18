# Day 6:
# Tuples
# Creating a Tuple
# Tuple length
# Accessing Tuple Items
# Slicing tuples
# Changing Tuples to Lists
# Checking an Item in a Tuple
# Joining Tuples
# Deleting Tuples
# 💻 Exercises: Day 6
# Exercises: Level 1
# Exercises: Level 2

# Creating a Tuple (Empty Tuple)
empty_tuple = ()
empty_tuple = tuple()
# Tuple with initial values
tpl = ('itme1', 'item2', 'item3', 'item4')
print(tpl)

fruits = ('banana', 'orange', 'mango', 'lemon')

# Tuple length (len)
tpl = ('item1', 'item2', 'item3')
len(tpl)

# Accessing Tuple Items
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(first_fruit)
print(second_fruit)
print(last_fruit)

# Negative Indexing
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-len(fruits)]
print(first_fruit)
second_fruit = fruits[-3]
print(second_fruit)
last_fruit = fruits[-1]
print(last_fruit)

# Slicing tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:]
print(all_fruits)
orange_lemon = fruits[1: : 2]
print(orange_lemon)
banana_mango = fruits[::2]
print(banana_mango)
orange_lemon = fruits[-3::2]
print(orange_lemon)
orange_to_the_rest = fruits[-3:]
print(orange_to_the_rest)

# Changing Tuples to lists
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
print(fruits)
fruits = tuple(fruits)
print(fruits)

# Checking items in tuple
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits)

# Joining tuple
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# Deleting Tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits

empty_tuple = tuple()
empty_tuple = ()
print(empty_tuple)

sisters = ('Gunnu', 'Kashu', 'Nini', 'Chichi', 'Doraemon')
brothers = ('Bander', 'Nikku', 'Chinu', 'Faizal', 'Ibrahim', 'Ali')
siblings = sisters + brothers
print(siblings)
print(len(siblings))
sibling = list(siblings)
family_members = ['Moh.Naeem', 'Shamshad Khan']
sibling.extend(family_members)
print(sibling)
a,b,c,d,e,f,g,h,i,j,k,l,m = sibling
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
print(m)
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
animal_product = ('Meat', 'Eggs', 'Poultry', 'Milk', 'Cheese', 'butter', 'yogurt')
food_stuff_tp = fruits + vegetables + animal_product
print(food_stuff_tp)
food_stuff_it = list(food_stuff_tp)
middle = len(food_stuff_tp) // 2
print(food_stuff_tp[middle])
print(food_stuff_it[:4])
print(food_stuff_it[13:])
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)

movies = []
movie1 = (input("Enter First movies: "))
movie2 = (input("Enter Second movies: "))
movie3 = (input("Enter Third movies: "))
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies)

lst = [1,2,3]
lst1 = lst.copy()
lst1.reverse()

if lst1 == lst:
    print["The list have palindrome elements."]
else:
    print("The list does not have palindrome elements.")

grade = ('C', 'D', 'A', 'A', 'B', 'B', 'A') 
count = grade.count('B')
print("The number of students who get 'B' grade are:", count)
grade.sort()
print(grade)

