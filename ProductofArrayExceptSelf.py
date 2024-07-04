class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(1, len(nums)): 
            prefix[i] = prefix[i - 1] * nums[i - 1] #before the index
        
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1] #after the index

        return [prefix[i] * suffix[i] for i in range(len(nums))]

        #Time: O(n)
        #Space: O(n)
