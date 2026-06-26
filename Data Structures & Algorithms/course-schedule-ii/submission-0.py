class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)

        for i in range(len(prerequisites)):
            g[prerequisites[i][1]].append(prerequisites[i][0])

        vis = set()
        path = set()
        ans = [0] * numCourses 

        index = [numCourses - 1]

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
            ans[index[0]] = i
            index[0] -= 1

            
            return True

        for i in range(len(prerequisites)):
            if not dfs(prerequisites[i][1]):
                return []

        for k in range(numCourses):
            if k not in vis:
                ans[index[0]] = k
                index[0] -= 1
                
        return ans




