class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if '-' in s:
            s=s.replace('-','')
            a = int('-'+s[::-1])
            if a in range(-(2**31),(2**31)-1):
                return a
            else:
                return 0
        else:
            b = int(s[::-1])
            if b in range(-(2**31),(2**31)-1):
                return b
            else:
                return 0
