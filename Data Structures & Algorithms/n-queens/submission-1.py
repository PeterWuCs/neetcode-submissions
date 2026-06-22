class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        row = [0] * n
        board = [row.copy() for _ in range(n)]

        r_set = set()
        c_set = set()
        d_set = set()
        d2_set = set()


        def checkRight(i, j):
            if i in r_set:
                return False
            if j in c_set:
                return False
            
            if (i - j) in d_set:
                return False
            if (i + j) in d2_set:
                return False

            return True

        def dfs(z):
            if z == n:
                ans = []
                for i in range(n):
                    row = ""
                    for j in range(n):
                        if board[i][j] == 1:
                            row += "Q"
                        else:
                            row += '.'
                    ans.append(row)
                res.append(ans)
                return
            
            for j in range(n):
                if checkRight(z , j):
                    r_set.add(z)
                    c_set.add(j)
                    d_set.add(z - j)
                    d2_set.add(z + j)
                    board[z][j] = 1

                    dfs(z + 1)

                    board[z][j] = 0
                    r_set.remove(z)
                    c_set.remove(j)
                    d_set.remove(z - j)
                    d2_set.remove(z + j)

        dfs(0)
        return res
        