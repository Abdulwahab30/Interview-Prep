def revStr(word):
    reversedWord=word[::-1]

    print(reversedWord)

revStr("heello")


#Problem 2: Reverse Words
def revWord(word):
    temp=word.split()
    reversedWord=temp[::-1]

    print(reversedWord)

revWord("heello how are you")

#Problem 3: Remove Duplicates
def remDup(col):
    dupl=[]
    seen=set()
    for i in col:
        if i in seen:
            pass
        else:
            seen.add(i)
            dupl.append(i)
            
    print(dupl)
remDup([1,1,2,2,3,4,4])


#Problem 4: Move Zeroes

def rem0(nums):
    # 'a' will hold all the non-zero numbers
    a = []
    # 'b' will hold all the zeroes
    b = []
    
    # Loop through the list without modifying it
    for i in nums:
        if i == 0:
            b.append(i)  # Collect zeroes
        else:
            a.append(i)  # Collect everything else
            
    # Concatenate (merge) the two lists together, putting non-zeroes first
    concatlist = a + b
    print(concatlist)

# Test Case
rem0([0, 1, 0, 3, 12])  # Output: [1, 3, 12, 0, 0]