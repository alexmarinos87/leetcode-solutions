class Solution(object):
    def singleNumber(self, nums):
        """
        Approach:
            - Track per-bit counts modulo 3 using two masks:
                * ones:  bits seen 1 mod 3
                * twos:  bits seen 2 mod 3
              For each x, update:
                ones = (ones ^ x) & ~twos
                twos = (twos ^ x) & ~ones
              Do all ops in 32-bit space; result is 'ones'.

        Why it fits:
            - Each bit cycles through states 00->01->10->00 as it appears 0/1/2/3 times.
              The masks encode this finite-state machine in O(1) space.

        Invariant:
            - After processing any prefix, for every bit position b:
              'ones[b]' == count(b) mod 3 == 1, 'twos[b]' == 2, never both set.

        Correctness:
            - Triply occurring bits are cleared (state returns to 00).
              Only bits appearing once remain in 'ones', hence the unique number.

        Complexity:
            - Time: O(n)
            - Space: O(1)
        """
        MASK = 0xFFFFFFFF  # confine to 32 bits
        ones = twos = 0
        for x in nums:
            x &= MASK
            ones = (ones ^ x) & ~twos
            twos = (twos ^ x) & ~ones
            ones &= MASK
            twos &= MASK

        # convert to signed 32-bit
        if ones & (1 << 31):
            return ones - (1 << 32)
        return ones
