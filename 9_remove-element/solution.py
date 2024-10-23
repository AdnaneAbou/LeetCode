def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    counter = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[counter] = nums[i]
            counter += 1
    
    return counter , nums

nums = [0,1,2,2,3,0,4,2]
val = 2

counter , nums = removeElement(nums,val)

print(counter , nums)


    