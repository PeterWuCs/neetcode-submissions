class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []

        for p in points:
            dis = ((p[0]**2) + (p[1]**2))**(1/2)
            heap.append((dis, p))

        heapq.heapify(heap)
        result = []
        for i in range(k):
            s = heapq.heappop(heap)
            result.append(s[1])

        return result

        