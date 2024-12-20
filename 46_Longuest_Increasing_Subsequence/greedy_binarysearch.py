import bisect
def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sub = []

    for num in nums:
        
        pos = bisect.bisect_left(sub,num)

        if pos == len(sub):
            sub.append(num)
        
        else:
            sub[pos] = num

    return len(sub)

nums = [10,9,2,5,3,7,101,18]

print(lengthOfLIS(nums))
