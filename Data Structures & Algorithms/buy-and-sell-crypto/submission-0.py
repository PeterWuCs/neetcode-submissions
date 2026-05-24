class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0

        low = max(prices)
        for price in prices:
            if price < low:
                low = price
            
            elif price > low:
                new = price - low
                if max_p < new:
                    max_p = new
        
        return max_p

        