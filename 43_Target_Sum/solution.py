def findTargetSumWays(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    hashmap = {}

    def backtrack(index , total):
        if index == len(nums):
            return 1 if target == total else 0 
        
        if (index , total) in hashmap:
            return hashmap[(index,total)]
        
        hashmap[(index , total)] = (backtrack(index +1 , total + nums[index]) +
                                    backtrack(index +1 , total - nums[index]) )
       
        return hashmap[(index , total)]
    
    return backtrack(0,0)

nums = [1,1,1,1,1]


print(findTargetSumWays(nums,target=3))