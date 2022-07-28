class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n>=0:
            res = 1
            while(n):
                if n%2:
                    res = res*x
                x = x*x
                n = n//2
            return res
        else:
            return self.myPow(1/x, -1*n)
