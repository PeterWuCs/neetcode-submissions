class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2


        n = len(nums1)
        m = len(nums2)

        total = n + m

        half = total // 2

        if len(B) < len(A):
            A, B = B, A
            n, m = m, n

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i > -1 else float("-inf")
            Aright = A[i + 1] if (i + 1) < n else float("inf")
            Bleft = B[j] if j > -1 else float("-inf")
            Bright = B[j + 1] if (j + 1) < m else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


