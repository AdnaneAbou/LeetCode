def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    array = [[] for i in range(len(nums)+1)]

    hashmap = {}

    for num in nums:
        if num not in hashmap:
            hashmap[num] = 1 
        else:
            hashmap[num] += 1 
        
    for num,count in hashmap.items():
        array[count].append(num)

    result = []
    for i in range(len(array)-1,0,-1):
        for num in array[i]:
            result.append(num)
            if len(result) == k:
                return result


nums = [1,1,1,2,2,3]

print(topKFrequent(nums,k=2))