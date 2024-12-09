
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root):
    """
    :type root: Optional[TreeNode]
    :rtype: Optional[TreeNode]
    """

    if not root:
        return None
    
    if root.left:
        root.left = invertTree(root.left)
    if root.right:
        root.right = invertTree(root.right)
    temp = root.left
    root.left = root.right
    root.right = temp
    return root