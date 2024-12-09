from collections import deque


def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    m = len(grid)
    n = len(grid[0])    

    def zero(i,j):
        if (i != m and i!=-1  and j!=n and j!=-1 and grid[i][j] == "1"):
            grid[i][j] = "0"
            zero(i+1,j)
            zero(i-1,j)
            zero(i,j+1)
            zero(i,j-1) 
        return
    
    total = 0 
    for i in range(m) :
        for j in range(n):
            if(grid[i][j] == "1"):
                zero(i,j)
                total += 1 
    return total

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(numIslands(grid))