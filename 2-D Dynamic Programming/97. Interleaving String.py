class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def dfs(i, j, k, s1, s2, s3):
            if(k == len(s3)): 
                return 1
            if((i, j) in d):
                return d[(i, j)]
            x = 0
            if(i < len(s1) and s1[i] == s3[k]):
                x = x or dfs(i+1, j, k+1, s1, s2, s3)
            if(j < len(s2) and s2[j] == s3[k]):
                x = x or dfs(i, j+1, k+1, s1, s2, s3)
            d[(i, j)] = x
            return x
        if(len(s1) + len(s2) != len(s3)):
            return 0
        d = dict()
        return dfs(0, 0, 0, s1, s2, s3)
