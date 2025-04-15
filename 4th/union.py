def union(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    i,j=0,0
    u=[]
    while i<n1 and j<n2:
        if arr1[i]<arr2[j]:
            if len(u)==0 or arr1[i]!=u[-1] :
                u.append(arr1[i])
            i+=1
        else:
            if  len(u) == 0 or arr2[j] != u[-1] :
                u.append(arr2[j])
            j+=1
    while i<n1:
        if arr1[i]!=u[-1] :
                u.append(arr1[i])
                i+=1
    while j<n2:
         if arr2[j]!=u[-1] :
                u.append(arr2[j])
                j+=1
    return u

print(union([1,2,2],[1,2,3]))

