from collections import deque
def orangesRotting(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = len(grid)
    n = len(grid[0])
    q = deque()
    counter = 0 
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                q.append([i,j])
            elif grid[i][j] == 1:
                counter += 1 
    if counter == 0:
        return 0 
    times = 0 
    q_length = len(q)
    while q:
        for _ in range(len(q)):
            i , j = q.popleft()

            if i+1 < m and grid[i+1][j] == 1 :
                grid[i+1][j] = 2 
                q.append([i+1,j])
                counter -= 1 
            if i-1 > -1  and grid[i-1][j] == 1 :
                grid[i-1][j] = 2 
                q.append([i-1,j])
                counter -= 1 
            if j+1 < n and grid[i][j+1] == 1 :
                grid[i][j+1] = 2 
                q.append([i,j+1])
                counter -= 1 

            if j-1 > -1  and grid[i][j-1] == 1 :
                grid[i][j-1] = 2 
                counter -= 1 
                q.append([i,j-1])
        if q:
            times += 1 

             
    return -1 if counter > 0 else times
        


# grid = [[2,1,1],[1,1,0],[0,1,1]]

# grid = [[2,1,1],[0,1,1],[1,0,1]]

grid = [[0]]
print(orangesRotting(grid))
