class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1

        parent = [i for i in range(n)]
        size = [1] * n

        def root(i):
            res = i

            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res

        def union(i, j):
            
            r1 = root(i)
            r2 = root(j)

            if r1 == r2:
                return True
            if size[r1] >= size[r2]:
                size[r1] += size[r2]
                parent[r2] = r1
            else:
                size[r2] += size[r1]
                parent[r1] = r2

            return False

        result = []
        for i, j in edges:
            if union(i, j):
                result = [i, j]

        return result

        