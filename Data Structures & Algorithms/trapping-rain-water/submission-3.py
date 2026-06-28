class Solution:
    def trap(self, height: List[int]) -> int:

        res = 0

        n = len(height)
        r, l = n - 2, 1
        rMax = height[n - 1]
        lMax = height[0]

        while l <= r:
            if rMax >= lMax:
                water = lMax - height[l]
                if water > 0:
                    res += water
                lMax = max(lMax, height[l])
                l += 1
            else:
                water = rMax - height[r]
                if water > 0:
                    res += water
                rMax = max(rMax, height[r])
                r -= 1
        return res
            