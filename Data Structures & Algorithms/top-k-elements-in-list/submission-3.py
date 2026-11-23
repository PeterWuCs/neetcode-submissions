class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_dict = defaultdict(int)
        for num in nums:
            count_dict[num] += 1
        
        heap = []

        for key in count_dict:
            heap.append((-count_dict[key], key))

        heapq.heapify(heap)

        res = []
        for i in range(k):
            _, value = heapq.heappop(heap)
            res.append(value)

        
        return res

