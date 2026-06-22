def removeDDuplicate(a):
    # Create an empty list to store our final unique elements
    unique_list = []
    # Create a set for fast O(1) lookups to track items we've already met
    seen = set()

    for i in a:
        # If we haven't seen this item before, it's unique so far!
        if i not in seen:
            unique_list.append(i) # Add it to our clean results list
            seen.add(i)           # Mark it as seen so we don't add it again
            
    # Print our brand new list that contains no duplicates
    print(unique_list)

# Test Cases
removeDDuplicate([1, 2, 2, 3, 1, 4])  # Output: [1, 2, 3, 4]
removeDDuplicate(["a", "b", "a", "c"]) # Output: ['a', 'b', 'c']