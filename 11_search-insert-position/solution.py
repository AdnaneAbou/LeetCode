def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l = 0
    h = len(nums) -1 
    while l <= h:
        mid = (l+h) // 2
        if (nums[mid] == target):
            return mid
        elif(nums[mid] < target):
            l = mid + 1
        else:
            h = mid -1 
    
    return l

nums = [1,3,5,6]
print(searchInsert(nums , 2))
