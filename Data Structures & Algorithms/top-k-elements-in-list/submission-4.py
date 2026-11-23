class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        bucket = [set() for i in range(len(nums))]

        count_dict = defaultdict(int)

        for num in nums:
            count_dict[num] += 1
            if count_dict[num] == 1:
                bucket[0].add(num)

            else:
                bucket[count_dict[num] - 2].remove(num)
                bucket[count_dict[num] - 1].add(num)
        res = []
        while k != 0:
            count_set = bucket.pop()

            for ele in count_set:
                res.append(ele)
            k -= len(count_set)
        return res

        
