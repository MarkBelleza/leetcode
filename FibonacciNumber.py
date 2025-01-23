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

        # Note: Without memoization Time is O(n^2). 
        # This is because without memoization, the function makes redundant recursive calls for the same inputs. For example, fib(n-1) and fib(n-2) will independently calculate overlapping subproblems.
