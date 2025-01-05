import heapq
def kSmallestPairs(nums1, nums2, k):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: List[List[int]]
    """
    if not nums1 or not nums2:
        return []
    min_heap = []
    result = []
    visited = set()
    visited.add((0,0))
    heapq.heappush(min_heap,([nums1[0],nums2[0]],0,0))

    while min_heap and len(result) < k:
        current_sum , i , j = heapq.heappop(min_heap)
        result.append([nums1[i],nums2[j]])

        if i+1 < len(nums1) and (i+1,j) not in visited:
            current_sum = nums1[i+1]+ nums2[j]
            heapq.heappush(min_heap,(current_sum , i+1 ,j))
            visited.add((i+1,j))

        if j+1 < len(nums2) and (i,j+1) not in visited:
            current_sum = nums1[i]+ nums2[j+1]
            heapq.heappush(min_heap,(current_sum , i,j+1))
            visited.add((i,j+1))

            
    return result




print(kSmallestPairs(nums1 = [1,1,2], nums2 = [1,2,3], k = 2))
