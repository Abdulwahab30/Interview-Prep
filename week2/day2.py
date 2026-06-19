#Problem 5: Valid Palindrome

def palindrome(word):
    left=0
    right=len(word)-1

    while left < right:
        if word[left] != word[right]:
            print("Not Palindrome")
            break
        left+=1
        right-=1

    else:
        print("Palindrome")

palindrome("madam")


#Problem 6: Merge Sorted Arrays
def msa(a, b):
    combined = a + b
    size = len(combined)
    
    # Outer loop: Controls how many times we scan the entire list
    for pass_num in range(size):
        left = 0
        right = 1
        
        # Inner loop: Scans from left to right swapping adjacent elements
        while right < size:
            if combined[left] > combined[right]:
                # Swap them if they are in the wrong order
                combined[left], combined[right] = combined[right], combined[left]
            
            # Crucial: Always move BOTH pointers forward to scan the next pair
            left += 1
            right += 1
            
    print(combined)

msa([5, 1, 8], [6, 2, 0])  # Output: [1, 2, 3, 4, 5, 6]




# Problem 7: Remove Duplicates In-Place
def remDup(col):
    # 'j' is our writing pointer, starting at index 1
    j = 1
    
    # 'i' is our scout pointer, scanning the list from index 1 onward
    for i in range(1, len(col)):
        # Compare current element to the last confirmed unique element
        if col[i] != col[j-1]:
            # Overwrite the duplicate slot with the new unique value
            col[j] = col[i]
            # Move the writing pointer forward
            j += 1
            
    # Print the modified list up to index j (where unique elements end)
    print(col[:j])

remDup([1, 1, 2, 2, 3])  # Output: [1, 2, 3]


#Problem 8: Two Sum Sorted

def twoSum(nums,target):
    left=0
    right=len(nums)-1
    result=[]
    while left<right:
        if nums[left]+nums[right] == target:
            result=[nums[left],nums[right]]
            break
        elif nums[left]+nums[right] < target:
            left+=1
        else:
            right-=1
    print(result)

twoSum([1,2,3,4,6],6)