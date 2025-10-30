# Define a function named 'abso' that takes one number as input
def abso(num):
    # If the number is negative, multiply it by -1 to make it positive
    if num < 0:
        return num * (-1)
    # Otherwise, return the number as it is (already positive)
    else:
        return num

# Try to run the following code block and handle any possible errors
try:
    # Ask the user to enter a number and convert the input to an integer
    num = int(input("Type your number here: "))
    # Call the 'abso' function with the user's input and store the result
    result = abso(num)
    # Print the absolute value result
    print(result)

# If the user enters something that is not a number, show an error message
except ValueError:
    print("Please type digits only")