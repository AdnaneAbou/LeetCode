def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    start = 0
    end = k 

    average = 0.0
    

    for i in range(k):
        average += float(nums[i])/k

    maxaverage = average

    while end < len(nums):
        average = average + float(nums[end]) / k
        average = average - float(nums[start]) / k
        maxaverage = max(average, maxaverage)
        start = start +1 
        end = end +1 

    return maxaverage

        

nums= [1,12,-5,-6,50,3]
k = 4 

print(findMaxAverage(nums,k))