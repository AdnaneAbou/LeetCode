class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res= []
        def backtrack(currentCombination , start):
            
            res.append(currentCombination[:])
            for i in range(start,len(nums)):
                currentCombination.append(nums[i])
                backtrack(currentCombination, i+1)
                currentCombination.pop()

        backtrack([],0)

        return res

sol = Solution()
print(sol.subsets(nums = [1,2,3]))