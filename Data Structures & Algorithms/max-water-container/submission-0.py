class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        max = 0
        while i < j:
            if min(heights[i], heights[j]) * (j - i) > max:
                max =  min(heights[i], heights[j]) * (j - i)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return max