class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        longest = 0
        for n in nums:
            if n-1 not in num_set:
                length = 0
                while n in num_set:
                    length += 1
                    n += 1
                longest = max(longest, length) 
        return longest
