class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
            
        dig_map = { 2: ['a', 'b', 'c'], 
                    3: ['d', 'e', 'f'],
                    4: ['g', 'h', 'i'],
                    5: ['j', 'k', 'l'],
                    6: ['m', 'n', 'o'],
                    7: ['p', 'q', 'r', 's'],
                    8: ['t', 'u', 'v'],
                    9: ['w', 'x', 'y', 'z']}

        res = []

        temp = []

        def dfs(i):
            if i >= len(digits):
                res.append(temp.copy())
                return
            
            for j in range(len(dig_map[int(digits[i])])):
                temp.append(dig_map[int(digits[i])][j])
                dfs(i + 1)
                temp.pop()
        
        dfs(0)
        ans = []

        for i in range(len(res)):
            ans.append("".join(res[i]))

        return ans
