def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    paths = []

    def backtrack(path, used):

        if len(path) == len(nums):
            paths.append(list(path))
            return
        
        for i in range(len(nums)):

            if used[i]:
                continue

            path.append(nums[i])
            used[i] = True

            backtrack(path,used)

            path.pop()
            used[i] = False

    backtrack([],[False]* len(nums))

    return paths

nums = [1,2,3]


print(permute(nums))

