class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_max = 0
        
        for i in nums:
            current_max = max(current_max + i, i)
            max_sum = max(current_max, max_sum)
        
        return max_sum
    
    #Time: O(n), Space: O(1)
