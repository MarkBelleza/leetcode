class Solution {
    public int maxProfit(int[] prices) {
        int low = prices[0];
        int profit = 0;

        for (int price : prices){
            if (price < low){
                low = price;
            }
            profit = Math.max(price - low, profit);   
        }
        return profit;
        //Time: O(n)
        //Space: O(1)
    }
}
