def palindrome(word):

    reversedWord= word[::-1]
    print(reversedWord)
    if word == reversedWord:
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is Not a palindrome")

palindrome("madam")