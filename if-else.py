num = int(input("Enter a number: "))

if(num % 2 == 0):
    print("Even number")
else:
    print("Odd number")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if(num1 > num2 and num1 > num3):
    print(num1, " is the greatest number!")
elif(num2 > num1 and num2 > num3):
    print(num2, " is greatest number!")
elif(num3 > num1 and num3 > num2):
    print(num3 ," is the greatest number!")
else:
    print("The number you entered is a negative number!!")

num = 68

if (num % 7 == 0):
    print(num, "is multiple of 7.")
else:
    print(num, "Not multiple of 7.")