#Declear a global variable to store and use the customers's information throughout the code
customers = []
#This function adds new customer to the system
def addAccount():
   first_name = input("Type the holder's account name: ")
   last_name = input(f"Type the last name for {first_name.title()}: ")
   try:
      cust_id = int(input(f"Create A Customer ID for {first_name.title()} {last_name.title()}: "))
   except ValueError:
      print("Enter digits only")
      return
   try:
      acc_id = int(input(f"Create An Account ID for the {first_name.title()} {last_name.title()}: "))
   except ValueError:
      print("Enter digits only")
      return
   try:
      balance = int(input(f"Enter the initial balance for {first_name.title()} {last_name.title()} $: "))
   except ValueError:
      print("Enter digits only")
      return
   info = [first_name, last_name, cust_id, acc_id, balance]
   customers.append(info)
#This function displays customers's information
def display():
   for c in customers:
      print(f"Info ==> CustomerID: {c[2]} - AccountID: {c[3]} - FullName: {c[0].title()} {c[1].title()} - Balance = ${c[4]:,}")
#This function helps to deposit into another account
def deposit():
   try:
      user_acc = int(input("Enter the AccountID into which you want to deposit: "))
      amount = int(input("Enter the amount $: "))
   except ValueError:
      print("Enter digits only")
      return
   found = False
   for c in customers:
      if user_acc == c[3]:
         found = True
         c[4] += amount
         print(f"\nAn amount Of ${amount:,} was deposited into the account with ID:{c[3]} Full Name: {c[0].title()} {c[1].title()} \nUpdated acoount balance is ${c[4]:,}")
   if not found:
      print(f"This account ID {user_acc} Not Found")
      return  
#This fuction helps to withdraw from accounts
def withdraw():
   try:
      user_acc = int(input("Enter the AccountID from which you want to withdraw: "))
      amount = int(input("Enter the amount $: "))
   except ValueError:
      print("Enter digits only")
      return
   found = False
   for c in customers:
      if user_acc == c[3]:
         found = True
         if amount < c[4]:
            c[4] -= amount
            print(f"${amount:,} was withdrawn from the accountID: {c[3]} FullName: {c[0].title()} {c[1].title()} \nUpdated balance is {c[4]:,}")
         else:
            print(f"The balance account is insufficient to withdraw")
   if not found:
      print(f"This AccountID: {user_acc} Was Not Found!")
      return
#This function displays a specific customer’s account ID based on their customer ID
def serachCustomerAccounts():
   try:
      user_id = int(input("Please Enter the customer ID to show its accounts: "))
   except ValueError:
      print("Enter Digits Only")
      return
   found = False
   total_acc = 0
   for c in customers:
      if user_id == c[2]:
         found = True
         total_acc += 1
         print(f"CustomerID: {c[2]} - Full Name: {c[0].title()} {c[1].title()} - AccountID: {c[3]}")
   if not found:
      print(f"CustomerID {user_id} Was Not Found!")
      return
   print(f"\nThe customer has {total_acc} accounts")
#This function displays the average balance of customers’ accounts based on their customer ID
def averageBalance():
    try:
        user_id = int(input("Enter the customer ID: "))
    except ValueError:
        print("Enter Digits Only")
        return 
    found = False
    total_balance = 0
    counter = 0
    for c in customers:
        if user_id == c[2]:
            found = True
            total_balance += c[4]
            counter += 1
            print(f"AccountID: {c[3]} Full Name: {c[0].title()} {c[1].title()} - Balance = ${c[4]:,}")
    if not found:
        print(f"The CustomerID {user_id} Was Not Found!")
        return
    ave = total_balance / counter
    print(f"\nThe Average Balance = ${ave:,}")
#This function displays the accounts ID that are above the average based on their customer ID
def displayAccountAboveAve():
   try:
      user_id = int(input("Enter the customer ID here: "))
   except ValueError:
      print("Enter Digits Oly")
      return
   found = False
   total_balance = 0
   counter = 0
   for c in customers:
      if user_id == c[2]:
         found = True
         total_balance += c[4]
         counter += 1
   if not found:
      print(f"The CustomerID: {user_id} Was Not Found!")
      return
   ave = total_balance / counter
   for c in customers:
      if user_id == c[2] and c[4] > ave:
         found = True
         print(f"The Balance Of AccountID: {c[3]} Is Above The Average, which is ${c[4]:,}")   
#Display how many accounts we have in the system
def totalAccountsID():
   total_account = 0
   for c in customers:
      c[3] = 1
      total_account += c[3]
   print(f"Total AccountID = {total_account}")
#Display how many customers we have in the system
def totalCustomers():
   total_customer = 0
   seen = []
   for c in customers:
      if c[2] not in seen:
         seen.append(c[2])
         total_customer += 1
   print(f"Total Number Of Customers = {total_customer:,}")
#This function displays the menu by which the user can choose one of its options to operate it  
def menu():
   while True:
      print("\n========== Banking Operation System ==========")
      print("\n1.Add New Accounts")
      print("2.Display All Accounts")
      print("3.Deposit Into Accounts")
      print("4.Withdraw From Accounts")
      print(f"5.Display The Customer's Accounts Using Their CustomerID")
      print(f"6.Display The Average Balance Of A Customer's Accounts")
      print("7.Display The Customer's Accounts With Balance Above The Average")
      print("8.Diplay Total Number Of AccountID")
      print("9.Display Total Number Of Customers")
      print("10.Exit The Program")
      try:
         choice = int(input(f"\nChoose one of the options above: "))
      except ValueError:
         print("Enter digits only")
         continue
      if choice == 1: 
         addAccount()
      elif choice == 2:
         display()
      elif choice == 3:
         deposit()
      elif choice == 4:
         withdraw()
      elif choice == 5:
         serachCustomerAccounts()
      elif choice == 6:
         averageBalance()
      elif choice == 7:
         displayAccountAboveAve()
      elif choice == 8:
         totalAccountsID()
      elif choice == 9:
         totalCustomers()
      elif choice == 10:
         print("Exiting The Program")
         exit()
      else:
         print("Plase Choose One Of The 5 Options Above")        
menu()
input("Press Enter To Exit In DOS Environment")
