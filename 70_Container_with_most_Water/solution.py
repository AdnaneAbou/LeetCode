import time
def maxArea(height):
    """
    :type: height: List[int]
    :rtype : int
    """
    left  = 0 
    right = len(height) -1
    max_area = 0 
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        if area > max_area:
            max_area = area
        
        if height[left] < height[right] : 
            left += 1
        else : 
            right -= 1

    return max_area

# Time function1
start = time.perf_counter()
height = [1,8,6,2,5,4,8,3,7]
print(maxArea( height = height))
end = time.perf_counter()
print(f"Function 1: {end - start:.4f} seconds")

