class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        graph = defaultdict(list)

        for i in range(len(prerequisites)):
            pre = prerequisites[i][0]
            cou = prerequisites[i][1]

            graph[pre].append(cou)
        
        reachable = defaultdict(set)
        visited = set()

        def dfs(i):
            if i in visited:
                return

            visited.add(i)

            for neb in graph[i]:
                dfs(neb)

        for i in range(numCourses):
            dfs(i)
            reachable[i] = visited
            visited = set()

        res = []
        for i, j in queries:
            if j in reachable[i]:
                res.append(True)
            else:
                res.append(False)

        

        return res
            
            