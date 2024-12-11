# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def maxDepth(root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    if root == None:
        return 0
    
    return 1 + max(maxDepth(root.left),maxDepth(root.right))

