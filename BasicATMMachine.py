#Simple ATM Simulation
#Setting balance initially to $500
balance = 500

#Using while loop to create menu based program
while True:
    #Printing Operations
    print("--------------------Welcome to the ATM Simulation--------------------")
    print("ATM Operations:\n1. Check Balance\n2. Withdraw Money\n3. Deposit Money \n4. Exit\n")

    #Asking user which operation to do
    choice = input("Enter which operation to choose(1/2/3/4): ")

    #Using if-elif-else to check which option user entered
    if choice == "1":
        #Printing Balance
        print(f"Your balance is: ${balance}")

    elif choice == "2":
        #Asking user amount to be withdrawn
        withdraw = int(input("Enter Amount to Withdraw: "))

        #If sufficient balance, amount is withdrawn
        if withdraw <= balance:
            print(f"${withdraw} have been withdrawn")
            balance -= withdraw
            print(f"Your new balance is ${balance}")
        #If insufficient balance
        else:
            print("Insufficient funds. Please enter a lesser amount")
            continue

    elif choice == "3":
        #Asking user amount to be deposited and adding it to the balance
        deposit = int(input("Enter Amount to be deposited: "))
        balance += deposit
        print(f"${deposit} deposited")
        print(f"Your new balance is ${balance}")

    elif choice == "4":
        #Exiting Program
        print("Thank you for using the ATM, Goodbye!")
        break

    else:
        print("Invalid Option")
        print()
        continue
