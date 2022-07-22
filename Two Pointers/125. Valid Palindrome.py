class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = ''
        for i in s:
            if i.isalnum():
                i = i.lower()
                lower += i
        rev = lower[::-1]
        return True if rev == lower else False
