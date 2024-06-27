class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r, num in enumerate(nums):
            if num != 0:
                nums[l], nums[r] = nums[r], nums[l] #swap the elements in index l and r
                l += 1 #this ensures that l is always at an element that is 0 (this happens the first time you swap, by then l will always be at a 0 element)

        # The idea is that you move non-zeros to the left
        # There will never be a point where there is a non-zero between at index l and r (ie.[0/l, 1, 2, 4/r] <-- will NOT happen)
    
        #Time: O(n)
        #Space: O(1)
