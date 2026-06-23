class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        index_set = set()
        n = len(grid)
        m = len(grid[0])

        def dfs(i, j, size):
            if (i, j) in index_set:
                return size
            if grid[i][j] == 0:
                return size

            size += 1
            index_set.add((i, j))

            possible_i = []
            possible_j = []

            if i > 0:
                possible_i.append(-1)
            if j > 0:
                possible_j.append(-1)
            if i < n - 1:
                possible_i.append(1)
            if j < m - 1:
                possible_j.append(1)

            total = 0
            for num in possible_i:
                total += dfs(i + num, j, 0)
            for num in possible_j:
                total += dfs(i, j + num, 0)

            return size + total


        biggest = 0



        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    size = dfs(i, j, 0)
                    biggest = max(biggest, size)
                    
        return biggest
                
        
                    