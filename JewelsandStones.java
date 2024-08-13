class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        Set<Character> j = new HashSet<Character>();
        int count = 0;

        for (char i: jewels.toCharArray()){
            j.add(i);
        }

        for (char i: stones.toCharArray()){
            if (j.contains(i)){
                count++;
            }
        }

        return count;

    }
    // Time: O(n+m), n and m are the length of jewels and stones respectively
    // Space: O(n)
}
