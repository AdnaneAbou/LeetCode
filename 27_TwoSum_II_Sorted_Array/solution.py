def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    start = 0
    end = len(nums) -1

    while start < end:
        if nums[start] + nums[end] == target:
            print('start',start,' end',end)
            return start +1, end+1
        
        if nums[start] + nums[end] > target:
            print('bb start',start,' end',end)
            end = end - 1 
        if nums[start] + nums[end] < target:
            print('start',start,' end',end)
            start += 1

    return -1
            

nums =  [2,7,11,15]
indices = twoSum(nums , target=9)
print(indices)