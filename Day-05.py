# Day 5
    # Lists
        # How to Create a List
        # Accessing List Items Using Positive Indexing
        # Accessing List Items Using Negative Indexing
        # Unpacking List Items
        # Slicing Items from a List
        # Modifying Lists
        # Checking Items in a List
        # Adding Items to a List
        # Inserting Items into a List
        # Removing Items from a List
        # Removing Items Using Pop
        # Removing Items Using Del
        # Clearing List Items
        # Copying a List
        # Joining Lists
        # Counting Items in a List
        # Finding Index of an Item
        # Reversing a List
        # Sorting List Items
# 💻 Exercises: Day 5
    # Exercises: Level 1
    # Exercises: Level 2

# List is a collection of different data types which is ordered and modifiable (mutable). 
# A list can be empty or it may have different data type items.
# How to create a List
# Using list built-in function

lst = list()

empty_list = list()
print(len(empty_list))

# Using square brackets []
lst = []
empty_list = []
print(len(empty_list))

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomtao', 'Potato', 'Cabbage', 'Onion', 'Carrot']
animal_products = ['milk', 'meat','butter', 'yogurt']
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB']
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and its length
print('Fruits:', fruits)
print('Number of fruits: ', len(fruits))
print('Vegetables: ', vegetables)
print('Number of vegetables: ', len(vegetables))
print('Animal products:', animal_products)
print('Number of animal products: ', len(animal_products))
print('Web technologies: ', web_techs)
print('Number of web technologies: ', len(web_techs))
print('Countries: ', countries)
print('Number of countries: ', len(countries))

lst = ['Arshi', 250, True, {'country':'Finland','city':'Helsinki'}]
print(lst)

# Accessing items using positive index

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)
third_fruit = fruits[2]
print(third_fruit)
last_index = len(fruits)-1
last_fruit = fruits[last_index]
print(last_fruit)

# Accessing items using negative index

fruits = ['banana', 'orange', 'mango', 'lemon']
first_index = -len(fruits)
first_fruit = fruits[first_index]
print(first_fruit)
second_fruit = fruits[-3]
print(second_fruit)
third_fruit = fruits[-2]
print(third_fruit)
last_fruit = fruits[-1]
print(last_fruit)

# Unpacking List Items

lst = ['item1', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)
print(second_item)
print(third_item)
print(rest)

# First Example

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)
print(second_fruit)
print(third_fruit)
print(rest)

# Second Example about unpacking list

first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)

# Third Example about unpacking list

countries = ['Germany', 'France', 'Belgium', 'Sweden', 'Denmark', 'Finland', 'Norway', 'Iceland', 'Estonia']
gr,Fr,bg,sw,*scandic,es = countries
print(gr)
print(Fr)
print(bg)
print(sw)
print(scandic)
print(es)

# Slicing Items from a List (Positive Indexing)

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruit = fruits[::-2]
all_fruits = fruits[0 : ]
orange_and_mango = fruits[1 : 3]
orange_mango_lemon = fruits[1 : ]
orange_lemon = fruits[1 : : 2]
print(all_fruit)
print(all_fruits)
print(orange_and_mango)
print(orange_mango_lemon)
print(orange_lemon)

# (Negative Index)

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4::]
print(all_fruits)
orange_mango = fruits[-3: ]
print(orange_mango)
orange_mango_lemon = fruits[-3: ]
reverse_fruits = fruits[::-1]
print(orange_mango_lemon)
print(reverse_fruits)

# Modifying list

print("\t~~~Modifying List~~~\t")
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)
fruits[1] = 'apple'
print(fruits)
last_index = len(fruits)-1
fruits[last_index] = 'lime'
print(fruits)

# Checking Items in a list

print("~~Checking Items in a list~~")
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)
does_exist = 'lime' in fruits
print(does_exist)

# Adding Items to a list

print("~~Adding Items to a list~~")
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)
fruits.append('lime')
print(fruits)

# Inserting an item into a list

print("~~Inserting an item into a list~~")
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple')
print(fruits)
fruits.insert(3, 'lime')
print(fruits)

# Removing Items from a list

print("~~Removing Items from a list~~")
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)
fruits.remove('lemon')
print(fruits)

# Removing Items Using Pop

print("~~Removing Items Using Pop~~")
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)
fruits.pop(0)
print(fruits)

# Removing Items Using Del

# print("~~Removing Items Using Del~~")
# fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
# del fruits[0]
# print(fruits)
# del fruits[1:3]
# print(fruits)
# del fruits
# print(fruits)

# Clearing List Items

# print("~~Clearing List Items~~")
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.clear()
# print(fruits)

# Copying a List

print("~~Copying a list~~")
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)

# Joining Lists (plus operator(+))

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = positive_numbers + zero + negative_numbers
print(integers)

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# (using extend() method)

num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers: ', num1)

negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integer: ', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables: ', fruits)

# Counting Items in a List

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('banana'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))

# Finding Index of an Item
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))

# Reversing a List

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits[::-1])

fruits.reverse()
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)

# Sorting List Items

print("~~Sorting List Items~~")
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()   # ascending
print(fruits)
fruits.sort(reverse = True) # descending
print(fruits)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)

# sorted()- built-in function
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))
# Reverse Order
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = sorted(fruits, reverse=True)
print(fruit)
print(fruits)

if __name__ == '__main__':
    n = int(input())
    my_tup = map(int, input().split())
    t = tuple(my_tup)
    print(hash(t))