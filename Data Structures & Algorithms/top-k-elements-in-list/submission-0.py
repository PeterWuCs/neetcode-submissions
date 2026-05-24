class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {
        }

        for num in nums:
            if count_dict.get(num):
                count_dict[num] += 1
            else:
                count_dict[num] = 1

        sortsd = sorted(count_dict.items(), key=lambda x:x[1], reverse=True)

        answer = []
        for i in range(k):
            answer.append(sortsd[i][0])
            

        return answer