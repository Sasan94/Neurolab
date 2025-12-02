'''This program takes a number from the user and reverses its digits.'''

#Try taking digits from the user
try:
    #Take a number from the user
    num = int(input("Enter your number here: "))

    #Store the original number for displaying later
    tem = num

    #Check if the number is zero and ask again until it is non-zero
    while num == 0:
        num = int(input("Enter a number greater than zero: "))

    #If the number is negative, convert it to positive
    if num < 0:
        num = num * (-1)

    #Create a variable to store the reversed digits
    num_reverse = 0

    #Reverse the digits of the number
    while num > 0:
        # Extract the last digit from the number
        remainder = num % 10                         
        # Add the digit to the reversed number
        num_reverse = num_reverse * 10 + remainder
        # Remove the last digit from the number
        num = num // 10                              

    #Print the original number and its reversed form
    print(f"{tem} in reverse order is {num_reverse}")

#If the user enters sth except digits a message will be showed
except ValueError:
    print("Enter digits only")
