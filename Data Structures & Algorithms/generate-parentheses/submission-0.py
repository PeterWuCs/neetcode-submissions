class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []

        def dfs(l, r, temp):
            if r == l == n:
                result.append(temp)
                return 
            
            if l == r:
                temp = temp + "("
                dfs(l + 1, r, temp)
                return

            if l == n:
                temp = temp + ")"
                dfs(l, r + 1, temp)
                return

            temp1 = temp + "("
            dfs(l + 1, r, temp1)
            temp2 = temp + ")"
            dfs(l, r + 1, temp2)
            
        dfs(0, 0, "")
        return result