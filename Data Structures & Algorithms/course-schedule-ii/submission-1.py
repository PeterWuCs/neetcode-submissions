class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)

        for i in range(len(prerequisites)):
            course = prerequisites[i][0]
            pre = prerequisites[i][1]

            graph[pre].append(course)

        

        res = []
        visited = set()
        visiting = set()

        def dfs(i):
            if i in visited:
                return True
            
            if i in visiting:
                return False

            
            visiting.add(i)

            for neb in graph[i]:
                if not dfs(neb):
                    return False
            
            visited.add(i)
            visiting.remove(i)
            res.append(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        res.reverse()
        return res


