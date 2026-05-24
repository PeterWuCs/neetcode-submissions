class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix) -1 , len(matrix[0]) - 1

        if n == -1:
            return False

        low, high = 0, m
        mid = (low + high) // 2

        while low <= high:
            if (target >= matrix[mid][0] and target<= matrix[mid][-1]):
                break
            if target < matrix[mid][0]:
                high = mid - 1
                mid = (low + high) // 2
            else:
                low = mid + 1
                mid = (low + high) // 2

        print(mid)

        low, high = 0, n
        while low <= high:
            mid2 = (low + high) //2
            
            if matrix[mid][mid2] == target:
                return True
            elif target < matrix[mid][mid2]:
                high = mid2 -1
            else:
                low = mid2 + 1
            
        return False