
def maxsubarraysum(arr):
    # Your code here
    sums = 0
    maxi = float('-inf')
    starting=0
    ending=0
    temp_s=0
    for i in range(0, len(arr)):
        sums += arr[i]

        if sums > maxi:
            maxi = sums
            starting=temp_s
            ending=i

        if sums < 0:
            sums = 0
            temp_s=i+1
    subarray=arr[starting:ending+1]

    return maxi , subarray

print(maxsubarraysum([1, 3, -8, 7, -1, 2, 3]))