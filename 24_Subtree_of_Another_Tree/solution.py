# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p,q):
    if not p and not q:
        return True
    if p and q and p.val == q.val: 
        return isSameTree(p.left,q.left) and  isSameTree(p.right,q.right)
    return False

def isSubtree(root, subRoot):
    """
    :type root: Optional[TreeNode]
    :type subRoot: Optional[TreeNode]
    :rtype: bool
    """
    if  not subRoot: return True
    if not root: return False

    return isSameTree(root, subRoot) or isSubtree(root.left , subRoot) or isSubtree(root.right,subRoot) 


root = TreeNode(1)
root.left = None
root.right = TreeNode(1,TreeNode(1,TreeNode(1,TreeNode(1,TreeNode(1,TreeNode(1,TreeNode(1,TreeNode(1,TreeNode(2)))))))))

subRoot = TreeNode(1,TreeNode(1,TreeNode(1,TreeNode(1,TreeNode(1,TreeNode(1,TreeNode(2)))))))

print(isSubtree(root,subRoot))