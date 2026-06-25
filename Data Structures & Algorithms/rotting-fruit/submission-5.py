class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))

        p = []

        count = -1
        visited = set()

        while q:
            i, j = q.pop()
                
                
            if grid[i][j] == 1:
                grid[i][j] = 2
            possible = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for k in range(4):
                new_i = i + possible[k][0]
                new_j = j + possible[k][1]

                if ((-1 < new_i < n)
                    and (-1 < new_j < m) 
                    and grid[new_i][new_j] == 1
                    and (new_i, new_j) not in visited):
                    visited.add((new_i, new_j))
                    p.append((new_i, new_j))
            if not q:
                count += 1
                p, q = q, p
            
        has_R = False
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
                if not has_R and grid[i][j] == 2:
                    has_R = True

        return count if has_R else 0








            

