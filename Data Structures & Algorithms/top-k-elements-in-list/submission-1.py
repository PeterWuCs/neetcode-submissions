class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {
        }

        for num in nums:
            if count_dict.get(num):
                count_dict[num] += 1
            else:
                count_dict[num] = 1

        bucket = [ [] for i in range(len(nums)+ 1)] 
        
        for n, f in count_dict.items():

            bucket[f].append(n)
        
        answer = []

        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                answer.extend(bucket[i])
            if len(answer) == k:
                return answer
        return answer