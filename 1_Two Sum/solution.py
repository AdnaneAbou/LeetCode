def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in reversed(range(len(nums))):
            if (nums[i] + nums[j] == target and i != j) :
                return i, j
            

nums = [3,2,4]
indices = twoSum(nums , target=6)
print(indices)