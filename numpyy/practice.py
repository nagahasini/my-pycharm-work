# def duplicate_find(arr):
#     return len(set(arr)),set(arr)
#
#
# r=duplicate_find([1,1,1,2,2,2,2,2,3])
# print(r)
#
#
# def sorted_a(a):
#     for i in range(0,len(a)-1):
#         if a[i]>a[i+1]:
#             return False
#     return True
#
# print(sorted_a([2,3,44,5]))

def dup(array_1):
    i=0
    for j in range(1,len(array_1)):
        if array_1[i]!=array_1[j]:
            array_1[i+1]=array_1[j]
            i+=1
    return array_1[:i+1],i+1

print(dup([1,22,22,3]))