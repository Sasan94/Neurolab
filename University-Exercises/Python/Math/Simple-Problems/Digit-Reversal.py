#This takes just numbers
try:

  #Taking a tow-digit number from the user
  num = int(input("Type your number to get reversed: "))

  #This condition checks if the number is a two-digits 
  if num > 9 and num < 100:

    #Extrapolating tens from the number
    tens = num//10

    #Extrapolating ones from the number
    ones = num % 10

    #Swapping the value of variables, which are tens and ones
    tens, ones = ones, tens

    #This line is used to print the result using f-string
    print(f"The reverse of {num} is {tens}{ones}")

  #This line will be executed if the num is less than 10 or greater than 99
  else:
    print("Type a two-digit number please")

#This line is used to print a message in case the user types something except digits
except ValueError:
  print("Type numbers only")
  
