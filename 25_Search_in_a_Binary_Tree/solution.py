# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
def searchBST( root, val):
    """
    :type root: Optional[TreeNode]
    :type val: int
    :rtype: Optional[TreeNode]
    """
    if not root:
        return None
    
    if root.val == val:
        return root
    
    left_search = searchBST(root.left, val)
    if left_search:
        return left_search
    
    return searchBST(root.right, val)
    


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)

print(searchBST(root , val=1))