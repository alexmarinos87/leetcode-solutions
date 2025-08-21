class Solution(object):
    def mySqrt(self, x):
        """
        Approach:
            - Handle small cases x < 2 directly (answer is x).
            - Binary search the largest m with m*m <= x.
              Search space: [1, x//2] since sqrt(x) <= x//2 for x >= 2.
        Why it fits:
            - Monotonic predicate m*m <= x lets us use binary search.
            - No floats, no pow; safe in Python for very large x.
        Invariant:
            - At every step, 'ans' is the best known m with m*m <= x.
            - Search interval [lo, hi] always contains ⌊√x⌋.
        Correctness:
            - Binary search over a monotone condition finds the maximal m
              satisfying m*m <= x, which equals ⌊√x⌋ by definition.
        Complexity:
            - Time: O(log x) iterations
            - Space: O(1)
        """
        if x < 2:
            return x

        lo, hi = 1, x // 2
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            sq = mid * mid
            if sq == x:
                return mid
            if sq < x:
                ans = mid       # mid is feasible
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
