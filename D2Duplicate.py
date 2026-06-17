def duplicateCheck(numList):
    duplicateNum=[]
    seen=set()
    size=len(numList)
    for i in numList:
        if i in seen:
            duplicateNum.append(i)
        else:
            seen.add(i)
    print(duplicateNum) 

duplicateCheck([1,1,2,3,4,2])



