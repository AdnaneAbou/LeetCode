def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left = 0
    right = len(nums) -1
    mid = 0

    while left <= right:
        mid = (left + right ) // 2 
        if nums[mid] >= nums[left] and nums[left] > nums[right]:
            left = mid + 1 
        elif nums[mid] < nums[left]:
            right = mid
        elif nums[left] == nums[mid] or nums[left] <= nums[right]:
            print("ff")
            return nums[left]
    print(left)
    
    return nums[0]
    

print(findMin(nums =[2,1]))

# print(findMin(nums =[4,5,6,7,0,1,2]))

