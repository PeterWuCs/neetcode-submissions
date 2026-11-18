class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i in range(len(heights)):
            if not stack or heights[i] >= stack[-1][1]:
                stack.append((i, heights[i]))
                continue
            
            index = -1
            while stack and stack[-1][1] > heights[i]:
                index, h = stack.pop()
                res = max(res, (i - index) * h)

            if stack and stack[-1][1] == heights[i]:
                continue

            stack.append((index, heights[i]))
        
        while stack:
            i, h = stack.pop()
            area = (len(heights) - i) * h
            res = max(res, area)

        return res