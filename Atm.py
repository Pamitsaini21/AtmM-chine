import time

print("Please insert your CARD")
time.sleep(5)

password = 1234
balance = 5000

try:
    pin = int(input("Enter your ATM pin: "))
except ValueError:
    print("Invalid input. Please enter a numerical pin.")
    exit()

if pin == password:
    while True:
        print("""
        1 == Check Balance
        2 == Withdraw Balance
        3 == Deposit Balance
        4 == Exit
        """)

        try:
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Please enter a valid option")
            continue

        if option == 1:
            print(f"Your current balance is {balance}")
            print("==================================================")
        elif option == 2:
            try:
                withdraw_amount = int(input("Please enter withdraw amount: "))
            except ValueError:
                print("Invalid amount. Please enter a numerical value.")
                continue

            if withdraw_amount <= balance:
                balance -= withdraw_amount
                print(f"{withdraw_amount} is debited from your account")
            else:
                print("Insufficient balance")
                
            print("==================================================")
            print(f"Your current balance is {balance}")
            print("==================================================")
        elif option == 3:
            try:
                deposit_amount = int(input("Please enter deposit amount: "))
            except ValueError:
                print("Invalid amount. Please enter a numerical value.")
                continue

            balance += deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print("==================================================")
            print(f"Your current balance is {balance}")
            print("==================================================")
        elif option == 4:
            print("Thank you for using our service!")
            break
        else:
            print("Invalid option, please try again")
else:
    print("Wrong pin, please try again")
