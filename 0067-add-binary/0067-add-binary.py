class Solution(object):
    def addBinary(self, a, b):
        """
        Approach:
            - Simulate grade-school addition from right to left with a carry.
            - Walk indices i, j from the ends of a, b; at each step:
              sum_bit = carry + bit(a[i]) + bit(b[j])
              output bit = sum_bit % 2, new carry = sum_bit // 2
            - Append bits to a list and reverse at the end.

        Why it fits:
            - Works directly on strings without integer conversion, handles very long inputs.
            - Linear time in total length.

        Invariant:
            - After processing position t from the right, the partial result equals
              the exact sum of the last t bits, and 'carry' is the carry into the next higher bit.

        Correctness:
            - Binary addition is associative and local: computing each bit and propagating
              carry yields the unique correct sum.

        Complexity:
            - Time: O(n) where n = max(len(a), len(b))
            - Space: O(n) for the output list (in-place aside from result)
        """
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        out = []

        while i >= 0 or j >= 0 or carry:
            s = carry
            if i >= 0:
                s += ord(a[i]) - 48   # '0' -> 0, '1' -> 1
                i -= 1
            if j >= 0:
                s += ord(b[j]) - 48
                j -= 1
            out.append('1' if (s & 1) else '0')
            carry = s >> 1

        return ''.join(reversed(out))
