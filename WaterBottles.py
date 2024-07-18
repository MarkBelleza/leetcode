class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_bottles = numBottles
        ans = numBottles

        while total_bottles >= numExchange:
            ans += total_bottles // numExchange
            total_bottles = (total_bottles // numExchange) + (total_bottles % numExchange)
        return ans

    # Time: O(log(n)) where n is numBottles and base is numExchange (since we are reducing numBottles by a factor of numExhange in each iteration)
    # Space: O(1)
