class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # P - N = target  P+ N = sum --> 2P = target + sum --> P = (target+sum)/2  
        total_sum = sum(nums)
        if (total_sum + target) % 2 != 0 or target > total_sum or target < -total_sum:
            return 0
        m = len(nums)
        n = (total_sum + target) // 2
        dp = [[0] * (n + 2) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1

        dp[0][1] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 2):
                if j - 1 >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[m][n + 1]
