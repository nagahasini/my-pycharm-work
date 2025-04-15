def fre(arr):
    freq={}
    for i in range(0,len(arr)):
        if arr[i] in freq:
            freq[arr[i]]+=1
        else:
            freq[arr[i]]=1
    return freq




#sort array by frequencyy

def sortarraybyfrequency(arr):

    frequency=fre(arr)

    sorted_arr=sorted(arr, key=lambda x: (-frequency[x],x))
    return sorted_arr

array=[2,2,2,1,3,3,44,1]
a=sortarraybyfrequency(array)
print(a)
