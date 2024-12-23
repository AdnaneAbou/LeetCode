
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderBottom(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[List[int]]
    """
    if not root:
        return []
    
    q = deque()
    q.append(root)
    result = []
    result.append([root.val])

    while len(q) >0:
        current_level = []
        for i in range(len(q)):
            node = q.popleft()

            if node.left:
                q.append(node.left)
                current_level.append(node.left.val)
            if node.right:
                q.append(node.right)
                current_level.append(node.right.val)

        if current_level:
            result.append(current_level)
    result.reverse()
    return result
            
def postorder(root):
    result = []

    def recrusive(node):
        if not root:
            return None
        if node.left:
            recrusive(node.left)
        if node.right:
            recrusive(node.right)
        result.append(node.val)
    recrusive(root)

    return result


def bfs(root):
    if not root:
        return None

    q = deque()
    q.append(root)
    result = []
    while q:
        node = q.popleft()

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)   

        result.append(node.val)

    return result




root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# print(levelOrderBottom(root))
print(bfs(root))


