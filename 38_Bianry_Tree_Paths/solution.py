# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binaryTreePaths( root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[str]
    """
    if not root:
        return None
    result = []
    current_path = ""
    def _traverse(node, current_path):
        current_path += f'{node.val}->'

        if not node.left and not node.right:
            result.append(current_path)
    
        if node.left :
            _traverse(node.left,current_path)
        if node.right:
            _traverse(node.right,current_path)
            
    _traverse(root,current_path)
    return result
    


