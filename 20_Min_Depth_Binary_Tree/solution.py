
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root):

    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    left_depth = float('inf') if root.left is None else minDepth(root.left)
    right_depth = float('inf') if root.right is None else minDepth(root.right)

    

    return 1 + min(left_depth, right_depth)


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)

# Call the function
depth = minDepth(root)
print("Minimum Depth:", depth)
