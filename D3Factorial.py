def factorial(num):
    # 1. Handle the negative number edge case first
    if num < 0:
        return "Factorial is not defined for negative numbers"
        
    # 2. Base case
    elif num == 0:
        return 1
        
    # 3. Recursive case
    else:
        return num * factorial(num - 1)

# Test cases
print(f"factorial is {factorial(3)}")   # Output: 6
print(factorial(-3))  # Output: Factorial is not defined for negative numbers