# Declare a global arry in order to be used throughout the program
products = []

# This function creates a menu by which the user can select options from it
def menu():
   while True:
      print(f"\n********* Store Shopping System *********")
      print(f"\n1.Enter Products")
      print(f"2.Total Revenue")
      print(f"3.Report Sales By Category")
      print(f"4.Display All Products")
      print(f"5.Best-Selling And Least-Selling Products")
      print(f"6.Pricy And Cheap Products")
      print(f"7.Exit The Program")
      print("\n")
      try:
         choice = int(input("Select One Of The Options Above: "))
      except ValueError:
         print("Enter Digits Only")
         continue
      if choice == 1:
         enter()
      elif choice == 2:
         revenue()
      elif choice == 3:
         saleByCategory()
      elif choice == 4:
         display()
      elif choice == 5:
         bestSellingProducts()
      elif choice == 6:
         pricyCheapProducts()
      elif choice == 7:
         print("Exiting The Program...")
         exit()
      else:
         print("Choose One Of The Options Above Please")

# Enter information about products such as product name, price, quantity and so on
def enter():
   try:
      store_id = int(input("Enter the store ID: "))
   except ValueError:
      print("Enter Digits Only")
      return
   product_name = input("Enter the name of the product here: ")
   try:
      barcode = int(input(f"Enter the barcode of the {product_name}: "))
      price = float(input(f"Enter the price of the {product_name}: $"))
      quantity = int(input(f"Enter the quantity of the {product_name}: "))
   except ValueError:
      print("Enter Digits Only")
      return
   info = [store_id, product_name, barcode, price, quantity]
   products.append(info) 

# Display all products along side their barcodes
def display():
   for p in products:
      print(f"Store ID: {p[0]} - Product Name: {p[1].title()} - Barcode: {p[2]} - Price ${p[3]:,} - Quantity: {p[4]:,}")   

# Display the total revenue
def revenue():
   if not products:
      print("There are no reports to show")
      return
   try:
      user_code = int(input("Enter the store ID: "))
   except ValueError:
      print("Enter Digits Only")
      return
   found = False
   total_revenue = 0
   for p in products:
      if user_code == p[0]:
         found = True
         total_revenue = total_revenue + p[3]*p[4]   
   if found:
      print(f"Total revenue for store with ID {user_code} is ${total_revenue:,}")
   else:
      print(f"The storeID: {user_code} not found")

# To show units of products using the category, which is product barcode
def saleByCategory():
   if not products:
      print("There are no reports to show")
      return
   try:
      user_code = int(input("Enter the store ID: "))
      user_barcode = int(input("Enter the barcode: "))
   except ValueError:
      print("Enter Digits Only")
      return
   found = False
   for p in products:
      if user_code == p[0] and user_barcode == p[2]:
         found = True
         total_price = p[3]*p[4]
         print(f"{p[4]:,} unit{'s' if p[4]>1 else ''} of {p[1].title()} {'were' if p[4]>1 else 'was'} sold with the total price of ${total_price:,}")
   if not found:
      print(f"The storeID {user_code} not found")

# Display the best-selling and least-selling products
def bestSellingProducts():
   if not products:
      print("There are no products")
      return
   best_selling = products[0]
   least_selling = products[0]
   for p in products:
      if p[4] > best_selling[4]:
         best_selling = p
   print(f"The best-selling product is {best_selling[1].title()} with the sold unit{'s' if best_selling[4]>1 else ''} of {best_selling[4]:,}")
   for p in products:
      if p[4] < least_selling[4]:
         least_selling = p
   print(f"The least-selling product  is {least_selling[1].title()} with the sold unit{'s' if least_selling[4]>1 else ''} of {least_selling[4]:,}")

# Display pricy and cheap products
def pricyCheapProducts():
   if not products:
      print("There are no products")
      return
   pricy = products[0]
   cheap = products[0]
   for p in products:
      if p[3] > pricy[3]:
         pricy = p
   print(f"The product: {pricy[1].title()} is pricy, the price is ${pricy[3]:,}")
   for p in products:
      if p[3] < cheap[3]:
         cheap = p
   print(f"The product: {cheap[1].title()} is the cheapest product, the price is ${cheap[3]:,}")
menu()
