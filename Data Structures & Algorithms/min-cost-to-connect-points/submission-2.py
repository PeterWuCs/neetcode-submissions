class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def dist(xi, yi, xj, yj):
            return abs(xi - xj) + abs(yi - yj)

        graph = defaultdict(list)
        for i in range(len(points)):
            xi = points[i][0]
            yi = points[i][1]
            for j in range(i + 1, len(points)):
                xj = points[j][0]
                yj = points[j][1]

                weight = dist(xi, yi, xj, yj)

                graph[(xi, yi)].append((weight, xj, yj))
                graph[(xj, yj)].append((weight, xi, yi))

        heap = [(0, points[0][0], points[0][1])]
        mst = 0
        added = set()

        while heap and len(added) != len(points):
            w, x, y = heapq.heappop(heap)
            if (x, y) not in added:
                added.add((x, y))
                mst += w
                for weight, nebX, nebY in graph[(x, y)]:
                    heapq.heappush(heap, (weight, nebX, nebY))

        return mst