class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        pq = []
        visited = set()
        visited.add((points[0][0], points[0][1]))
        def get_dis(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


        for i in range(1, len(points)):
            dis = get_dis(points[0], points[i])
            heapq.heappush(pq, (dis, (points[i][0], points[i][1])))

        n = len(points)
        count = 0
        ans = 0
        while count != n - 1:
            w, new_p = heapq.heappop(pq)
            
            if new_p not in visited:
                ans += w
                visited.add(new_p)
                count += 1

                for i in range(len(points)):
                    p = (points[i][0], points[i][1])
                    if p not in visited:
                        dis = get_dis(new_p, points[i])
                        heapq.heappush(pq, (dis, p))
        return ans
