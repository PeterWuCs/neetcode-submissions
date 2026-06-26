class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific = set()
        atlantic = set()
        v = set()

        n = len(heights)
        m = len(heights[0])

        def dfs(i, j, pac):
            if (i, j) in v:
                return
            if pac:
                pacific.add((i, j))
            else:
                atlantic.add((i, j))

            v.add((i, j))

            possible = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for z in range(4):
                u, p = possible[z]
                if -1 < u + i < n and -1 < p + j < m and heights[u + i][p + j] >= heights[i][j]:
                    dfs(u + i, p + j, pac)
        
        for j in range(m):
            dfs(0, j, True)
        for i in range(n):
            dfs(i, 0, True)

        v = set()

        for j in range(m):
            dfs(n - 1, j, False)
        for i in range(n):
            dfs(i, m - 1, False)

        res = []

        for k in pacific:
            if k in atlantic:
                res.append(k)
        return res
        