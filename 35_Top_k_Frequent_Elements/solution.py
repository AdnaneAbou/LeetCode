import heapq
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """

    hashmap = {}

    for num in nums:
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1
    heap_min = []

    for num,freq in hashmap.items():

        heapq.heappush(heap_min,(freq, num))

        if len(heap_min) > k :
            heapq.heappop(heap_min)

    return [ num for freq , num in heap_min]


nums = [1,1,1,2,2,3]

print(topKFrequent(nums,k=2))