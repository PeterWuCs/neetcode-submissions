class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        visited = set()
        n = len(grid)

        heap = []

        heapq.heappush(heap, ( max(grid[0][1], grid[0][0]), 0, 1))
        heapq.heappush(heap, ( max(grid[1][0], grid[0][0]), 1, 0))
        visited = set()

        while heap:
            weight, i, j = heapq.heappop(heap)
            if (i, j) in visited:
                continue
            if i == n - 1 and j == n - 1:
                return max(weight, grid[i][j])

            visited.add((i, j))
            possible = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for r, c in possible:
                if -1 < i + r < n and -1 < j + c < n:
                    heapq.heappush(heap, (max(weight, grid[i + r][j + c]), i + r, j + c))




        