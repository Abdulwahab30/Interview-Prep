def charachterFrequency(word):
    # Initialize an empty dictionary to store characters as keys and counts as values
    duplicateNum = {}
    
    # Loop through each individual character in the string directly
    # 'i' will be 'h', then 'e', then 'e', etc.
    for i in word:
        # Check if the character is already a key in our dictionary
        if i in duplicateNum:
            # If it exists, increment its existing count by 1
            duplicateNum[i] += 1
        else:
            # If it's a brand new character, add it to the dictionary with a count of 1
            duplicateNum[i] = 1
        
    # Print the final dictionary showing the frequency of each character
    print(duplicateNum) 

# Test the function with a sample string
charachterFrequency("heellloo")