class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        dp = [[-1]*len(s) for _ in range(len(s))]
        for g in range(len(s)):
            for i,j in zip(range(0,len(dp)),range(g,len(dp))):
                if g==0:
                    dp[i][j] = True
                elif g==1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                    else:
                        dp[i][j] = False
                else:
                    if s[i] == s[j] and dp[i+1][j-1]==True:
                        dp[i][j] = True
                    else:
                        dp[i][j] = False
                if dp[i][j]:
                    count+=1
        return count
