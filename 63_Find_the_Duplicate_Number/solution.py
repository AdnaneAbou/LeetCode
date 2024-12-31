def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    slow = nums[0]
    fast = nums[0]
    while True :

        slow = nums[slow]
        fast = nums[nums[fast]]

        if fast == slow :
            break

    slow2 = nums[0]
    while slow !=slow2:
        slow = nums[slow]
        slow2 = nums[slow2]
    
    return slow
        


print(findDuplicate(nums = [2,5,9,6,9,3,8,9,7,1]))