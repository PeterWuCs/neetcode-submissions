class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [- weight for weight in stones]

        heapq.heapify(heap)

        while len(heap) > 1:
            most = - heapq.heappop(heap)
            sec = - heapq.heappop(heap)

            if most > sec:
                heapq.heappush(heap , - (most - sec))

        if len(heap) == 0:
            return 0
        return - heap[0]