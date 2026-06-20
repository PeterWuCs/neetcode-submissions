class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []

        candidates.sort()

        def dfs(i, sum):
            if sum == target:
                res.append(temp[:])
                return
            
            elif len(candidates) <= i or sum > target:
                return
            
            else:
                temp.append(candidates[i])
                dfs(i + 1, sum + candidates[i])
                temp.pop()
                if i < len(candidates) - 1 and candidates[i + 1] == candidates[i]:

                    for j in range(i + 1, len(candidates)):
                        if candidates[j] != candidates[j - 1]:
                            dfs(j, sum)
                            break
                else:
                    dfs(i + 1, sum)
        dfs(0, 0)
        return res
