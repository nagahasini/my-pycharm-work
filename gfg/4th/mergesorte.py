def mergearrays(arr1,arr2):
    left,right=len(arr1)-1,0
    while left>=0 and right<len(arr2):
        if arr1[left]>arr2[right]:
            (arr1[left],arr2[right])=(arr2[right],arr1[left],)
            left-=1
            right+=1
        else:
            break
    arr1.sort()
    arr2.sort()

# method-2
def mergesortedarrays(a1,a2):
    i=0
    j=0
    m=len(a1)
    n=len(a2)
    r=[]
    while i<m and j<n:
        if a1[i]<a2[j]:
            r.append(a1[i])
            i+=1
        else:
            r.append(a2[j])
            j+=1
    while i<m:
        r.append(a1[i])
        i += 1
    while j<n:
        r.append(a2[j])
        j += 1
    return r

print(mergesortedarrays([3,10,20],[1,2,5]))



