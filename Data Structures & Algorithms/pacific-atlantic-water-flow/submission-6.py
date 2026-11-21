class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        visited = set()
        alt = set()
        pac = set()

        n = len(heights)
        m = len(heights[0])

        def dfs(i, j):
            if (i, j) in visited:
                return 
            if i < 0 or i >= n or j < 0 or j >= m:
                return

            visited.add((i, j))

            if i == 0 or j == 0:
                pac.add((i, j))
            if i == n - 1 or j == m - 1:
                alt.add((i, j))

            if i > 0 and heights[i][j] >= heights[i - 1][j]:
                dfs(i - 1, j)
                if (i - 1, j) in alt:
                    alt.add((i, j))
                if (i - 1, j) in pac:
                    pac.add((i, j))

            if i < n - 1 and heights[i][j] >= heights[i + 1][j]:
                dfs(i + 1, j)
                if (i + 1, j) in alt:
                    alt.add((i, j))
                if (i + 1, j) in pac:
                    pac.add((i, j))

            if j < m - 1 and heights[i][j] >= heights[i][j + 1]:
                dfs(i, j + 1)
                if (i, j + 1) in alt:
                    alt.add((i, j))
                if (i, j + 1) in pac:
                    pac.add((i, j))

            if j > 0 and heights[i][j] >= heights[i][j - 1]:
                dfs(i, j - 1)
                if (i, j - 1) in alt:
                    alt.add((i, j))
                if (i, j - 1) in pac:
                    pac.add((i, j))




        for i in range(n):
            for j in range(m):
                dfs(i, j)

                if i != 0 and (i - 1, j) in alt and heights[i -1][j] <= heights[i][j]:
                    alt.add((i, j))
                if i != 0 and (i - 1, j) in pac and heights[i -1][j] <= heights[i][j]:
                    pac.add((i, j))
                if j != 0 and (i, j - 1) in alt and heights[i][j- 1] <= heights[i][j]:
                    alt.add((i, j))
                if j != 0 and (i, j - 1) in pac and heights[i][j- 1] <= heights[i][j]:
                    pac.add((i, j))


        res = []

        for i in range(n):
            for j in range(m):
                if (i, j) in alt and (i, j) in pac:
                    res.append([i, j])

        return res
