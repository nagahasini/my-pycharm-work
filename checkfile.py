#Array

from array import *
arr=array('i',[11,22,3,4])
for i in range(len(arr)):
    print(arr[i])

arr2=array(arr.typecode,[a for a in arr])
print(arr2)

arr3=array('i',[])
inn=int(input("enter size of array: "))
for i in range(inn):
    val=int(input("enter value" + str(i)))
    arr3.append(val)
print(arr3)

target=int(input("enter number u want to find: "))
for i in range(len(arr3)):
    if target==arr3[i]:
        print("element found at index"+ str(i))

#**************************** useee arr.index(target)*****************