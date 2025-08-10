class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        Minimum Size Subarray Sum (LeetCode 209)

        Approach
        --------
        Sliding Window (O(n)):
        - Maintain a moving window [left, right] and its sum.
        - Expand right to increase the sum until it reaches/exceeds target.
        - Then shrink left as much as possible while keeping sum >= target,
          updating the best (shortest) length along the way.
        - Works because all numbers are positive, so expanding increases sum
          and contracting decreases sum monotonically.

        Parameters
        ----------
        target : int
            Positive target sum to reach or exceed.
        nums : List[int]
            Array of positive integers.

        Returns
        -------
        int
            The minimal length of a subarray with sum >= target; 0 if none exists.
        """
        left = 0
        window_sum = 0
        best = float('inf')

        for right, x in enumerate(nums):
            window_sum += x
            while window_sum >= target:
                best = min(best, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return 0 if best == float('inf') else best
