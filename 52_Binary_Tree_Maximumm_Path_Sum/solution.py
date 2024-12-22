# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum( root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    max_sum = {"value" : float('-inf')}

    def recursive(node):
        
        if not node:
            return 0
        
        left = max(0,recursive(node.left))
        right = max(0,recursive(node.right))

        current_sum_subtree = left + right + node.val
        max_sum["value"] = max(max_sum["value"],current_sum_subtree)
        

        return node.val + max(left, right)
    recursive(root) 
    return max_sum["value"]
     

root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
print(maxPathSum(root))