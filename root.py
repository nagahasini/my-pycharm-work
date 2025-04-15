def root(m,n):
    if n==0:
        return 0
    if n==1:
        return 1
    low=1
    high=n
    while low<=high:
        mid=(low+high)//2
        if mid**m==n:
            return mid
        elif mid**m<n:
            low=mid+1
        else:
            high=mid-1
    return -1


a=root(3,125)
print(a)
