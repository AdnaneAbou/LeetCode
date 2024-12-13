import heapq
def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    min_heap = []

    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap,num)
        else:
            if num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap,num)
    
    return min_heap[0]

nums = [3,2,1,5,6,4]

print(findKthLargest(nums, k=2))