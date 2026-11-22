class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = [i for i in range(n) ]
        size = [1] * n

        def find(n):
            res = n

            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]

            return res
        
        def union(u, v):
            root1 = find(u)
            root2 = find(v)

            if root1 == root2:
                return 0
            
            if size[root1] > size[root2]:
                parent[root2] = root1
                size[root1] += size[root2]
            else:
                parent[root1] = root2
                size[root2] += size[root1]

            return 1
        
        res = n
        for u, v in edges:
            res -= union(u, v)
            
        return res
            
