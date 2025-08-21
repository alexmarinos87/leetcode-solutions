class Solution(object):
    def myPow(self, x, n):
        """
        Approach:
            - Handle trivial cases: n == 0 → 1.0; x == 0 → 0.0 (for n > 0).
            - For negative n, invert base: x = 1/x; n = -n.
            - Use iterative binary exponentiation:
                res = 1; while n > 0:
                  if n is odd: res *= x
                  x *= x; n //= 2
        Why it fits:
            - Exponentiation by squaring cuts the exponent in half each step.
            - Avoids recursion depth; purely integer ops on n; stable for floats.
        Invariant:
            - res * (x ** n_remaining) == original x ** n_abs at every iteration.
        Correctness:
            - Binary decomposition of n ensures each bit’s contribution is multiplied once.
            - For negative n, result is (x^{-n})^{-1}.
        Complexity:
            - Time: O(log |n|)
            - Space: O(1)
        """
        if n == 0:
            return 1.0
        if x == 0.0:
            return 0.0  # valid when n > 0 per constraints

        neg = n < 0
        n = -n if neg else n

        res, base = 1.0, float(x)
        while n:
            if n & 1:
                res *= base
            base *= base
            n >>= 1
        return 1.0 / res if neg else res

