class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # impossible cases
        if k % 2 == 0 or k % 5 == 0:
            return -1

        current = 1 % k
        length = 1

        while current != 0:
            current = (current * 10 + 1) % k
            length += 1

        return length
