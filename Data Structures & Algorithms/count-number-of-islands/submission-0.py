class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        graph = {}

        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    graph[(i, j)] = []
                        
                    if j < m - 1 and grid[i][j + 1] == '1':
                        graph[(i, j)].append((i , j+ 1))

                    if j > 0 and grid[i][j - 1] == '1':
                        graph[(i, j)].append((i , j - 1))

                    if i > 0 and grid[i - 1][j] == '1':
                        graph[(i, j)].append((i - 1, j))

                    if i < n - 1 and grid[i + 1][j] == '1':
                        graph[(i, j)].append((i + 1 , j))

        
        visited = {}
        count = 0
        def dfs(v):
            visited[v] = True
            for u in graph[v]:
                if not visited.get(u):
                    dfs(u) 
        
        for key in graph:
            if not visited.get(key):
                print("key",key)
                count += 1
                dfs(key)

        return count


    
        





