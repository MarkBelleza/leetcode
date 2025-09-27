class Solution {
    public int maxNumberOfBalloons(String text) {
        Map<Character, Integer> b = new HashMap<>();
        char[] x = {'b', 'a', 'l', 'o', 'n'};
        for (char i : x){
            b.put(i, 0);
        }

        for (char i : text.toCharArray()){
            if (b.containsKey(i)){
                int val = b.get(i);
                b.put(i, val + 1);
            }
        }

        int l = b.get('b');
        int m = b.get('a');
        int n = b.get('l') / 2;
        int o = b.get('o') / 2;
        int p = b.get('n');

        return Math.min(Math.min(Math.min(l, m), Math.min(n, o)), p);
        // Time: O(n)
        // Space: O(1)
    }
}
