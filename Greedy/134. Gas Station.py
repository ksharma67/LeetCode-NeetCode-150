class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        extra,ans = 0,0
        for i in range(len(gas)):
            extra += gas[i]-cost[i]
            if extra<0:
                ans = i+1
                extra = 0
        return ans
