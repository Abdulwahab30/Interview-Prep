def fibonacci(num):
    # Initialize the list with the first two base numbers of the sequence
    fib = [0, 1]
    
    # Edge Case 1: Handle invalid negative numbers
    if num < 0:
        print("Number should be positive")
    # Edge Case 2: Handle zero input
    elif num == 0:
        print("Number should be greater than 0")
    # Edge Case 3: If requesting 1 number, print just the first element [0]
    elif num == 1:
        print(fib[0])
    # Edge Case 4: If requesting 2 numbers, print the initial list [0, 1] directly
    elif num == 2:
        print(fib)
    # General Case: For 3 or more numbers, calculate the rest dynamically
    else:
        # Loop from index 2 up to (num - 1)
        for i in range(2, num):
            # Sum the last two numbers in the list and append the result to the end
            fib.append(fib[i-1] + fib[i-2])
        # Print the fully generated sequence
        print(fib)

# Test the function to generate the first 8 Fibonacci numbers
fibonacci(8)