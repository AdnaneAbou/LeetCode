def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    start = 0
    end = len(nums) -1

    while start < end:
        if nums[start] + nums[end] > target:
            print('start',start,' end',end)
            end -= 1 
        elif nums[start] + nums[end] < target:
            print('start',start,' end',end)
            start += 1
        elif nums[start] + nums[end] == target:
            print('start',start,' end',end)
            return start , end
    return -1
            

nums = [2,3,4]
indices = twoSum(nums , target=6)
print(indices)