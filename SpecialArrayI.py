class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        def parity(num):
            if num % 2 != 0:
                return 'odd'
            else:
                return 'even' 

        if len(nums) == 1:
            return True
        for i in range(len(nums) - 1):
            if parity(nums[i]) == parity(nums[i + 1]):
                return False
        return True
