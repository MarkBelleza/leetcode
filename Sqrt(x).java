class Solution {
    public int mySqrt(int x) {
        if (x == 0){
            return 0;
        }

        int l = 1;
        int r = x;
        int mid = 1;
        
        while (l <= r){
            mid = l + ((r - l) / 2); //to avoid integer overflow

            if (mid * mid == x){
                return mid;
            }
            else if((long) mid * mid > (long) x){ //Add long as the number might be too big
                r = mid - 1;
            }
            else{
                l = mid + 1;
            }
        }
        //Once l > r, without returning anything inside the loop, the answer is r
        return r;
    }
}
// Time: O(log(n))
// Space: O(1)
