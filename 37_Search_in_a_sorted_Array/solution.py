def search(nums,target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
     
    l ,r = 0 , len(nums)-1

    while l <= r :
        mid = ( l+ r) // 2 
        if target == nums[mid]:
            return mid
        # Left sorted array 
        if nums[l] <= nums[mid]: # Binary search criteria , left < mid
            if target > nums[mid] or target  < nums[l] :
                l = mid + 1
            else:
                r = mid -1 
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1  
            else:
                l = mid + 1
    return -1
nums = [7,8,1,2,3,4,5,6]

print(search(nums,7))