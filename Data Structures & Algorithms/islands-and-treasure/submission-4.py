class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        n = len(grid)
        m = len(grid[0])

        def bfs(c):
            p = c
            q = []
            count = 0
            l = len(c)

            while p:
                
                i, j = p.pop()
                if not ((i < 0 or j < 0 or i > n - 1 or j > m - 1 or
                    grid[i][j] != 2147483647) and l <= 0):
                    grid[i][j] = count
                    q.append((i - 1, j))
                    q.append((i, j - 1))
                    q.append((i + 1, j))
                    q.append((i, j + 1))
                l -= 1
            
                if not p:
                    count += 1
                    p, q = q, p

        chests = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    chests.append((i, j))
        
        bfs(chests)

                    

