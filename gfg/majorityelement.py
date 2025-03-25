from pandas.core.common import not_none


def majority_element(arr1):
    freq={}
    for i in arr1:
        if i in freq :
            freq[i]+=1
        else:
            freq[i]=1
    for x in freq:
        if freq[x]>len(arr1)//2:
            return x

    return -1

r=majority_element([1,1,1,1,2])
print(r)


def majority(arr):
    c=0
    candidate=None

    for i in arr:
        if c==0:
            candidate=i
        if i==candidate:
            c+=1
        else:
            c-=1

    c2=0
    for i in arr:
        if i==candidate:
            c2+=1
    if c2>len(arr)//2:
        return candidate

r2=majority([1,1,1,1,1,2,2])
print(r2)