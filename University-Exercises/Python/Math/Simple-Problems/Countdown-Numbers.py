#Try getting digits
try:
   #Take a number from the user
   number = int(input("Type your number here: "))
    #Using a for loop to countdown the number 
    for i in range(number,0,-1):
       print(i)
#If the user types sth except digits, it asks the user to type digits only
except ValueError: 
    print("Enter digits only")