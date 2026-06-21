class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(numsdd, temp):
            if not numsdd:
                res.append(temp)
                return
            
            for i in range(len(numsdd)):
                cop = numsdd.copy()
                first = cop.pop(i)
                here = temp[:]
                here.append(first)
                dfs(cop, here)

        dfs(nums, [])
        return res