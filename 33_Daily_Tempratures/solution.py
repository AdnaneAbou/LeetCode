def dailyTemperatures(temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    result = [0] * len(temperatures)  # Initialize result with -1
    stack = []  # Monotonic decreasing stack

    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            index = stack.pop()
            result[index] = i - index
        stack.append(i)  


    return result

def dailyTemperatures_optimized(temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    



temperatures =[73,74,75,71,69,72,76,73]

print(dailyTemperatures(temperatures))