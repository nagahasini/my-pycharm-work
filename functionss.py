#packing and unpacking
list=[1,2,3,4]
print(*list)
def add(a,b):
    return a+b

print(add(2,3))
def addition(*num):
    sum=0
    for i in num:
        sum=sum+i
    return sum

print(addition(1,2,3,4,5,6,7,8,9,10))
