def insert(intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    result = []
    n = len(intervals)
    i = 0

    while i < n and intervals[i][1] < newInterval[0]: 
        result.append(intervals[i])
        i += 1 
    
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0],intervals[i][0])
        newInterval[1] = max(newInterval[1],intervals[i][1])
        i += 1 
    result.append(newInterval)

    while i < n :
        result.append(intervals[i])
        i += 1 
    
    return result


print(insert(intervals = [[1,5]], newInterval = [0,0]))