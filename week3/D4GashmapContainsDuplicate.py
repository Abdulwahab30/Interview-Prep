def hashDuplicate(nums):
    dup={}
    for i in nums:
        if i not in dup:
            dup[i] = 1
        else:
            dup[i]+=1
            print("duplicate found")
            return True
    
    print("False")
    

hashDuplicate([1,2,3,4])