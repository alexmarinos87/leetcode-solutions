class Solution(object):
    def isHappy(self, n):
        """
        Happy Number (LeetCode 202)

        Approach
        --------
        Floyd's cycle detection (O(log n) per transform, O(1) extra space):
        - Define f(x) = sum of squares of digits of x.
        - A number is happy iff repeated application of f enters the cycle at 1.
        - Use two iterates: slow = f(slow), fast = f(f(fast)).
        - If they meet at 1 → happy; if they meet elsewhere → loop → not happy.

        Parameters
        ----------
        n : int
            Positive integer to test.

        Returns
        -------
        bool
            True if n is a happy number; False otherwise.
        """
        def sqsum(x):
            s = 0
            while x:
                x, d = divmod(x, 10)
                s += d * d
            return s

        slow = n
        fast = sqsum(n)
        while fast != 1 and slow != fast:
            slow = sqsum(slow)
            fast = sqsum(sqsum(fast))

        return fast == 1

        # --- Alternative (simpler, uses O(k) space) ---
        # seen = set()
        # while n != 1 and n not in seen:
        #     seen.add(n)
        #     n = sqsum(n)
        # return n == 1

