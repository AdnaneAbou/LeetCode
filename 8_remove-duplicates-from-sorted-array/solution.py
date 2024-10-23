def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums: 
        return 0
    
    counter = 0
    
    for i in range(1, len(nums)):
        print(i)
        if nums[i] != nums[counter]:  
            counter += 1  
            nums[counter] = nums[i] 
    
    return counter + 1 , nums

nums = [0,0,1,1,1,2,2,3,3,4]

counter, return_list = removeDuplicates(nums)

print( counter ,return_list)