# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    
def kthSmallest(root, k):
    """
    :type root: Optional[TreeNode]
    :type k: int
    :rtype: int
    This Function has time complexity of O(n) and O(n) + list space
    """
    output = []

    def recursive(node):
        if not node:
            return None
    
        recursive(node.left)
        output.append(node.val)
        recursive(node.right)
    recursive(root)

    return output[k-1]


    