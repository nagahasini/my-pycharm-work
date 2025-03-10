def selectionsort(arr):
    n=len(arr)
    for i in range(0,n-1):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
        arr[i], arr[mini] = arr[mini], arr[i]

    return arr


print(selectionsort([9,8,7,6,1,3]))