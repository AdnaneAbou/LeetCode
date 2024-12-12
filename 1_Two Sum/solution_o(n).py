def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    indices ={}
    for i in range(len(nums)):
        if target - nums[i] in indices:
            return [indices[target - nums[i]],i]
        indices[nums[i]] = i 

nums = [3,2,4]
indices = twoSum(nums , target=6)
print(indices)