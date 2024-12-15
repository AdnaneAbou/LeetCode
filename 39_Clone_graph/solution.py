
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
  
def cloneGraph(node):
    """
    :type node: Node
    :rtype: Node
    """
    if not node:
        return None
    if not node.neighbors:
        return Node(node.val,[])
    
    visited = {}

    def dfs(node):
        if node in visited:
            return visited[node]
        
        clone_node = Node(node.val)
        visited[node] = clone_node

        for neighbor in node.neighbors:
            clone_node.neighbors.append(dfs(neighbor))

        return clone_node
    
    return dfs(node) 
