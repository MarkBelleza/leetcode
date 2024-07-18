class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int ans = numBottles;

        while (numBottles >= numExchange){
            ans = ans + (numBottles / numExchange);

            int drank = numBottles / numExchange;
            int remainder = numBottles % numExchange;
            numBottles = drank + remainder;
        }
        return ans;
    }
}
// Time: O(log(n)) where n is numBottles and base is numExchange (since we are reducing numBottles by a factor of numExhange in each iteration)
// Space: O(1)
