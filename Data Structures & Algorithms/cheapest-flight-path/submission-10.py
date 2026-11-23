class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)
        for u, v, wei in flights:
            graph[u].append((wei, v))

        dist = {}
        dist[(src, 0)] = 0
        heap = [(0, src, 0)]

        while heap:
            w, node, stops = heapq.heappop(heap)

            if node == dst:
                return w

            if stops > k:
                continue
            if w > dist.get((node, stops), float('inf')):
                continue

            for edge_weight, nei in graph[node]:
                if w + edge_weight < dist.get((nei, stops + 1), float('inf')):
                    dist[(nei, stops + 1)] = w + edge_weight
                    heapq.heappush(heap, (dist[nei, stops + 1], nei, stops + 1))

        
        return -1
