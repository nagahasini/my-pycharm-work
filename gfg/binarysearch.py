def fun(arr,x):
    n=len(arr)
    f=0
    l=n-1

    while f<=l:
        mid = (f + l) // 2
        if arr[mid]==x:
            return mid
        elif x<arr[mid]:
            l=mid-1
        else:
            f=mid+1



a=fun([1,2,3],3)
print(a)

#------------- square root-----------
def Squareroot(num):
    low=0
    high=num
    ans=-1
    while low<=high:
        mid=(low+high)//2
        ms=mid*mid
        if ms==num:
            return mid
        elif ms>num:
            high=mid-1
        else:
            ans=mid
            low=mid+1

    return ans
