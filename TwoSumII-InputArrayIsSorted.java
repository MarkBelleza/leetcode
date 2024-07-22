class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0;
        int r = numbers.length - 1;

        while (l < r){
            int tar = numbers[l] + numbers[r];
            if(tar == target){
                int[] ans = {l+1, r+1};
                return ans;
            }else if(tar < target){
                l++;
            }else{
                r--;
            }
        }
        int[] ans = {l+1, r+1};
        return ans;
    }
}
// Time: O(n)
// Space: O(1)
