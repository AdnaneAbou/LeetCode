from collections import deque
class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [[] for _ in range(self.V)]

    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self,start):
        visited = [False] * self.V
        result = []
        def _dfs(node):
            visited[node] = True
            result.append(node)

            for neighbour in  self.graph[node]:
                if not visited[neighbour]:
                    _dfs(neighbour)
        _dfs(start)
        return result

    def dfs_iterative(self, start):
        visited = [False] * self.V
        stack = []
        stack.append(start)
        visited[start] = True
        while stack:
            current = stack.pop()
            print(current,end="")

            for neighbour in self.graph[current]:
                if not visited[neighbour]:
                    stack.append(neighbour)
                    visited[neighbour] = True
    
    def bfs(self,start):
        seen = set()
        seen.add(start)
        q = deque()
        q.append(start)

        while q:
            node = q.popleft()
            print(node , end="")

            for neighbour in self.graph[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    q.append(neighbour)




g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
print(g.graph)

g.dfs_iterative(0)

print(g.dfs(0))

g.bfs(0)