from heapq import heappush , heapify , heappop
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_ = [] 
        heapify(max_)
        ans = []
        for i in range(k) :
            heappush(max_ , [-nums[i] , i])
            
        ans.append(-max_[0][0])
        start = 0
        end = k
        while end < len(nums) :
            while max_ and max_[0][1] <= start :
                heappop(max_)
            
            heappush(max_ , [-nums[end] , end])
            
            ans.append(-max_[0][0])
            start += 1
            end += 1
            
        return ans
            
