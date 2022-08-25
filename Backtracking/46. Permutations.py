class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def solve_permute(i):
            if i == len(nums) - 1:
                R.append(nums[::])
            
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                solve_permute(i + 1)
                nums[i], nums[j] = nums[j], nums[i]
        
        R = []
        solve_permute(0)
        return R
