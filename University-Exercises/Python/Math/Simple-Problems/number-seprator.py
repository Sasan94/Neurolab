'''
This program receives a number from the user,
extracts its digits,
and displays them in order.
'''

# Take a number from the user
num = int(input("Enter your number here: "))
temp = num   # Store the original number for later display

# Check if the number is zero and ask again until it is non-zero
while num == 0:
    num = int(input("Enter numbers greater than 0: "))

# Create a list to store the separated digits
num_separate = []

# While the number is greater than zero,
# divide the number by 10 to separate the last digit
while num > 0:
    remainder = num % 10           # Get the last digit of the number
    num = num // 10                # Remove the last digit from the number
    num_separate.append(remainder) # Add the digit to the list, which is num_separate

# Reverse the list so the digits appear in the correct order
num_separate.reverse()

# Print the original number and its separated digits
print(f"{temp} consists of the digits {num_separate}")
