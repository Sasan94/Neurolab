# This line tries to get only digits.
try: 
  # This line is used get a two-digit number from a user.
  num = int(input("Type here: "))
  # check if the number has two digits.
  while num < 10 or num > 99: 
     # if the number does not contain two digits this asks to get a two-digit.
     num = int(input("Enter a two-digit number please: ")) 
  # to get the tens digit. 
  tens = num // 10 
  # to get the ones digit. 
  ones = num % 10 
  # This is used to rasie the tens digit to the power of ones digit and store it in power_result1 variable. 
  power_result1 = tens ** ones 
  # This is used to rasie the ones digit to the power of tens digit and store it in power_result2 variable. 
  power_result2 = ones ** tens 
  print(f"The result of {tens} to the power of {ones} is {power_result1:,} \nand {ones} to the power of {tens} one is {power_result2:,}")
# if the user types something except digits, it will ask to enter digits only.
except ValueError: 
   print("Enter Digits Only")
