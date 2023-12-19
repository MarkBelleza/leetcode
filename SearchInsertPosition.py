class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0] > target:
            return 0
        elif nums[-1] < target:
            return len(nums)

        #binary search
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            elif nums[mid] < target and nums[mid + 1] > target:
                return mid + 1
            elif target < nums[mid]: 
                end = mid - 1 #check the left side of the list
            else:
                start = mid + 1 #check the right side of the list
