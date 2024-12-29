def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    res = []
    
    def backtrack(currentCombination, currentSum , start):
        if currentSum == target:
            res.append(currentCombination[:])
            return

        if currentSum > target:
            return
        
        for i in range(start, len(candidates)):
            currentCombination.append(candidates[i])
            backtrack(currentCombination,currentSum + candidates[i], i)
            currentCombination.pop()
    
    backtrack([],0,0)


    return res


print(combinationSum(candidates = [2,3,6,7], target = 7))

