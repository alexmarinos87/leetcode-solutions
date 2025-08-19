class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        Approach: Expand right to grow sum; while sum >= target, shrink left and record best length.
        Why it fits: Positives make the window sum monotone—expanding increases, shrinking decreases.
        Invariants: left <= right; total = sum(nums[left:right+1]); best is minimal length seen so far.
        Correctness: Every valid window is examined and shrunk to minimal size before moving on.
        Complexity: Time O(n), Space O(1).
        """
        left = 0
        total = 0
        best = float('inf')

        for right, x in enumerate(nums):
            total += x
            while total >= target:
                best = min(best, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if best == float('inf') else best