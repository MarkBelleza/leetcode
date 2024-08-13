class Solution {
    public int findClosestNumber(int[] nums) {
        int val = nums[0];

        for (int num: nums){
            if (Math.abs(num) < Math.abs(val)){
                val = num;
            }
            else if(Math.abs(num) == Math.abs(val) && num > val){
                val = num;
            }
        }
        return val;
    }
    // Time: O(n)
    // Space: O(1)
}
