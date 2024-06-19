class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        # Binary search based on the condition: 
        # if (mid * mid < x and (mid + 1) * (mid + 1) > x) or mid * mid == x, then the answer is mid

        left = 1
        right = x

        while left <= right:
            mid = (left + right) // 2

            if mid * mid > x: #mid is too big, need to check the left side
                right = mid - 1
            elif (mid * mid < x and (mid + 1) * (mid + 1) > x) or mid * mid == x:
                return mid
            else:
                left = mid + 1

        #Time: O(log(x))
        #Space: O(1)
