class Solution {
    public int removeElement(int[] nums, int val) {
        int left = 0;
        int count = 0;

        // The idea is we move the non-val to the left
        for (int right = 0; right < nums.length; right++){
            if (nums[right] != val ){
                // switch the left and right
                int temp = nums[right];
                nums[right] = nums[left];
                nums[left] = temp;


                //incriment the count
                count++;
                left++; //this will make sure left will always be at an index that contains val
            }
        }
        return count;
    }
}

// Time: O(n)
// Space: O(1)
