class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        val = nums[0]

        for num in nums:
            if abs(num) < abs(val):
                val = num
            elif abs(num) == abs(val) and num > val:
                val = num
    
        return val

        # Time: O(n)
        # Space: O(1)
