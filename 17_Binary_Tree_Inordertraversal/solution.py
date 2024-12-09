# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def inorderTraversal(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """
    result = []

    def _inorder_traversal(node):
        if node:
            _inorder_traversal(node.left)
            result.append(node.val)
            _inorder_traversal(node.right)
    _inorder_traversal(root)

    return result
        