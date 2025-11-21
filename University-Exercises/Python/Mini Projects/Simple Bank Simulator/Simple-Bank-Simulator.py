accounts = int(input("How many accounts do you need: "))
customers = []

for i in range(accounts):
    acc_name = input("Type the account holder's name: ")
    acc_id = int(input("Type the ID for the account: "))
    balance = int(input("Type the balance $: "))
    customers.append([acc_id, acc_name, balance])

print("\n")

while True:
    print("\n\n===== Banking Operations Menu =====")
    print("1. Display all accounts")
    print("2. Deposit into an account")
    print("3. Withdraw from an account")
    print("4. Exit the program")

    choice = input("\nChoose one of the options: ")

    if choice == '1':
        for acc_id, acc_name, balance in customers:
            print(f"\nAccount ID: {acc_id}, Name: {acc_name.title()}, Balance: ${balance:,}")

    elif choice == '2':
        acc_id = int(input("Enter the account ID to deposit into: "))
        amount = int(input("Enter the deposit amount $: "))

        for c in customers:
            if c[0] == acc_id:
                c[2] += amount
                print(f"\nUpdated balance for {c[1].title()}: ${c[2]:,}")
                break
        else:
            print("The account was not found.")

    elif choice == '3':
        acc_id = int(input("Enter the account ID to withdraw from: "))
        amount = int(input("Enter the withdrawal amount $: "))

        for c in customers:
            if c[0] == acc_id:
                if c[2] < amount:
                    print("Insufficient funds.")
                else:
                    c[2] -= amount
                    print(f"\nUpdated balance for {c[1].title()}: ${c[2]:,}")
                break
        else:
            print("The account was not found.")

    elif choice == '4':
        print("Exiting...")
        exit()

    else:
        print("Invalid choice. Try again.")
