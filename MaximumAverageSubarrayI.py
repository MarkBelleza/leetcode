class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = 0
        for i in range(k):
            ans += nums[i]

        curr = ans
        l = 1
        r = k

        while r < len(nums):
            curr = curr - nums[l - 1] + nums[r]
            ans = max(ans, curr)
            l += 1
            r += 1

        return ans / k

        # Time: O(n)
        # Space: O(1)
