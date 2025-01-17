class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums)-2, -1, -1): #(start, end, jump)
            if nums[i] + i >= goal:
                goal = i
        
        return goal == 0

    #Time: O(nums)
    #Space: O(1)
