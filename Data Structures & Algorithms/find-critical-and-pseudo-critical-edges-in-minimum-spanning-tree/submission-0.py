class UF:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1 for i in range(size)]

    def find(self, n):
        res = self.parent[n]
        while res != self.parent[res]:
            self.parent[res] = self.parent[self.parent[res]]
            res = self.parent[res]
        return res
    
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return False
        
        if self.size[u] > self.size[v]:
            self.parent[v] = u
            self.size[u] += self.size[v]
        else:
            self.parent[u] = v
            self.size[v] += self.size[u]

        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        def MST(uf, init_weight=0, index=-1):

            res = init_weight
            for u, v, w, i in edges:
                if i != index and uf.union(u, v):
                    res += w
            return res

        for i in range(len(edges)):
            edges[i].append(i)
        edges.sort(key=lambda ele: ele[2])

        uf = UF(n)
        mst = MST(uf)

        c, p = [], []

        for u, v, w, i in edges:
            uf = UF(n)
            new_mst = MST(uf, index=i)

            if max(uf.size) != n or new_mst != mst:
                c.append(i)
                continue

            uf = UF(n)
            uf.union(u, v)
            new_mst = MST(uf, init_weight=w, index=i)

            if new_mst == mst:
                p.append(i)

        return [c, p]








        