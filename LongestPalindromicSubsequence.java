class Solution {
    public int longestPalindromeSubseq(String s) {
        // Let's implement the dynamic programming way using a 2D array (tabulation bottom up)
        int n = s.length();
        int[][] table = new int[n][n];

        // Fill the diagonal of the table with 1
        for (int i = 0; i < n; i++){
            table[i][i] = 1;
        }

        //Fill the upper side of the diagonal
        for (int size = 2; size <= n; size++){
            for(int i = 0; i < n - size+1; i++){

                int j = i + size-1;
                if (s.charAt(i) == s.charAt(j) && size == 2){
                    table[i][j] = 2;
                }
                else if (s.charAt(i) == s.charAt(j)){
                    table[i][j] = table[i+1][j-1] + 2;
                }
                else{
                    table[i][j] = Math.max(table[i][j-1], table[i+1][j]);
                }
            }
        }

        return table[0][n-1];
    }
}

// Time: O(n^2)
// Space: O(n^2)
