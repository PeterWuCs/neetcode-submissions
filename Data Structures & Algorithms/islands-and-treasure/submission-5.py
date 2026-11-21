class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        q = deque()
        

        n = len(grid)
        m = len(grid[0])


        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j))

        time = 0

        visited = set()

        q2 = deque()

        while q:
            for i in range(len(q)):
                row, col = q.popleft()

                if (row < 0 or row >= n or col < 0 or col >= m or 
                        grid[row][col] == -1 or (row, col) in visited):

                    continue
                
                visited.add((row, col))

                if grid[row][col] != 0:
                    grid[row][col] = time
                
                q2.append((row - 1, col))
                q2.append((row, col - 1))
                q2.append((row + 1, col))
                q2.append((row, col + 1))
            time += 1
            q, q2 = q2, q





