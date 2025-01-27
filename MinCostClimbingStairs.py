class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # n = len(cost)
        # min_cost = [0, 0] #since step 1 and 2 is free they cost 0 each
        # for i in range(2, n+1):
        #     next_cost = min(min_cost[i-2] + cost[i-2], 
        #                    min_cost[i-1] + cost[i-1])

        #     min_cost.append(next_cost)
        # return min_cost[n]

        # or (same solution)

        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i-2], dp[i-1]) + cost[i]
        
        return min(dp[-1], dp[-2])
        #DP, bottom up tabulation
        #time: O(n), space: O(n)
    
    


        # n = len(cost)
        # for i in range(n-3, -1, -1):
        #     cost[i] += min(cost[i+1], cost[i+2])
        # return min(cost[0], cost[1])
        #DP, top down tabulation 
        #time: O(n), space: O(1)
