def findOrder(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    graph = {i:[] for i in range(numCourses)}
    for course ,prereq in prerequisites:
        graph[course].append(prereq)
    print(graph)
    recStack = set()
    visited = set()
    res = []
    def dfs(course):

        if course in recStack:
            return False
        
        if course in visited:
            return True
        
        recStack.add(course)
        for prereq in graph[course]:
            if not dfs(prereq):
                return False
            
        recStack.remove(course)
        visited.add(course)
        res.append(course)

        return True

    for course in range(numCourses):
        if not dfs(course):
            return  []
        dfs(course)
    
    return res

print(findOrder(numCourses = 2, prerequisites = [[1,0]]))

# prerequisites = [[0,1]]