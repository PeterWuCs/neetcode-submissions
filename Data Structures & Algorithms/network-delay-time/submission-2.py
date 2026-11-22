class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        dist = [float('inf') for _ in range(n)]
        
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))
        
        dist[k - 1] = 0
        heap = [(0, k)]

        while heap:
            weight, node = heapq.heappop(heap)

            if weight > dist[node - 1]:
                continue

            for v, w in graph[node]:
                if weight + w < dist[v - 1]:
                    dist[v - 1] = weight + w 
                    heapq.heappush(heap, (dist[v - 1], v))

        res = dist[0]
        for num in dist:
            if num == float('inf'):
                return -1
            res = max(res, num)


        return res