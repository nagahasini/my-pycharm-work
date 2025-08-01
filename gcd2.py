# find count
def lower_bound(arr,x):
    low=0
    high=len(arr)-1
    ans=len(arr)
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=x:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
def upper_bound(arr,x):
    low=0
    high=len(arr)-1
    ans=len(arr)
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>x:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
def count_occurances(arr,x):
    l=lower_bound(arr,x)
    u=upper_bound(arr,x)-1
    return (u-l)+1


print(lower_bound([1,2,3,4],3))
print(upper_bound([1,2,3,4],3))
a11=count_occurances([1,22,22],22)
print(a11)



