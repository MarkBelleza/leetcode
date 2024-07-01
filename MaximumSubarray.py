class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_max = nums[0]
        
        for num in nums[1:]:
            current_max = max(current_max + num, num)
            max_sum = max(current_max, max_sum)
        
        return max_sum
    
    #Time: O(n), Space: O(1)
