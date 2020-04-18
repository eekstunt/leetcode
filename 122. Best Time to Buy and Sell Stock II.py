# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i] - prices[i-1] > 0:
                max_profit += prices[i] - prices[i-1]
        return max_profit
