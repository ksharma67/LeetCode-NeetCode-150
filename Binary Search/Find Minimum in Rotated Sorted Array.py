class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        start = 0
        end = len(nums) - 1
        if nums[end] > nums[0]:
            return nums[0]
        while end >= start:
            mid = int(start + (end - start) / 2)
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                start = mid + 1
            else:
                end = mid - 1
