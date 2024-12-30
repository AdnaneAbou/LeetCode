def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    recStack = set()
    graph = {i : [] for i in range(numCourses)}

    for course , prereq in prerequisites:
        graph[course].append(prereq)


    def dfs(course):

        if graph[course] == []: 
            return True
        if course in recStack :
            return False
        
        recStack.add(course)

        for prereq in graph[course]:
            if not dfs(prereq):
                return False
            
        recStack.remove(course)
        graph[course] = []            
        return True


        
    for course in range(numCourses):
        
        if not dfs(course):
            return False
                 
    return True
        


print(canFinish(numCourses = 2, prerequisites = [[1,0]]))