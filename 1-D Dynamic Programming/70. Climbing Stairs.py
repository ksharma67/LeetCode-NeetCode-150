class Solution:
    def climbStairs(self, n: int) -> int:
        current = 1
        previous = 1
        while (n>0):
            current, previous = current+previous, current
            n-=1
        return previous
