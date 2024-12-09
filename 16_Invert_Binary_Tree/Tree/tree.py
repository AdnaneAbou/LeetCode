
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):

        if not self.root:
            self.root = TreeNode(value)
            return
        
        def _insert_recursive(node, value):
            if not node:
                return TreeNode(value)
            
            if value < node.val:
                node.left = _insert_recursive(node.left, value)
            else:
                node.right = _insert_recursive(node.right ,value)

            return node
        
        return _insert_recursive(self.root,value)
    
    def inorder_traversal(self):
        result = []

        def _traverse(node):
            if node:
                _traverse(node.left)
                result.append(node.val)
                _traverse(node.right)

        _traverse(self.root)
        return result

    def preorder_traversal(self):
        result = []
        def _traverse(node):
            if node:
                result.append(node.val)
                _traverse(node.left)
                _traverse(node.right)
        _traverse(self.root)
        return result
    
    def postorder_traversal(self):
        result = []

        def _traverse(node):
            if node:
                _traverse(node.left)
                _traverse(node.right)
                result.append(node.val)
        _traverse(self.root)

        return result



values = [5,3,7,1,4,6,8]
# Demonstrate traversals
tree = BinaryTree()

for value in values:
    tree.insert(value)

print("Inorder Traversal (Left-Root-Right):", tree.inorder_traversal())
# Expected: [1, 3, 4, 5, 6, 7, 8]

print("Preorder Traversal (Root-Left-Right):", tree.preorder_traversal())
# Expected: [5, 3, 1, 4, 7, 6, 8]

print("Postorder Traversal (Left-Right-Root):", tree.postorder_traversal())
# Expected: [1, 4, 3, 6, 8, 7, 5]