# 🟢 LEVEL 1 — List Basics
# Problem 1 ⭐
numbers = [10, 20, 30, 40, 50]
for i in numbers:
    print(i)
    
for i in range(len(numbers)):
    print(numbers[i])

# Problem 2 ⭐
numbers = [5, 10, 34, 5, 76, 86]
num = []
for i in numbers:
    num.append(i * 2)

print(num)

# Problem 3 ⭐
numbers = [12, 5, 8, 21, 10, 7]
num =[]
for i in numbers:
    if i % 2 == 0:
        num.append(i)
print(num)

# Problem 4 ⭐
numbers = [12, 5, 8, 21, 10, 7]
num = []
for i in numbers:
    if i % 2 != 0:
        num.append(i)

print(num)

# LEVEL 2 — for + accumulator
# Problem 5 ⭐⭐

numbers = [5, 10, 15, 20]
num = []
sum = 0
for i in numbers:
    sum += i
    num.append(sum)

print(sum)

# Problem 6 ⭐⭐
numbers = [4, 7, 2, 9, 6, 3, 10]
num = []
sum = 0
for i in numbers:
    if i % 2 == 0:
        sum += i
        num.append(sum)

print(sum)

# LEVEL 3 — Counting
# Problem 7 ⭐⭐

numbers = [2, 7, 7, 0, 6, 6, 8]
count = 0
num = []

for i in numbers:
    if i % 2 == 0:
        count += 1

print(count)

# Problem 8 ⭐⭐
numbers = [94, 17, 56, 21, 10, 15, 12]
count = 0
for i in numbers:
    if i > 10:
        count += 1

print(count)

# LEVEL 4 — Finding
# Problem 9 ⭐⭐⭐

numbers = [-3, -56, -33, -45]
largest = -1
for i in numbers:
    if i > largest:
        largest = i

print("Largest number in the list is:", largest)

# Problem 10 ⭐⭐⭐

numbers = [112, 145, 123, 156]
smallest = 1000
for i in numbers:
    if i < smallest:
        smallest = i

print('Smallest number:',smallest)

# 🟡 LEVEL 5 — List Manipulation & Searching
# 🧩 Problem 11 ⭐⭐ — Search for an element
numbers = [10, 25, 7, 40, 15, 30]
n = int(input("Enter a number: "))
ele = n

for i in numbers:
    if i is ele:
        print("Found")
        break
else: 
    print("Not Found!")

# 🧩 Problem 12 ⭐⭐ — Count a particular number
numbers = [2, 5, 2, 2, 8, 22, 5, 2]
count = 0
target = 8

for i in numbers:
    if i == target:
        count += 1

print(count)

# 🧩 Problem 13 ⭐⭐ — Create a list of positive numbers
numbers = [-5, 10, -2, 7, 8, 15, 0]
positive_numbers = []
for i in numbers:
    if i > 0:
        num.append(i)

print(num)

# 🧩 Problem 14 ⭐⭐ — Replace negative numbers
numbers = [-5, 3, -8, -7, -2, 1]
new_list = []
for i in numbers:
    if i < 0 :
        i = 0
        new_list.append(i)
    else:
        new_list.append(i)

print(new_list)

# 🧩 Problem 15 ⭐⭐⭐ — Reverse a list into a NEW list
numbers = [10, 20, 30, 40, 50]
reversed_list = []
for i in range(-1,-len(numbers)- 1,-1):
    reversed_list.append(numbers[i])

print(reversed_list)

# 🧩 Problem 16 ⭐⭐⭐ — Find the position

numbers = [15, 8, 22, 9, 31]
ele = 22
for i in range(len(numbers)):
    if numbers[i] == ele:
        print('Index:',i)

# 🧩 Problem 17 ⭐⭐⭐ — Separate even and odd numbers
numbers = [1, 4, 7, 10, 13, 16, 19]
even = []
odd = []
for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

# n = int(input())
# lst = []
# for x in input().split():
#     lst.append(int(x))

# print(lst)

# # 🟢 Problem 2 ⭐
# n = int(input())
# for x in input().split():
#     print(int(x))

n = int(input())
for x in input().split():
    int(x)
    if int(x) % 2 == 0:
        print(int(x))
    





