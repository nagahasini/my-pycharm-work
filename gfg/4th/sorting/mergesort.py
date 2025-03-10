def mergesort(a,low,high):

    if low>=high:
        return
    mid=(low+high)//2
    mergesort(a,low,mid)
    mergesort(a,mid+1,high)
    merge(a,low,mid,high)

def merge(a,low,mid,high):
   left=a[low:mid+1]
   right=a[mid+1:high+1]
   i=0
   j=0
   k=low
   while i<len(left) and j<len(right):
       if left[i]<right[j]:
           a[k]=left[i]
           i+=1
           k+=1
       else:
           a[k] = right[j]
           j+=1
           k+=1
   while i<len(left):
        a[k] = left[i]
        i += 1
        k += 1
   while j<len(right):
       a[k] = right[j]
       j += 1
       k += 1
   return a


ap=list(map(int,input("enter array:").split()))
mergesort(ap,0,len(ap)-1)
print(ap)








