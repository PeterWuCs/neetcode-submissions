class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distance = [-1] * n
        distance[k - 1] = 0

        pq = [(0, k)]

        g = defaultdict(list)
        relaxed = set()

        for i in range(len(times)):
            g[times[i][0]].append((times[i][2], times[i][1]))
        
        while pq:
            weight, u = heapq.heappop(pq)
            if u in relaxed:
                continue
            relaxed.add((u))

            for new_weight, v in g[u]:
                if distance[v - 1] == -1 or new_weight + weight < distance[v - 1]:
                    distance[v - 1] = new_weight + weight
                heapq.heappush(pq, (distance[v - 1], v))

        print(distance)

        ans = distance[0]
        for num in distance:
            if num == -1:
                return -1
            else:
                ans = max(num, ans)

        return ans