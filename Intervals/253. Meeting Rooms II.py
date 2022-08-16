class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        d = defaultdict(lambda: 0)
        for val in intervals:
            d[val[0]] += 1 # one more room is used
            d[val[1]] -= 1 # one less room is used
        ans = 0
        cur = 0
        for key, value in sorted(d.items()): # as time goes
            cur += value # how many rooms are used right now
            ans = max(ans, cur) # get maximum rooms needed
        return ans
