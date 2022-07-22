class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = {}
        for i in s:
            if i in chars:
                chars[i] += 1
            else:
                chars[i] = 1
        for x in t:
            if x in chars:
                chars[x] -= 1
            else:
                return False
        for c in chars:
            if chars[c] != 0:
                return False
        return True
