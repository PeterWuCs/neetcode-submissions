class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = [i for i in range(n)]
        size = [1] * n

        count = [n]

        def root(i):
            res = i
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        
        
        def union(i, j):

            root1 = root(i)
            root2 = root(j)

            if root1 != root2:
                if size[root1] > size[root2]:
                    parent[root2] = root1
                    size[root1] = size[root1] + size[root2]
                else:
                    parent[root1] = root2
                    size[root2] = size[root1] + size[root2]
                
                count[0] -= 1
            
        for i, j in edges:
            union(i, j)


        return count[0]
            






        