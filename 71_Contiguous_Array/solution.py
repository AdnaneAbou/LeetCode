def findMaxLength( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sum_map = {0: -1}
    max_length = 0
    current_sum = 0
    
    for i in range(len(nums)):
        if nums[i] == 0:
            current_sum -= 1
        else:
            current_sum += 1
        
        if current_sum in sum_map:
            max_length = max(max_length, i - sum_map[current_sum])
        else:
            sum_map[current_sum] = i
    
    return max_length



def findMaxLength_( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    one ,zero = 0,0
    res = 0 

    diff_index = {}

    for i , n in enumerate(nums):
        if n == 0:
            zero += 1 
        else:
            one += 1  
        if one - zero not in diff_index:
            diff_index[one - zero ] = i
        if one == zero :
            res = one + zero
        else:
            idx = diff_index[one - zero]
            res = max(res , i - idx)


    return res 
        

    


print(findMaxLength_(nums=[1,1,1,0,0,0]))
print(findMaxLength(nums=[1,1,1,0,0,0]))
    
  