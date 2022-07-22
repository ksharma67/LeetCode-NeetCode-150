class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        return self.climb(0, n, cache)
    
    def climb(self, currentSteps, n, cache):
        if currentSteps == n:
            return 1
        if currentSteps > n:
            return 0
        if currentSteps in cache:
            return cache[currentSteps]
        
        total = 0
        # 1 step
        total += self.climb(currentSteps + 1, n, cache)
        # 2 steps
        total += self.climb(currentSteps + 2, n, cache)
        
        cache[currentSteps] = total
        return total
    
    
 
class Solution:
    def climbStairs(self, n: int) -> int:
        current = 1
        previous = 1
        while (n>0):
            current, previous = current+previous, current
            n-=1
        return previous
