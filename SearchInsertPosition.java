class Solution {
    public int searchInsert(int[] nums, int target) {
        if (nums[0] > target){
            return 0;
        }else if(nums[nums.length-1] < target){
            return nums.length;
        }

        // Perform binary search
        int l = 0;
        int r = nums.length - 1;

        while (l <= r){
            int m = l + ((r - l) / 2); //consider overflow

            if (nums[m] == target){
                return m;
            }else if (nums[m] < target && nums[m+1] > target){
                return m+1;
            }else if (nums[m] > target){
                r = m - 1;
            }else {
                l = m + 1;
            }
        }
        return -1; //I don't think this part matters, the code above should find the actual answer
    }
}

// Time: O(log n)
// Space: O(1)
