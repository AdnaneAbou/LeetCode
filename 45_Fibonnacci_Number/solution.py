def fib(n):
    """
    :type n: int
    :rtype: int
    """
    memo = {}
    memo[0]=0
    memo[1]=1

    def recursive(n):    
        if n in memo:
            return memo[n]
        if n <= 2:
            result = 1

        else:
            result =  recursive(n-1) + recursive(n-2)
        memo[n] = result

        return result
    return recursive(n)
import time
start_time = time.time()
result = fib(100)
end_time = time.time()

print(result)


execution_time = end_time - start_time
print(f"Execution time: {execution_time:.6f} seconds")