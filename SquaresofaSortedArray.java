class Solution {
    public int[] sortedSquares(int[] nums) {
        int l = 0;
        int r = nums.length - 1;
        int[] res = new int[nums.length];
        
        int i = 0;

        while (l <= r){
            if (Math.abs(nums[l]) < Math.abs(nums[r])){
                res[i] = nums[r] * nums[r];
                i++;
                r--;
            }else{
                res[i] = nums[l] * nums[l];
                i++;
                l++;
            }
        }

        // Need to reverse array

        l = 0;
        r = res.length - 1;

        while(l <= r){
            int temp = res[r];
            res[r] = res[l];
            res[l] = temp;
            l++;
            r--;
        }

        return res;
    }
    // Time: O(n)
    // Space: O(n)
}
