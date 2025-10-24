# To get numbers only
try:
    # To take numbers from the user
    num = int(input("Type your number here: "))

    # To count even numbers
    total = 0

    # Using a for loop to count numbers from 0 to 'num' with a step of 2 (even numbers)
    if num > 1:
        for i in range(0, num + 1, 2):
            # Add 1 to the total counter variable
            total += 1
            # Print even numbers in the loop
            print(i)
        # Print a separator line
        print("==")
        # Print how many even numbers are in the number range
        print(f"There are {total} even numbers in the range up to {num}.")
    
    elif num == 0:
        print("There is only 1 even number: 0.")
    
    else:
        print("Type a number greater than 1.")

# If the user types something other than digits, show this message
except ValueError:
    print("Type numbers only!")