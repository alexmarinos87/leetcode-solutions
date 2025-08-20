class Solution(object):
    def isHappy(self, n):
        """
        Approach: Repeatedly replace n with sum of squares of digits.
                  Use Floyd's cycle detection: slow=f(n), fast=f(f(n)).
                  If we ever reach 1, it's happy; if slow==fast (≠1), there's a loop.

        Complexity: Each step costs O(#digits) ≈ O(log n).
                    The sequence quickly falls below 1000, so steps are small in practice.
        """
        def sumsq(x):
            s = 0
            while x:
                x, d = divmod(x, 10)
                s += d * d
            return s

        slow = sumsq(n)
        fast = sumsq(sumsq(n))
        while slow != fast:
            if fast == 1 or sumsq(fast) == 1:  # hare is two steps ahead; quick exit if it hits 1
                return True
            slow = sumsq(slow)
            fast = sumsq(sumsq(fast))
        return slow == 1
