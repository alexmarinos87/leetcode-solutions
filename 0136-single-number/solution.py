class Solution(object):
    def singleNumber(self, nums):
        """
        Approach:
            - XOR all numbers: pairs cancel (a ^ a = 0), and 0 ^ x = x.
            - The final accumulator is the unique number.

        Why it fits:
            - Exactly-two duplicates guarantee pairwise cancellation via XOR.
            - Requires only a single pass and constant space.

        Invariant:
            - After processing the first t elements, 'acc' equals the XOR of those t numbers.
              Since duplicates cancel, 'acc' always equals the XOR of numbers with odd frequency
              among the first t items.

        Correctness:
            - Because every duplicate occurs twice, all duplicates vanish in the XOR.
              Only the single element (frequency 1) remains.

        Complexity:
            - Time: O(n)  (one pass)
            - Space: O(1)
        """
        acc = 0
        for x in nums:
            acc ^= x
        return acc

