class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        M, N = len(s), len(t)
        
        # Dynamic Programming table
        dp = [0 for j in range(N)] 
        
        # Iterate over the strings in reverse so as to
        # satisfy the way we've modeled our recursive solution
        for i in range(M - 1, -1, -1):
            
            # At each step we start with the last value in
            # the row which is always 1. Notice how we are
            # starting the loop from N - 1 instead of N like
            # in the previous solution.
            prev = 1
            
            for j in range(N - 1, -1, -1):
          
                # Record the current value in this cell so that
                # we can use it to calculate the value of dp[j - 1]
                old_dpj = dp[j]
        
                # If the characters match, we add the
                # result of the next recursion call (in this
                # case, the value of a cell in the dp table
                if s[i] == t[j]:
                    dp[j] += prev
                
                # Update the prev variable
                prev = old_dpj    
        
        return dp[0]
