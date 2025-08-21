class Solution(object):
    def plusOne(self, digits):
        """
        Approach:
            - Start from the least significant digit and add 1.
            - If digit becomes 10, set it to 0 and propagate carry left.
            - If carry exists after the most significant digit, prepend 1.
        Why it fits:
            - Simulates addition the same way humans do on paper.
            - Avoids converting to int, works with arbitrarily large numbers.
        Invariant:
            - All digits are in [0,9]; any overflow turns to 0 and carries left.
        Correctness:
            - The algorithm mirrors elementary school addition.
            - Handles carry correctly even for inputs like [9,9,9].
        Complexity:
            - Time: O(n)
            - Space: O(1) extra (in-place, except when prepending due to carry)
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits

