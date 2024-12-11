# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def isSameTree(p, q):
    """
    :type p: Optional[TreeNode]
    :type q: Optional[TreeNode]
    :rtype: bool
    """
    if not q or not p :
        return p == q
    
    return q.val == p.val and isSameTree(q.left,p.left) and isSameTree(p.right,q.right)

root_a = TreeNode(1)
root_a.left = TreeNode(2)
root_a.right = TreeNode(3)
root_b = TreeNode(1)
root_b.left = TreeNode(2)
root_b.right = TreeNode(3)

print(isSameTree(root_a,root_b))
