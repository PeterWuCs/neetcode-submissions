class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:


        dist = [-1] * n
        dist[src] = 0
        for _ in range(k + 1):
            new_dist = dist.copy()

            for u, v, weight in flights:
                if dist[u] != -1 and (new_dist[v] == -1 or dist[u] + weight < new_dist[v]):
                    new_dist[v] = dist[u] + weight
            dist = new_dist

        return dist[dst]
