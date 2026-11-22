class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        dist = {}   
        n = len(heights)
        m = len(heights[0])

        dist[(0, 0)] = 0
        heap = [(0, 0, 0)]

        while heap:
            cur_dist, i, j = heapq.heappop(heap)

            if cur_dist > dist.get((i, j), float('inf')):
                continue
            
            if i > 0:
                weight = max(abs(heights[i][j] - heights[i - 1][j]), cur_dist)
                if weight < dist.get((i - 1, j), float('inf')):
                    dist[(i - 1, j)] = weight
                    heapq.heappush(heap, (weight, i - 1, j))
            if j > 0:
                weight = max(abs(heights[i][j] - heights[i][j - 1]), cur_dist)
                if weight < dist.get((i, j - 1), float('inf')):
                    dist[(i, j - 1)] = weight
                    heapq.heappush(heap, (weight, i, j - 1))

            if i < n - 1:
                weight = max(abs(heights[i][j] - heights[i + 1][j]), cur_dist)
                if weight < dist.get((i + 1, j), float('inf')):
                    dist[(i + 1, j)] = weight
                    heapq.heappush(heap, (weight, i + 1, j))

            if j < m - 1:
                weight = max(abs(heights[i][j] - heights[i][j + 1]), cur_dist)
                if weight < dist.get((i, j + 1), float('inf')):
                    dist[(i, j + 1)] = weight
                    heapq.heappush(heap, (weight, i, j + 1))

        return dist[(n - 1, m - 1)]

