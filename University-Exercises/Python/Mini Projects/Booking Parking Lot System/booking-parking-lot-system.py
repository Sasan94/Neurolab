#Decaler A global array to be used throughout the code
spots = []
#This function creates the whole parking lot
def createParkingLot():
   global spots
   try:
      row = int(input("To create a parking lot enter rows: "))
      col = int(input("To create a parking lot enter columns: "))
   except ValueError:
      print("Enter Digits Only")
   spots = []
   for i in range(row):
      temp = []
      for j in range(col):
         temp.append(0)
      spots.append(temp)
   for row in spots:
      print(row)
#This fuction display the parking lot
def display():
   for spot in spots:
      print(spot)
#This function allows the user to book spots
def book():
   try:
      r = int(input("Enter the row to book a spot: "))
      c = int(input("Enter the column to book a spot: "))
   except ValueError:
      print("Enter Digits Only")
   if r < 1 or r > len(spots) or c < 1 or c > len(spots[0]):
      print("The number is out of parking spot range")
      return
   if spots[r-1][c-1] == 0:
      spots[r-1][c-1] = 1
      print("The spot has been booked")
   else:
      print("The spot is taken")
#This function allows the user to cancel spots
def cancel():
   try:
      r = int(input("Enter the row to book a spot: "))
      c = int(input("Enter the column to book a spot: "))
   except ValueError:
      print("Enter Digits Only")
   if r < 1 or r > len(spots) or c < 1 or c > len(spots[0]):
      print("The is out of parking lot range")
      return
   if spots[r-1][c-1] == 1:
      spots[r-1][c-1] = 0
      print("The spot has been canceled")
   else:
      print("The spot is already available")
#This function allows the user to get report of booked and available spots
def report():
   booked = 0
   empty = 0
   row = len(spots) 
   col = len(spots[0])
   for i in range(row):
      for j in range(col):
         if spots[i][j] == 1:
            booked += 1
         else:
            empty += 1
   print(f"Booked Spots = {booked}")
   print(f"Available Spots = {empty}")
#This function allows the user to take the total revenue 
def revenue():        
   row = len(spots)
   col = len(spots[0])
   booked = 0
   price = 2
   for i in range(row):
      for j in range(col):
         if spots[i][j] == 1:
            booked += 1
   revenue = booked * price
   print(f"Total Revenue = ${revenue:,}")
#Display the main menu
def menu():
   while True:
      print("\n========== Booking Ticket System ==========")
      print("\n0.Create Parking Lot")
      print("1.Display The Capacity Of Parking Lot")
      print("2.Book Spots")
      print("3.Cancel Spots")
      print("4.Spots Report")
      print("5.Revenue Report")
      print("6.Exit The Program")
      print("\n")
      try:
         choice = int(input("Select one of the options above: "))
      except ValueError:
         print("Enter Digits Only")
         continue
      if choice == 0:
         createParkingLot()
      elif choice == 1:
         display()
      elif choice == 2:
         book()
      elif choice == 3:
         cancel()   
      elif choice == 4:
         report()
      elif choice == 5:
         revenue()
      elif choice == 6:
         print("Exiting The Program...")
         exit()
      else:
         print("Please Choose One Of The Options Above")
menu()
