def BinarySearch(nums , target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l = 0
    h = len(nums) - 1

    while (l <= h):
        mid = (l + h)//2
        if (target == nums[mid]):
            return mid
        elif (target < nums[mid]):
            h  = mid - 1 
        else:
            l = mid + 1

    return -1

nums = [1,2,3,5,8,12,66,89]

result = BinarySearch(nums, target = 1)

print(result)