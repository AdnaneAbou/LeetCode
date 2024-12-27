from collections import deque
def floodFill(image, sr, sc, color):
    """
    :type image: List[List[int]]
    :type sr: int
    :type sc: int
    :type color: int
    :rtype: List[List[int]]
    """
    
    m  = len(image)
    n= len(image[0])
    starting_color = image[sr][sc]
    image[sr][sc] = color

    if starting_color == color:
        return image
    q = deque()
    q.append([sr,sc])

    while q:
        i , j  = q.popleft()
        if i+1 < m and image[i+1][j] == starting_color :
            image[i+1][j] = color 
            q.append([i+1,j])
        if i-1 > -1  and image[i-1][j] == starting_color :
            image[i-1][j] = color
            q.append([i-1,j])

        if j+1 < n and image[i][j+1] == starting_color :
            image[i][j+1] = color 
            q.append([i,j+1])

        if j-1 > -1  and image[i][j-1] == starting_color :
            image[i][j-1] = color
            q.append([i,j-1])

    return image

def floodFill_recursive(image, sr, sc, color):
    """
    :type image: List[List[int]]
    :type sr: int
    :type sc: int
    :type color: int
    :rtype: List[List[int]]
    """
    starting_color = image[sr][sc]
    if starting_color == color:
        return image
    
    def dfs(i,j):
        if i < 0 or i >=len(image) or j<0 or j >= len(image[0]) or image[i][j] != starting_color:
            return
        
        image[i][j] = color
        dfs(i+1,j)
        dfs(i-1,j)
        dfs(i,j+1)
        dfs(i,j-1)
    dfs(sr,sc)

    return image
   




print(floodFill_recursive(image = [[0,0,0],[0,0,0]], sr = 1, sc = 1, color = 1))