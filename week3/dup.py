def dup(nums):
    check={}
    result=False
    for i in nums:
        if i in check:
            check[i]+=1
            result=True
            
        else:
            check[i]=1
    print(result)
    return result
    
dup([1,2,3,1])

def ransomnote(r,m):
    r_map={}
    m_map={}

    for i in r:
        if i in r_map:
            r_map[i]+=1
        else:
            r_map[i] =1
    for i in m:
        if i in m_map:
            m_map[i]+=1
        else:
            m_map[i] =1

    # Check if the magazine has enough letters
    for i in r_map:
        # Using .get(i, 0) returns 0 if the letter 'i' is missing from the magazine
        if r_map[i] > m_map.get(i, 0):
            print("False")
            return  # Stop the function immediately since we can't build the note
            
    # If the loop finishes without returning False, we have everything we need!
    print("True")

# Test Cases
ransomnote("aa", "aab")   # Output: True
ransomnote("aaz", "aab")  # Output: False



def firstUniqChar(s):

    freq={}
    unique={}
    for i in s:
        if i in freq:
            freq[i]+=1
        else:
            freq[i] =1
    for i in range(len(s)):
        char = s[i]
        if freq[char] == 1:
            print(f"First unique is {char} at index {i}")
            return i
        else:
            pass
    

firstUniqChar("meetcode")
