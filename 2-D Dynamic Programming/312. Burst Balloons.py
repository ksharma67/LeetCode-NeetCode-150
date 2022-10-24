class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # special case
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]

        # handle edge case
        nums = [1] + nums + [1]

        @lru_cache(None)  # memoization
        def dp(left, right):
            # maximum if we burst all nums[left]...nums[right], inclusive
            if right - left < 0:
                return 0
            result = 0
            # find the last burst one in nums[left]...nums[right]
            for i in range(left, right + 1):
                # nums[i] is the last burst one
                gain = nums[left - 1] * nums[i] * nums[right + 1]
                # nums[i] is fixed, recursively call left side and right side
                remaining = dp(left, i - 1) + dp(i + 1, right)
                # update the result
                result = max(result, remaining + gain)
            return result

        # we can not burst the first one and the last one
        # since they are both fake balloons added by ourselves
        return dp(1, len(nums) - 2)
