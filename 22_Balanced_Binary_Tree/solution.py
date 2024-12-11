# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def isBalanced(root):
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """

    if not root:
        return True
    def _isbalanced(node):
        if not node:
            return True,0
        
        left_balanced,left_height = _isbalanced(node.left)
        right_balanced,right_height = _isbalanced(node.right)

        is_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1

        
        return is_balanced , 1+ max(left_height,right_height)
    
    _, is_balanced = _isbalanced(root)

    return is_balanced



