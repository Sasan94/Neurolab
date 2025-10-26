# factorial_with_for.py
# Program to calculate factorial using a for loop
# Mathematical formula : 5! = 5 × 4 × 3 × 2 × 1

# Taking a number from the user 
n = int(input("Type your number here: "))

# Initializing a variable to store the factorial value 
fact = 1

# Using a for loop that counts from 1 to the user’s number.
# In each iteration, multiply the current value of factorial by i,
# and store the result back in factorial.
for i in range(1, n + 1):
    fact *= i  # shorthand for fact = fact * i

# Printing the result using an f-string
print(f"The factorial of {n} is {fact}")