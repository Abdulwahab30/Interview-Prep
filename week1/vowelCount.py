def vowelcount(word):
    vowels = ["a","e","i","o","u"]
    size=len(word)
    sv = len(vowels)
    count=0
    j=0
    for i in range(size):
        for j in range(sv):
            if word[i] == vowels[j]:
                count +=1
    print(count)
vowelcount("developer")




#another bertter implementation

def vowelcount(word):
    # Using a set is perfect here
    vowels = {"a", "e", "i", "o", "u"}
    count = 0
    
    # Just loop through each letter in the word directly
    for letter in word:
        # Check if the letter exists in the vowel set
        if letter in vowels:
            count += 1
            
    print(count)

vowelcount("developer") # Prints: 4