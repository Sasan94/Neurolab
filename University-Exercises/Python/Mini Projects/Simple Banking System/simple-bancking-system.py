# Ask how many accounts the user wants to create
accounts = int(input("How many accounts do you need: "))

#To take basic account info and save them  in thecustomers array
customers = []
for i in range(accounts):
  temp = []
  acc_name = input("Type the account holder's name: ")
  acc_id = int(input("Type the ID for the account: "))
  balance = int(input("Type the balance $: "))
  temp = [acc_id, acc_name, balance]
  customers.append(temp)
print(f"\n")

#Starting the main program loop
while True:
  print(f"\n\n===== Banking Operations Menu =====")
  print(f"\n1.Display all account holders' names and Balances")
  print(f"2.Deposite into an account")
  print(f"3.Withdra from an account")
  print(f"4.Exit the program")

  #The user chooses one the five menu options
  choice = input("\nPlease choose one of the five options above: ")
  print("\n")

  #Option 1: to show all accounts
  if choice == '1':
    for acc_id, acc_name, balance in customers:
      print(f"Account ID: {acc_id}, Name: {acc_name.title()}, Balance: ${balance:,}")
      print("\n")

  #Option 2: To deposit into an account
  elif choice == '2':
    acc_id = int(input("Type the account ID you want to deposit into: "))
    amount = int(input("Type the amount $: "))
    for c in customers:
      if c[0] == acc_id:
        c[2] = c[2] + amount
        print(f"\nUpdated account {acc_name.title()} balance is ${c[2]:,}")
        break
    else:
      print(f"\nThe account was not found")

  #Option 3: To withdraw from an account    
  elif choice == '3':
    acc_id = int(input("Type the account ID you want to withdraw from: "))
    amount = int(input("Type the amount $: "))
    for c in customers:
      if c[0] == acc_id:
        if c[2] <= amount:
          print(f"The account balance is insufficient to withdraw")
          break
        c[2] = c[2] - amount
        print(f"\nUpdated account {acc_name.title()} balance is ${c[2]:,}")
        break
    else:
      print(f"\nThe account was not found")

  #Option 4: Exit the program
  elif choice == '4':
    print("Exit the program")
    exit()

  #Invalid input
  else:
    print("Choose one of the five options please")
