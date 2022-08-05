class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
                
        prev = float("-inf")
        res = 0
        
        for interval in intervals:
            if interval[0] >= prev:
                prev = interval[1]
            else:
                res += 1
                prev = min(interval[1], prev)
                
        return res
