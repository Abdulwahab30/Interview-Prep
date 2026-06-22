def twoSumDict(nums,target):
    result={}
    for i in range(len(nums)):
        num = nums[i]
        c=target-num
        if c in result:
            print(f"Indices found: {[result[c], i]}")
            return
        else:
            result[num]=i


twoSumDict([3,2,4],6)

def charFreq(word):
    result={}
    for i in word:
        if i in result:
            result[i]+=1
        else:
            result[i]=1
    print(result)


charFreq("banana")


