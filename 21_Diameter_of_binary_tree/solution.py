# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root):
    if not root:
        return 0,0


    left_height , left_diameter = dfs(root.left)
    right_height , right_diameter = dfs(root.right)

    height = 1 + max(left_height, right_height)
    diameter = max(left_diameter, right_diameter, right_height + left_height)

    return height , diameter



def diameterOfBinaryTree(root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    _, diameter = dfs(root)
    return diameter

root = TreeNode(1)
root.left = TreeNode(2)  
root.right = TreeNode(3)  
root.right.left = TreeNode(4)  
root.right.right = TreeNode(5)  

print(diameterOfBinaryTree(root))