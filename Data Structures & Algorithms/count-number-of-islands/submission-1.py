class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        n = len(grid)
        m = len(grid[0])

        count = 0

        def dfs(k , t):
            if (k, t) in visited:
                return
            visited.add((k, t))
            if t < m - 1 and grid[k][t + 1] == '1':
                dfs(k , t + 1)

            if t > 0 and grid[k][t - 1] == '1':
                dfs(k , t - 1)

            if k > 0 and grid[k - 1][t] == '1':
                dfs(k - 1, t)               

            if k < n - 1 and grid[k + 1][t] == '1':
                dfs(k + 1, t)

        

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i, j) not in visited:
                    count += 1
                    dfs(i, j)
        return count


    
        





