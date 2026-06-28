class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(list)

        for flight in flights:
            g[flight[0]].append((flight[1], flight[2]))
        
        heap = [(0, src, 0)]

        
        while heap:
            weight, v, stops = heapq.heappop(heap)

            if v == dst and stops <= k + 1:
                return weight
            
            for u, new_weight in g[v]:
                item = (weight + new_weight, u, stops + 1)
                heapq.heappush(heap, item)

                
        return -1