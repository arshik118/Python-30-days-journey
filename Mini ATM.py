# Mini ATM 🏦

balance = 0
username = input("Enter username: ")
password = int(input("Enter password: "))
correct_password = 1234


if username == 'admin' and password == correct_password:
    print("Login Successfully")
    print("\n~~~Simple ATM Program~~~\n")
    print("1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit\n")
    category = int(input("Choose Your Category: "))
elif username == 'admin' and password != correct_password:
    print("Incorrect Password")
    exit()
else:
    print("User Not Found!")
    exit()


match category:

    case 1:
        print("Your Current Balance: ₹",balance,"\n")
        balance = int(input("Initialize your balance: ₹"))

    case 2:
        amount = int(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print("Deposited Successfully!\n")
            print("Your Current Balance is: ₹", balance,"\n")
        else:
            print("Invalid Deposit Amount!\n")

    case 3:
        amount = int(input("Enter amount to withdrawal: "))
        if amount > balance:
            print("Insufficient Balance!\n")
        elif amount <= 0:
            print("Invalid Withdrawal Amount!\n")
        else:
            balance -= amount
            print("Withdrawal Successfully\n")
            print("Your Current Balance after withdrawal is: ₹", balance,"\n")

    case 4:
        print("Thank You for using our ATM !\n")

    case _:
        print("Invalid choice ! Please Try again!\n")


            
