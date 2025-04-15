def longestconsecutive(nums):
    nums = sorted(set(nums))
    last_smaller=float('inf')
    current_len=0
    maxi=0
    for i in nums:
        if i-1==last_smaller:
            current_len+=1
        else:
            current_len=1

        last_smaller=i
        maxi=max(maxi,current_len)

    return maxi

r=longestconsecutive([1,1,2,2,100,101,101,102])
print(r)