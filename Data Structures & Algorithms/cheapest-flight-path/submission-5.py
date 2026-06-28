class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        distance = [-1] * n
        distance[src] = 0

        for i in range(k + 1):
            temp = distance.copy()

            for v, u, weight in flights:
                if distance[v] == -1:
                    continue
                elif temp[u] == -1 or temp[u] > distance[v] + weight: 
                    temp[u] = distance[v] + weight   
                    
            distance = temp                

        return distance[dst]