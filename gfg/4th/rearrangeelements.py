def rearrangeelements(arr):
    p_a=[]
    n_a=[]
    for i in arr:
        if i>0:
            p_a.append(i)
        else:
            n_a.append(i)

    ans=[]
    i,j=0,0
    while i<len(p_a) and j<len(n_a):
        ans.append(p_a[i])
        ans.append(n_a[j])
        i+=1
        j+=1
    while i<len(p_a):
        ans.append(p_a[i])
        i+=1
    while j<len(n_a):
        ans.append(n_a[i])
        j+=1

    return ans

r=rearrangeelements([1,-2,3,4,-3,-6,-7])
print(r)



