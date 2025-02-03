class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        # for i in range (len(nums)):
        #     complement = target - nums[i]
        #     if complement in dic:
        #         return [dic[complement], i]
        #     else:
        #         dic[nums[i]] = i

        for i, num in enumerate(nums):
            complement = target - num
            if complement in dic:
                return [dic[complement], i]
            else:
                dic[num] = i
        #Time: O(n)
        #Space: O(n)

        #Slower but less memory
        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     for j in range(len(nums)):
        #         if j != i and nums[j] == complement:
        #             return [i, j]
        #Time: O(n^2)
        #Space: O(1)
