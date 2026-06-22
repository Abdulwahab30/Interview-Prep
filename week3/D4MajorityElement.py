def getMajorityelement(nums):
    freq={}
    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i]= 1
    
    for i in freq:
        c = freq[i]
        if c > len(nums)//2:
            print(f"The majority element is {i} (appears {c} times)")
            return i
        else: 
            pass

getMajorityelement([2,2,1,1,1,2,2])
