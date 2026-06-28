class Solution:
    def trap(self, height: List[int]) -> int:

        res = 0

        n = len(height)

        lMax = height[0]

        Rmax = [ height[n - 1] ]

        for i in range(n - 2, 1, -1):
            if height[i] > Rmax[-1]:
                Rmax.append(height[i])
            else:
                Rmax.append(Rmax[-1])
        print(Rmax)
        for i in range(1, n - 1):
            r = Rmax.pop()
            
            if min(r, lMax) - height[i] > 0:
                res += min(r, lMax) - height[i]
            
            lMax = max(lMax, height[i])
        
        return res
            