class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Two pointer solution
        # left = 0
        # max_profit = 0
        # for right in range(left, len(prices)):
        #     profit = prices[right] - prices[left]
        #     if profit > 0 :
        #         max_profit = max(profit, max_profit)
        #     else:
        #         left = right
        # return max_profit
        

        #Or
        low = prices[0]
        max_profit = 0

        for p in prices:
            if low > p:
                low = p

            max_profit = max(p - low, max_profit)
    
        return max_profit
        #Time: O(n)
        #Space: O(1)
