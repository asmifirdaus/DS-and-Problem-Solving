#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        price=float('inf')
        for i in range(len(prices)):
            price=min(price,prices[i])
            profit=max(profit,prices[i]-price)
        return profit
        
