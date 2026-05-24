class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_set = set()
            col_set = set()
            for j in range(9):
                row = board[i][j]
                col = board[j][i]

                if row in row_set or col in col_set:
                    return False
                if row != '.':
                    row_set.add(row)
                if col != '.':
                    col_set.add(col)

        indexs = [ (0,3), (3, 6), (6,9)]
        count = 0
        for z in range(3):
            for x in range(3):
                i, j = indexs[z]
                k, w = indexs[x]
                le_set = set()
                for s in range(i, j):
                    for y in range(k, w):
                        count += 1
                        ele = board[s][y]
                        if ele in le_set:
                            return False
                        if ele != '.':
                            le_set.add(ele)                        
        return True