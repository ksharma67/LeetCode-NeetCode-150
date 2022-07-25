class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_pos = len(nums) - 1
		
        for i in range(last_pos,-1,-1):
            if i+nums[i]>=last_pos:
                last_pos = i
				
        return last_pos == 0
