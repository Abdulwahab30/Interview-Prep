def allDup(nums):
    freq={}
    seen=set()
    result={}
    for i in nums:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    
    for key,value in freq.items():
        if freq[key]>1:
            result[key] = freq[value]
    
    print(result)

allDup([4,3,2,7,8,2,3,1])