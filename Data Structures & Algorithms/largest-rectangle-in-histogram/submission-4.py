class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        res = 0

        for i, height in enumerate(heights):
            if not stack:
                stack.append((height, i))
                continue

            h, j = stack.pop()

            if height > h:
                stack.append((h, j))
                stack.append((height, i))

            elif height < h:
                res = max(res, (i - j) * h)

                while stack and stack[-1][0] > height:
                    h, j = stack.pop()
                    res = max(res, (i - j) * h)
                stack.append((height, j))

            else:
                stack.append((h, j))

        n = len(heights)

        while stack:
            h, j = stack.pop()
            res = max(res, (n - j) * h)

        return res


