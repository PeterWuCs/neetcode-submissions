class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)

        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high) // 2
            total = 0
            for i in range(n):
                if piles[i] <= mid:
                    total += 1
                else:
                    if piles[i] % mid == 0:
                        total += (piles[i] // mid)
                    else:
                        total += (piles[i] // mid) + 1
            
            if total <= h:
                high = mid - 1
            else:
                low = mid + 1

        return low


        