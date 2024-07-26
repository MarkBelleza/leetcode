class Solution {
    public void reverseString(char[] s) {
        int r = s.length - 1;
        int l = 0;
        while (l < r){
            char temp = s[r];
            s[r] = s[l];
            s[l] = temp;
            l++;
            r--;
        }
    }
}
// Time: O(n)
// Space: O(1) as required in the question
