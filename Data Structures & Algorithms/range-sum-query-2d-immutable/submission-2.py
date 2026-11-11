class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.weight_dict = {}
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            row_sum = 0
            for j in range(m):
                key = (i, j)
                row_sum += matrix[i][j]
                
                sum = row_sum

                if i != 0:
                    sum += self.weight_dict[(i - 1, j)]
                
                self.weight_dict[(i, j)] = sum


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        res = self.weight_dict[(row2, col2)]

        if row1 > 0:
            res -= self.weight_dict[(row1 - 1, col2)]

        if col1 > 0:
            res -= self.weight_dict[(row2, col1 - 1)]

        if row1 > 0 and col1 > 0:
            res += self.weight_dict[(row1 - 1, col1 - 1)]

        return res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)