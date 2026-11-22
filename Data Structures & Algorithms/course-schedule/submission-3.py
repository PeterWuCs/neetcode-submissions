class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)

        for i in range(len(prerequisites)):
            graph[prerequisites[i][1]].append(prerequisites[i][0])
        
        visited = set()
        visiting = set()


        def dfs(i):
            if i in visited:
                return True
            
            visited.add(i)
            visiting.add(i)

            for j in graph[i]:
                if j in visiting:
                    return False
                elif not dfs(j):
                    return False
            
            visiting.remove(i)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

        
            