from typing import List



class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        index_0, index_1 = cost[0], cost[1]
        num_ladder = len(cost)
        dp = [0] * (num_ladder)
        dp[0] = index_0
        dp[1] = index_1
        for i in range(2, num_ladder):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return min(dp[num_ladder-1],dp[num_ladder-2])
s = Solution()
print(s.minCostClimbingStairs([10,15,20]))

