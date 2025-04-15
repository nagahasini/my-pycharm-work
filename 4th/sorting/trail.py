def mergesort(arr,low,high):
    if low>=high:
        return
    mid=(low+high)//2
    mergesort(arr,low,mid)
    mergesort(arr,mid+1,high)
    merge(arr,low,mid,high)


def merge(arr,low,mid,high):
    left=arr[low:mid+1]
    right=arr[mid+1:high+1]
    i,j,=0,0
    k=low
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
            k+=1
        else:
            arr[k] = right[j]
            j += 1
            k += 1
    while i<len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j<len(right):
        arr[k]=right[j]
        j += 1
        k += 1



array=list(map(int,input("enter").split()))
(mergesort(array,0,len(array)-1))
print(array)