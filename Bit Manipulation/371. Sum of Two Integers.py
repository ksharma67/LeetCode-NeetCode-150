class Solution:
    def getSum(self, a: int, b: int) -> int:
        return int(math.log2(2**a * 2**b))
