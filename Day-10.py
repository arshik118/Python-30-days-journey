# count = 0
# while count < 5:
#     print(count)
#     count = count + 1
# else:
#     print(count)

# Break and Continue - Part 1
# Break: We use break when we like to get out of or stop the loop.
# count = 0
# while count < 5:
#     print(count)
#     count = count + 1
#     if count == 3:
#         break

# Continue: With the continue statement we can skip the current iteration, and continue with the next.
# count = 0
# while count < 5:
#     if count == 3:
#         count += 1
#         continue
#     print(count)
#     count = count + 1

# For Loop for list
# for i in range(50,0,-2):
#     print(i)
    
# for i in range(1,21):
#     if i % 2 == 0:
#         continue
#     print(i)


# i = 1
# while i <= 10:
#     if i % 2 != 0:
#         i += 1
#         continue

#     print(i)
#     i += 1

# for i in range(1,51):
#     if i % 2 != 0:
#         print(i)
#     i += 1

# num = int(input("Enter number to print the table: "))
# for i in range(1,11):
#     print(num, "*", i, "=", num*i)

# n = int(input("Enter a number: "))
# i = 1
# sum = 0
# while i <= n:
#     sum += i
#     i += 1

# print(sum)

# num = int(input("Enter a number for factorial: "))
# fact = 1
# i = 1
# while i <= num:
#     fact *= i
#     i += 1

# print(fact)

# num = int(input("Enter number for count: "))
# i = num
# count = 0
# while i != 0:
#     count += 1
#     i = i // 10
# print(count)

# num = int(input("Enter a number for reverse: "))
# i = num
# rev = 0
# while i != 0:
#     digit = i % 10
#     rev = rev * 10 + digit
#     i = i // 10
# print("Reverse =", rev)

# if rev == num:
#     print("The number is a palindrome number")
# else:
#     print("The number is not a palindrome number")

# n = int(input("Enter a number: "))
# i = n
# num = 0
# while i != 0:
#     digit =  i % 10
#     num += digit**3
#     i = i // 10
# print(num)

# if num == n:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")

# num = int(input("Enter a number: "))

# if num < 2:
#     print("Not a prime number")
# else:
#     i = 2
#     while i < num:
#         if num % i == 0:
#             print(num, "is not a prime number")
#             break
#         i += 1

#     else:
#         print(num," is a Prime Number")


# Print all prime numbers between 1 and 100
# i = 2

# while i <= 100:
#     j = 2
#     is_prime = True

#     while j < i:
#         if i % j == 0:
#             is_prime = False
#             break
#         j += 1

#     if is_prime:
#         print(i)

#     i += 1

# Find the sum of all even digits in a number.
# num = int(input("Enter number: "))
# i = num
# total = 0

# while i != 0:
#     digit = i % 10

#     if digit % 2 == 0:
#         total += digit

#     i //= 10

# print(total)

# i = 2

# while i <= 100:
#     j = 2
#     is_prime = True

#     while j < i:

#         if i % j == 0:
#             is_prime = False
#             break
#         j += 1

#     if is_prime:
#         print(i)

#     i += 1

# count = 0

# while count <= 5:
#     if count == 3:
#         count += 1
#         continue
#     print(count)
#     count = count + 1

# num = int(input("Enter a number: "))
# smallest = 10

# while num > 0:
#     digit = num % 10

#     if digit < smallest:
#         smallest = digit

#     num //= 10

# print("The Smallest digit is: ", smallest)

# num = int(input("Enter a number: "))
# largest = 0

# while num > 0:
#     digit = num % 10

#     if digit > largest:
#         largest = digit

#     num //= 10

# print("The Largest digit is: ", largest)

# n = int(input("Enter a number: "))
# i = 1

# while i <= 10:
#     print(n, "*", i, "=", n*i)
#     i += 1

# a = 1
# i = 0

# while i <= 100:
#     if a % 2 != 0:
#         i += a
#         print(i)
# a += 1

# i = 1

# while i <= 10:
#     print (i*i)
#     i += 1

lst = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
heroes = ["ironman", "thor", "Superman", "Batman"]
i = 0

while i < len(heroes):
    print(heroes[i])
    i += 1


tuple = (1, 4, 9, 16, 25, 36, 64, 81, 100)
i = 0
x= 36

while i < len(tuple):
    if tuple[i] == x:
        print("Found at index:", i)
        break
    else:
        print("Finding")
    i += 1

i = 1

while i <= 10:
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1

# For Loop :-

tup = (1, 2, 3, 4, 2, 8, 9)

for num in tup:
    print(num)

str = "apanacollege"

for char in str:
    if char == 'o':
        print("O found")
        break
    print(char)
else: # here, else can be used if we want to print something after the end of the loop

    print("END")

list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0

for i in list:
    print(idx,i)
    idx += 1

tup = (1, 4, 16, 25, 36, 49, 64, 81, 100)
x = 50
for i in tup:
    if i == x:
        print(x,"Found!")
        break
else:
    print("Not Found!")

# Sum of first n natural numbers :-

i = 1
sum = 0

while i <= 5:
    sum += i
    i += 1
print("sum", sum)

# using for loop..

n = 7
sum = 0
for i in range(1, n+1):
    sum += i
print("Total sum =", sum)

# Factorial of n numbers:-

n = 8
fact = 1

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# Using For Loop on string

language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

# Using For loop on tuple

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# for loop with dictionary 
person = {
    'first_name': 'Arshi',
    'last_name': 'Khan',
    'country': 'India',
    'is_married': False,
    'skills': ['javascript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street':'Space Street',
        'zipcode': '02210'
    }
}

for key in person:
    print(key)

for key, value in person.items():
    print(key,value)

# Using For Loop in set

it_companies = {'facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

for company in it_companies:
    print(company)

# Break and Continue - Part 2
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end")
print('outside the loop')

# Range function:- means give me numbers one by one from here to there.
# range (start?, stop, step?)

# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(num, "*", i, "=", num*i)

for i in range(1,6):
    print(i)

for i in range(2, 11, 2):
    print(i)

# negative steps - going backwards
for i in range(10, 0, -1):
    print(i)

# Prime Numbers from 1 to 100
# Nested for loop
for i in range(2, 101):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i)

person = {
    'first_name': 'Arshi',
    'last_name': 'Khan',
    'country': 'India',
    'is_married': False,
    'skills': ['javascript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street':'Space Street',
        'zipcode': '02210'
    }
}

for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

# If we want to execute some message when the loop ends, we use else.
for number in range(11):
    print(number)
else:
    print("The loop stops at", number)

# Pass 
for number in range(6):
    pass
