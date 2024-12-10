# This is the BFS Approach 
# Recursive max in python is 1000 by default 

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth_BFS( root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    if not root:
        return 0
    q = deque([(root, 1)])

    while q:
        node , depth = q.popleft()

        if not root.left and not node.right:
            return depth
        if node.left:
            q.append((node.left, depth+1))
        if node.right:
            q.append((node.right, depth+1))



def minDepth_DFS( root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    if not root:
        return 0
    stack = [(root, 1)]
    min_depth = float('inf')
    while stack:
        node , depth = stack.pop()
        if not node.left and not node.right :
            min_depth = min(min_depth, depth)
        if node.left:
            stack.append((node.left , depth +1))
        if node.right:
            stack.append((node.right, depth +1))
    return min_depth

root = TreeNode(3)
root.left = TreeNode(9)  
root.right = TreeNode(20)  
root.right.left = TreeNode(15)  
root.right.right = TreeNode(7)  

print(minDepth_DFS(root))