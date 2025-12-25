#Decaler the array named products to store info and use them to further operations
products = []
#Using a while loop to show the menu untile the user chooses one of the options
def menu():
   while True:
      print("\n********* Shopping Store System *********")
      print("\n1.Select Products")
      print("2.Display All Products")
      print("3.Total Store Revenue")
      print("4.Report Sales By Category")
      print("5.Exorbitant Products")
      print("6.Best-Selling Products")
      print("7.Exit The Program")
      print("\n")
      try:
         choice = int(input("Select One of The Options Above Please: "))
      except ValueError:
         print("Enter Digits Only")
         continue
      if choice == 1:
         select()
      elif choice == 2:
         display()
      elif choice == 3:
         totalRevenue()
      elif choice == 4:
         soldByCategory()
      elif choice == 5:
         exorbitant()
      elif choice == 6:
         bestSelling()
      elif choice == 7:
         print("Exiting the program...")
         exit()
      else:
         print("Please Choose One Of The Options Above")
#Input info such as product name, price, quantity and so on 
def select(): 
   try:
      store_id = int(input("Enter Store ID: "))
   except ValueError:
      print("Enter Digits Only")
      return
   product = input("Enter the product name here: ")
   try:
      product_barcode = int(input(f"Enter the barcode for {product}: "))
      price = float(input(f"Enter the price of {product} $: "))
      quantity = int(input(f"Enter the quantity of {product} : "))
   except ValueError:
      print("Enter Digits Only")
      return
   info = [store_id, product, product_barcode, price, quantity]
   products.append(info)
#Display all products along side their barcodes
def display():
   for p in products:
      print(f"Product Barcode: {p[2]} - Product Name:{p[1].title()} - Price: ${p[3]:,} - Quantity: {p[4]:,} ")
#To show units of products using the category that is product barcode
def soldByCategory():
   try:
      user_barcode = int(input(f"Enter the productID: "))
   except ValueError: 
      print("Enter Digits Only")
      return
   found = False
   total_price = 0
   for p in products:
      if user_barcode == p[2]:
         found = True
         total_price = p[3] * p[4]
         print(f"{p[4]:,} of {p[1]} sold")
         print(f"Total revenue of {p[1]} is ${total_price:,} ")
   if not found:
      print(f"The Barcode {user_barcode} was not found")
      return
#Take total revenue of the store using store ID
def totalRevenue():
   try:
      user_store_id = int(input("Enter the store ID to see the total revenue: "))
   except ValueError:
      print("Enter Digits Only")
      return
   total = 0
   found = False
   for p in products:
      if user_store_id == p[0]:
         found = True
         total = total + p[3]*p[4]
   print(f"Total revenue of the store with ID:{user_store_id} is ${total:,}")
   return
   if not found:
      print(f"The store ID {user_store_id} Not Found")
      return
#Display pricy products
def exorbitant():
   found = False
   for p in products:
      if p[3] > 1000:
         found = True
         print(f"{p[1].title()} is pricy, which is ${p[3]:,}")
#Display the best-selling product
def bestSelling():
    if not products:
        print("No products available")
        return
    best_product = products[0]
    for p in products:
        if p[4] > best_product[4]:
            best_product = p
    print(f"The best-selling product is {best_product[1].title()} with {best_product[4]:,} units sold")    
menu()
