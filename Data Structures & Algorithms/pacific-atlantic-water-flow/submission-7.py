class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        visited = set()
        alt = set()
        pac = set()

        n = len(heights)
        m = len(heights[0])

        for i in range(n):
            pac.add((i, 0))
            alt.add((i, m - 1))

        for j in range(m):
            pac.add((0, j))
            alt.add((n - 1, j))

        def dfs(i, j, which):
            if ((i, j)) in visited or i < 0 or j < 0 or j >= m or i >= n:
                return
            visited.add((i, j))
            if i > 0 and heights[i][j] <= heights[i - 1][j]:
                which.add((i - 1, j))
                dfs(i - 1, j, which)

            if i < n - 1 and heights[i][j] <= heights[i + 1][j]:
                which.add((i + 1, j))
                dfs(i + 1, j, which)

            if j > 0 and heights[i][j] <= heights[i][j - 1]:
                which.add((i, j - 1))
                dfs(i , j - 1, which)

            if j < m - 1 and heights[i][j] <= heights[i][j + 1]:
                which.add((i, j + 1))
                dfs(i, j + 1, which)

        for i in range(n):
            for j in range(m):
                if (i, j) in alt:
                    dfs(i, j, alt)
        visited = set()
        for i in range(n):
            for j in range(m):
                if (i, j) in pac:
                    dfs(i, j, pac)


        res = []
        for i in range(n):
            for j in range(m):
                if (i, j) in pac and (i, j) in alt:
                    res.append([i, j])


        return res
