class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        res = []

        while l <= r:
            if abs(nums[r]) > abs(nums[l]):
                res.append(nums[r] ** 2)
                r -= 1
            else:
                res.append(nums[l] ** 2)
                l += 1
        
        #Reverse the res list as this is currently in decreasing order
        l = 0
        r = len(nums) - 1
        while l <= r:
            res[l], res[r] = res[r], res[l]
            l += 1
            r -= 1

        return res

        # Time: O(n)
        # Space: O(n)
