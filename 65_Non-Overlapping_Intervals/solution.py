def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    counter = 0 
    n = len(intervals)
    intervals = sorted(intervals, key=lambda x : x[1])
    last = intervals[0][1]

    for i  in range(1,n):
        if last > intervals[i][0]:
            counter += 1 
        else:
            last = intervals[i][1]
    
    return counter
                


print(eraseOverlapIntervals(intervals = [[1,2],[2,3]]))