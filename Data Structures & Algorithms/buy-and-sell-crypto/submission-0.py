class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0

        l, r = 0, 1
        
        # some condition, while r in range
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            elif prices[l] < prices[r]:
                max_profit = max(prices[r]-prices[l], max_profit)
            r += 1
        return max_profit


        
