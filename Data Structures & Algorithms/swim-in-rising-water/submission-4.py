class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dist = {}

        dist[(0, 0)] = grid[0][0]
        heap = [(grid[0][0], 0, 0)]

        while heap:
            w, i, j = heapq.heappop(heap)

            if i == n - 1 and j == m - 1:
                break
            if w > dist.get((i, j), float('inf')):
                continue
            
            possible = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for r, c in possible:
                newRow = i + r
                newCol = j + c

                if 0 <= newRow < n and 0 <= newCol < m:
                    weight = max(w, grid[newRow][newCol])
                    if weight < dist.get((newRow, newCol), float('inf')):
                        dist[(newRow, newCol)] = weight
                        heapq.heappush(heap, (weight, newRow, newCol))
    
        return dist[(n-1, m-1)]