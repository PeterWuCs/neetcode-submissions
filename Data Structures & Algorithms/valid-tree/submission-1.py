class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = defaultdict(list)
        
        for i in range(len(edges)):
            g[edges[i][0]].append(edges[i][1])
            g[edges[i][1]].append(edges[i][0])

        path = set()
        visited = set()
        def dfs(i, last):
            if i in path:
                return True
            
            if i in visited:
                return False

            path.add(i)
            visited.add(i)
            
            for v in g[i]:
                if dfs(v, i) and v != last:
                    return True

            return False

        if dfs(0, None):
            return False
        
        return len(visited) == n
                
