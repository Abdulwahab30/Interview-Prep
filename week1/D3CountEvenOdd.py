def countEO(numlist):
    # Initialize a dictionary to keep track of the counts for even and odd numbers
    countdict = {"even": 0, "odd": 0}
    
    # Loop through each actual number in the list directly
    for i in numlist:
        # If a number divided by 2 has a remainder of 0, it is even
        if i % 2 == 0:
            countdict["even"] += 1
        # Otherwise, the number must be odd
        else:
            countdict["odd"] += 1
            
    # Print the final dictionary showing both counts
    print(countdict)

# Test Cases
countEO([1, 2, 3, 4, 5, 6])  # Output: {'even': 3, 'odd': 3}
countEO([10, 20, 30])        # Output: {'even': 3, 'odd': 0}