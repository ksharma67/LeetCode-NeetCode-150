class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [0,0]
        for start in range(len(s)):
            end = start
            while end < len(s)-1 and s[end+1] == s[start]:
                end += 1
            while start > 0 and end < len(s)-1 and s[start-1] == s[end+1]:
                start -= 1
                end += 1
            if end - start > res[1]- res[0]:
                res = [start,end]
        return s[res[0]:res[1]+1]
