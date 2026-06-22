num =[5,2,9,1,7]
size=len(num)
print(size)
a=None
for m in range(size):
    if a == None:
        a=num[m]
    if num[m] > a:
        a=num[m]
        b=a
print(f"Largest number is {b}")