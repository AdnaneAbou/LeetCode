def nextGreaterElement(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    numsIdsx = { n:i for i, n in enumerate(nums1)}
    res = [-1] * len(nums1)

    stack = []
    for i in range(len(nums2)):
        curr = nums2[i]
        while stack and curr > stack[-1]:
            val = stack.pop()
            idx = numsIdsx[val]
            res[idx] = curr
        if curr in numsIdsx:
            stack.append(curr)
    return res


def nextGreaterElement_(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    Traversing the array from left to right
    """

    result = [-1]* len(nums1)
    stack = []
    nums_to_id = {n:i for i,n in enumerate(nums1)}
    
    
    for i in range(len(nums2)-1,-1,-1):
        
        while stack and stack[-1] <= nums2[i]:
            stack.pop()
        
        if stack and nums2[i] in nums_to_id.keys():
            idx = nums_to_id[nums2[i]]
            result[idx] = stack[-1]

        stack.append(nums2[i])
    

    return result


nums1 = [4,1,2]
nums2 = [1,3,4,2]

print(nextGreaterElement(nums1,nums2))