class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #Move all the non val to the left
        l = 0
        count = 0
        for r, num in enumerate(nums):
            if num != val:
                nums[l], nums[r] = nums[r], nums[l] #This and line below will ensure l is always at an index that contains val
                l += 1
                count += 1
        return count

        #Time: O(n)
        #Space: O(1)

