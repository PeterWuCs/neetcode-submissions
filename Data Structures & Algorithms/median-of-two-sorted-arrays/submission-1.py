class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        n, m = len(A), len(B)

        if n > m:
            A, B = B, A
            n, m = m, n

        low, high = 0, n
        half = (n + m + 1) // 2

        while low <= high:
            i = (low + high) // 2
            j = half - i

            AL = A[i - 1] if i > 0 else float('-inf')
            AR = A[i] if i < n else float('inf')
            BL = B[j - 1] if j > 0 else float('-inf')
            BR = B[j] if j < m else float('inf')

            if AL <= BR and BL <= AR:
                if (n + m) % 2 == 1:
                    return max(AL, BL)
                return (max(AL, BL) + min(AR, BR)) / 2

            elif AL > BR:
                high = i - 1
            else:
                low = i + 1