class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)

        for i in range(len(prerequisites)):
            g[prerequisites[i][1]].append(prerequisites[i][0])

        vis = set()
        path = set()

        def dfs(i):
            if i in path:
                return False
            if i in vis:
                return True

            vis.add(i)
            path.add(i)
            
            for j in range(len(g[i])):
                if not dfs(g[i][j]):
                    return False
            path.remove(i)
            
            return True

        for i in range(len(prerequisites)):
            if not dfs(prerequisites[i][1]):
                return False
        
        return True


            
