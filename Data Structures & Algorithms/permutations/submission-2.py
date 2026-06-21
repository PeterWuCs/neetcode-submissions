class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            new_res = []
            for prem in res:
                for i in range(len(prem) + 1):
                    cop = prem.copy()
                    cop.insert(i, num)
                    new_res.append(cop)

            res = new_res

        return res