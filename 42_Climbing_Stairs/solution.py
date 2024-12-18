from collections import defaultdict

def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    steps = [1,2]
    memo = defaultdict(lambda : 0)
    memo[0] = 1
    for i in range(1,n+1):
        memo[i] = 0

        for step in steps:
            subproblem = i - step

            if subproblem < 0:
                continue

            memo[i] = memo[i] +  memo[subproblem]
    return memo[n]


print(climbStairs(n=3))