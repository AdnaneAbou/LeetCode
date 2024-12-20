def minSubArrayLen(target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    l = 0 
    r = 0 
    sumWindow = 0
    result = float('inf')
    for r in range(len(nums)):
        sumWindow += nums[r]
        while sumWindow >= target and l <= r:
            sumWindow -= nums[l]
            result = min(result , r -l + 1 )
            l += 1 
    return 0 if result == float('inf') else result 





print(minSubArrayLen( target = 11, nums = [1,1,1,1,1,1,1,1]))
# print(minSubArrayLen( target = 7, nums = [2,3,1,2,4,3]))
# nums = [10, 20, 30, 40, 50]
