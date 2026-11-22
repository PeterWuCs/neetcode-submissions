class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        
        graph = defaultdict(list)

        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]

            graph[u].append(v)
            graph[v].append(u)

        visiting = set()
        visited = set()

        def dfs(i, parent):
            if i in visiting:
                return False
            
            if i in visited:
                return True
            
            visiting.add(i)
            
            for neb in graph[i]:
                if neb != parent:
                    res = dfs(neb, i)

                    if not res:
                        return False
            
            visited.add(i)
            visiting.remove(i)

            return True
        
        res = dfs(0, None)
        if not res:
            return False

        return len(visited) == len(graph)

