# 🟢 Easy: Build the basic logic
# 1. Print even numbers from 1 to 50
# i = 1

# while i <= 50:
#     if i % 2 == 0:
#         print(i)
#         i += 1
#     i += 1

# 2. Print odd numbers from 1 to 50
# i = 1

# while i <= 50:
#     if i % 2 != 0:
#         print(i)
#         i += 1
#     i += 1

# 3. Print numbers from 1 to 100 divisible by both 3 and 5
# i = 1

# while i <= 100:
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)
#     i += 1

# 4. Count how many numbers from 1 to 100 are divisible by 7
# i = 1
# count = 0

# while i <= 100:
#     if i % 7 == 0:
#         count += 1
#     i += 1
# print(count)

# 5. Find the sum of all even numbers from 1 to n
# n = int(input("Enter a number: "))
# i = 0
# sum = 0

# while i <= n:
#     if i % 2 == 0:
#         sum += i
#         print(i,end="")
#         if i != n:
#             print(" +",end=" ")
#     i += 1
    
# print(" =",sum)


# 🟡 Medium: Number + loop + conditions
# 6. Count even and odd digits in a number

# n = int(input("Enter a number: "))
# i = n
# count = 0
# sum = 0
# have_odd = False
# have_even = False

# while i != 0:
    
#     digit = i % 10
#     if digit % 2 == 0:
#         have_even = True
#         count += 1
#     else:
#         have_odd = True
#         sum += 1

#     i //= 10

# if have_even == True:
#     print("Even digits = ", count)
# else:
#     print("The Number does not contain any even number.")

# if have_odd == True:
#     print("Odd digits = ", sum)
# else:
#     print("The Number does not contain any odd number.")

# 7. Find the sum of even digits and the sum of odd digits separately
# n = int(input("Enter a number: "))
# i = n
# sum = 0
# total = 0
# have_even = False
# have_odd = False

# while i != 0:

#     digit = i % 10 
#     if digit % 2 == 0:
#         have_even = True
#         sum += digit

#     else:
#         total += digit
#         have_odd = True

#     i //= 10

# if have_even == True:
#     print("Even digit sum =", sum)
# else:
#     print("The number does not contain any even number.")
# if have_odd == True:
#     print("Odd Digit sum =", total)
# else:
#     print("The number does not contain any odd number.")

# 8. Find the largest and smallest digit in a number
# n = int(input("Enter a number: "))
# largest = 0
# smallest = 10
# i = n

# while i != 0:
#     digit = i % 10
#     if digit > largest:
#         largest = digit
#     if digit < smallest:
#         smallest = digit
#     i //= 10
# print("Largest =",largest)
# print("Smalest =",smallest)

# 9. Count how many digits are greater than 5
# n = int(input("Enter some digits: "))
# i = n
# count = 0

# while i != 0:
#     digit = i % 10
#     if digit > 5:
#         count += 1
#     i //= 10

# print("Digits greater than 5 =", count)

# 10. Check whether a number contains the digit 7
# n = int(input("Enter a number: "))
# i = n
# key = 7

# while i != 0:
#     digit = i % 10
#     if digit == key:
#         print("7 found")
#         break
#     i //= 10
# else:
#     print("7 not Found")

# 11. Count how many times a specific digit appears
# num = int(input("Enter a number: "))
# i = num
# count = 0
# key = 2

# while i != 0:
#     digit = i % 10
#     if digit == key:
#         count += 1
#     i //= 10

# print(key,"appears",count,"times")

# 13. Find the second largest digit in a number
# number = int(input("Enter a number: "))
# largest = -1
# second_largest = -1
# i = number

# while i != 0:
#     digit = i % 10

#     if digit > largest:
#         second_largest = largest
#         largest = digit

#     elif digit > second_largest and digit != largest:
#         second_largest = digit

#     i //= 10

# print("Second Largest digit: ", second_largest)

# 14. Check whether a number is a palindrome
# num = int(input("Enter a number: "))
# i = num
# rev = 0

# while i != 0:

#     digit = i % 10
#     rev = rev * 10 + digit

#     i //= 10

# if rev == num:
#     print("Palindrome number")
# else:
#     print("Not a palindrome number")

# 15. Check whether a number is an Armstrong number
# num = int(input("Enter a number: "))
# i = num
# total = 0
# while i != 0:
#     digit = i % 10
#     total += digit**3

#     i //= 10

# if total == num:
#     print("Armstrong number")
# else:
#     print("Not an armstrong number")

# 🔴 Expert Challenge
# 16. Find the largest even digit and largest odd digit separately

# num = int(input("Enter a number: "))
# i = num
# largest_even = -1
# largest_odd = -1
# even = False
# odd = False

# while i != 0:
#     digit = i % 10

#     if digit % 2 == 0:
#         even = True
#         if digit > largest_even:
#             largest_even = digit
#     else:
#         odd = True
#         if digit > largest_odd:
#             largest_odd = digit

#     i //= 10

# if even:
#     print("The largest even digit =", largest_even)
# else:
#     print("No even digit in the number")
# if odd:
#     print("The largest odd digit =", largest_odd)
# else:
#     print("No odd digit in the number")

# 17. Reverse only the even digits of a number

# num = int(input("Enter a number: "))
# i = num
# even_digit = []
# rev = 0
# rev_even = False

# while i != 0:
#     digit = i % 10
    
#     if digit % 2 == 0:
#         even_digit.append(digit)
#         rev = rev * 10 + digit
#         rev_even = True

#     i //= 10
# even_digit.reverse()

# if rev_even:
#     print("Even Digit: ", *even_digit)
#     print("Reverse of even digits in a number =", rev)
# else:
#     print("No even digits in the number.")

# 18. Print all numbers from 1 to 100 that are divisible by 3 but not divisible by 5

i = 1

while i <= 100:
    if i % 3 == 0 and i % 5 != 0:
        print(i)
    i += 1

# 20. Number Analyzer 🔥

num = int(input("Enter a number: "))
i = num
total = 0
sum = 0
sum_of_even = 0
sum_of_odd = 0
largest = 0
smallest = 10
odd_count = 0
even_count = 0

while i != 0:
    digit = i % 10

    total += 1

    sum += digit

    if digit % 2 == 0:
        sum_of_even += digit
    else:
        sum_of_odd += digit

    if digit > largest:
        largest = digit
    if digit < smallest:
        smallest = digit

    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    i //= 10
print("Total digits: ", total)
print("Sum of digits: ", sum)
print("Sum of even digits: ", sum_of_even)
print("Sum of odd digits: ", sum_of_odd)
print("Largest digit: ", largest)
print("Smallest digit: ", smallest)
print("Even digit count: ", even_count)
print("Odd digit count: ", odd_count)


