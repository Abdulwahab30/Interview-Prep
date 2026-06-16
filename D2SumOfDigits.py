
def sumOfDigits(num):
    a = str(num)
    print(a)
    size = len(a)
    x=0
    result=0
    for i in range(size):
        x=int(a[i])
        
        result=result+x
    print(result)
sumOfDigits(9001)

def sumOfDigits2(num):
    result=0
    newNumber=None
    if newNumber==None:
        newNumber=num
    while newNumber > 0:
        lastDigit= newNumber % 10
        print(lastDigit)
        
        newNumber= newNumber // 10
        print(newNumber)
        result=result+lastDigit
    print(result)
sumOfDigits2(9001)
