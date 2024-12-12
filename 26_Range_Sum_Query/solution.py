class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums 

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        n = len(self.nums)
        sumArray = [0] * (n+1)

        for i in range(1,n+1):
            sumArray[i] = sumArray[i-1] + self.nums[i-1]

        return sumArray[right +1] - sumArray[left]







# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)