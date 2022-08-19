class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        dp = [0]*len(s)
        dp[0] = 1
        if len(s) >= 2:
            if s[1] != '0':
                dp[1] = 1
            two_digit = int(s[:2])
            if two_digit >= 10 and two_digit <= 26:
                dp[1] += 1
        for i in range(2, len(dp)):
            if s[i] != '0':
                dp[i] = dp[i - 1]
            two_digit = int(s[i-1: i+1])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]
