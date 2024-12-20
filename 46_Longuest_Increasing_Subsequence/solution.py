def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dp = [1]*len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i] :
                dp[i] = max(dp[i], 1 + dp[j])

    return max(dp)


nums = [10,9,2,5,3,7,101,18]

print(lengthOfLIS(nums))
