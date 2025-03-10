def intersection(a1,a2):
    n1=len(a1)
    n2=len(a2)
    i,j=0,0
    ans=[]
    while i<n1 and j<n2:
        if a1[i]<a2[j]:
            i+=1
        elif a1[i]>a2[j]:
            j+=1
        else:
            ans.append(a1[i])
            i+=1
            j+=1
    return ans

print(intersection([1,2,3,3],[1,3]))