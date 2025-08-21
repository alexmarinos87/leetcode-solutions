class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        Approach:
            - Find the common binary prefix of left and right by right-shifting both
              until they become equal; count how many shifts we did (say 'shift').
            - All differing lower bits must turn to 0 across the range.
            - Answer is the common prefix shifted back: left << shift.

        Why it fits:
            - Any bit that flips within [left, right] gets ANDed with both 0 and 1,
              ending as 0. Only the stable high-prefix bits survive.

        Invariant:
            - After t shifts, 'left' and 'right' share all remaining bits (higher),
              and differ only in the t lower bits we removed.

        Correctness:
            - The loop stops when left == right, which is the common prefix.
              Lower 'shift' bits must be 0 in the AND, so shifting back restores
              the shared prefix with zeros below.

        Complexity:
            - Time: O(32) (at most 32 shifts for 32-bit numbers)
            - Space: O(1)
        """
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift
