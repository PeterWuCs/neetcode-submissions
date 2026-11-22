class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        cycles = set()

        cycle_start = -1

        def dfs(i, parent):
            nonlocal cycle_start

            if i in visited:
                cycle_start = i
                cycles.add(i)
                return True

            visited.add(i)

            for j in graph[i]:
                if j != parent:
                    if dfs(j, i):
                        cycles.add(j)
                        if cycle_start == -1:
                            cycle_start = j
                            return True
                        if cycle_start == i:
                            cycle_start = -1
                            return False
                        return True
            return False
        
        dfs(1, None)
        print(cycles)
        for i in range(len(edges) - 1, -1, -1):
            if edges[i][0] in cycles and edges[i][1] in cycles:
                return edges[i]
        
