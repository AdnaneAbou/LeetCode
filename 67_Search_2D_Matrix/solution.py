def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    j = 0
    while j < len(matrix[0]) and matrix[0][j] <= target:
        j += 1 

    i = 0
    while i < len(matrix) and matrix[i][0] <= target:
        i += 1 

    line = []

    # MAKE A LOOP TO PARSE A COLUMN OR A ROW 
    if i < j : 
        for m in range(0,i):
            for n in range(0,j):
                line.append(matrix[m][n])
    else:
        for n in range(0,j):
            for m in range(0,i):
                line.append(matrix[m][n])


    left = 0 
    right = len(line) -1
    line = sorted(line)

    while left <= right : 
        mid = (left + right) // 2 

        if line[mid] == target:
            return True
        elif line[mid] < target :
            left = mid + 1 
        elif line[mid] > target:
            right = mid -1 

    return False

def searchMatrix_Optimized(matrix, target):
    """
    :type: matrix: List[List[int]]
    :type: target: int
    :rtype: bool
    """
    n  , m = len(matrix[0]) , len(matrix)
    i = n - 1 
    j = 0
    while i < n and i >= 0 and j < m and j >= 0:
        current_element = matrix[j][i]
        if current_element == target:
            return True
        elif current_element > target:
            i -= 1
        else:
            j += 1 
    return False

print(searchMatrix_Optimized(matrix = [[-5]], target = -5))

