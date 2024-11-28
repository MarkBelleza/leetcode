class Solution:
    # this will remember previously called function calls
    # @cache
    def fib(self, n: int) -> int:
    #     if n == 0:
    #         return 0
    #     elif n == 1:
    #         return 1
    #     else:
    #         return self.fib(n-2) + self.fib(n-1)

        # Memoization (same solution)
        memo = {0:0, 1:1}

        def f(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = f(n-2) + f(n-1)
                return memo[n]

        return f(n)

        # Time: O(n)
        # Space: O(n)
