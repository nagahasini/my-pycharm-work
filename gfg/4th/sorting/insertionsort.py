def insertionsort(arr):
    n=len(arr)
    for i in range(1,n):
        temp=arr[i]
        j=i-1
        while j>=0 and arr[j]>temp:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp

    return arr

print(insertionsort([8,7,1]))
