# Take a number from the user and convert it to integer
num = int(input("Enter a number: "))

# If it's negative, turn it into positive
if num < 0:
    num = -num

# Variable to keep the largest digit found so far
largest = 0

# While the number still has digits
while num > 0:
    
    # Get the last digit (remainder of division by 10)
    digit = num % 10        
    # If it's greater than current largest, update it
    if digit > largest:     
        largest = digit
        
    # Remove the last digit (integer division by 10)
    num //= 10              

# Print the largest digit after checking all digits
print(f"The largest digit is: {largest}")