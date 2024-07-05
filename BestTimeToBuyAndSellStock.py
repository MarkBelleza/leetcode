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
        profit = 0
        buy = prices[0]

        for price in prices:
            if price < buy: #if current price is lower than previous buy, then buy this one
                buy = price
            else: #if current price is higher than previous buy, then sell
                profit = max(price - buy, profit)
        return profit
        #Time: O(n)
        #Space: O(1)
