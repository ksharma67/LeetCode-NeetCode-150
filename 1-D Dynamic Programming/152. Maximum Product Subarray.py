class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxSubarr = nums[0]
        curPositiveSubarr = nums[0]
        curNegativeSubarr = nums[0]
        
        for i in range(1, len(nums)):
            n = nums[i]
            t = curPositiveSubarr
            curPositiveSubarr = max(n, curPositiveSubarr * n, curNegativeSubarr * n)
            curNegativeSubarr = min(n, curNegativeSubarr * n, t * n)
            maxSubarr = max(maxSubarr, curPositiveSubarr, curNegativeSubarr)
        return maxSubarr
