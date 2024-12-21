# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    """
    :type root: Optional[TreeNode]
    :rtype: Optional[List]
    """
    output = []

    def recursive(node):
        if not node:
            return None
        recursive(node.left)
        output.append(node.val)
        recursive(node.right)
    recursive(root)

    return output


def balanceBST(root):
    """
    :type root: Optional[TreeNode]
    :rtype: Optional[TreeNode]
    """
    output = inorder_traversal(root)
    l,r= 0 , len(output) -1
    def recursive(l , r):
        if l > r:
            return None
        
        mid = (l+r)// 2 
        node = TreeNode(output[mid])
        node.left = recursive(l,r=mid-1)
        node.right = recursive( l =mid+1, r=r)
        return node

    return recursive(l,r)
print(1//2)



