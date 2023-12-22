class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0
        for right in range(left, len(prices)):
            profit = prices[right] - prices[left]
            if profit > 0 :
                max_profit = max(profit, max_profit)
            else:
                left = right
        return max_profit
                
