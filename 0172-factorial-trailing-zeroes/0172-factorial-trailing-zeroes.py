class Solution(object):
    def trailingZeroes(self, n):
        """
        Approach:
            - Trailing zeros come from pairs of (2,5); 2s are abundant, so count 5s in n!.
            - Sum floor(n/5) + floor(n/25) + floor(n/125) + ... until the quotient is 0.
        Why it fits:
            - Directly targets the limiting factor (5s) without computing factorials.
        Invariant:
            - After each step, 'n' is reduced by a factor of 5; 'ans' equals total 5-exponents counted so far.
        Correctness:
            - Legendre’s formula: v_5(n!) = Σ_{k≥1} ⌊n/5^k⌋ gives the exact count of factor 5s in n!.
            - Each factor 5 paired with a factor 2 yields one trailing zero.
        Complexity:
            - Time: O(log_5 n) iterations
            - Space: O(1)
        """
        ans = 0
        while n > 0:
            n //= 5
            ans += n
        return ans
