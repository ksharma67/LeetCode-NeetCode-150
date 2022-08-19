class Solution:
    def reverseBits(self, n: int) -> int:
        i = 0
        new = 0
        while n >> i:
            if (n >> i) & 1:
                new |= 1 << (31-i);
            i += 1;
        return new;
