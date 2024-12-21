# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root, targetSum):
    """
    :type root: Optional[TreeNode]
    :type targetSum: int
    :rtype: bool
    """
    def recursive(node,sum):
        
        if not node:
            return False
        
        sum += node.val

        if not node.left and not node.right:
            return sum == targetSum
     
        return recursive(node.right,sum) or recursive(node.left,sum)
         
    return recursive(root, 0)
