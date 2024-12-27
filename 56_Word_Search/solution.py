def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    start = []

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                start.append([i,j])

    def backtrack(i,j,k):

        if len(word) == k :
            return True
        
        if i < 0 or i >= len(board) or j <0 or j>= len(board[0]) or board[i][j] != word[k]:
            return False
        
        temp = board[i][j]
        board[i][j] = '#'

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for di , dj in directions:
            ni, nj = i + di , j + dj
            if backtrack(ni,nj,k+1):
                return True
        
        board[i][j] = temp

        return False
    
    for i , j in start:
        if backtrack(i,j,0):
            return True
    
    return False

print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))