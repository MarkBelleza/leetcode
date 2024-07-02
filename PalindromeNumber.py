class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x = str(x)
        # l = 0
        # r = len(x) - 1

        # while l < r:
        #     if x[l] != x[r]:
        #         return False
        #     else:
        #         l += 1
        #         r -= 1
        # return True
        #Time: O(n)
        #Space: O(1)


        #Without converting to string
        if x < 0:
            return False

        reverse = 0
        original = x

        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x //= 10
        
        return reverse == original
        #Time: O(n)
        #Space: O(1)
