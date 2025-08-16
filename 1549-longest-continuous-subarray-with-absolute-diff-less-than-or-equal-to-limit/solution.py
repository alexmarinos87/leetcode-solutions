class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        Longest Continuous Subarray With Absolute Diff <= Limit (LeetCode 1438)

        Approach
        --------
        Sliding window with two monotonic deques (O(n)):
        - Keep a window [left, right] and track its minimum and maximum using:
            * min_dq: indices of an increasing sequence of values (front = current min)
            * max_dq: indices of a decreasing sequence of values (front = current max)
        - For each new right:
            * Push it into both deques while maintaining their monotonicity.
            * While max - min > limit, move left forward and pop indices that exit.
        - Update the best window length each step.

        Parameters
        ----------
        nums : List[int]
            Array of integers.
        limit : int
            Maximum allowed difference between any two elements in the subarray.

        Returns
        -------
        int
            Length of the longest valid subarray.
        """
        from collections import deque

        min_dq = deque()  # increasing values
        max_dq = deque()  # decreasing values
        left = 0
        best = 0

        for right, x in enumerate(nums):
            # Maintain min deque
            while min_dq and nums[min_dq[-1]] > x:
                min_dq.pop()
            min_dq.append(right)

            # Maintain max deque
            while max_dq and nums[max_dq[-1]] < x:
                max_dq.pop()
            max_dq.append(right)

            # Shrink window until it's valid
            while nums[max_dq[0]] - nums[min_dq[0]] > limit:
                if min_dq[0] == left:
                    min_dq.popleft()
                if max_dq[0] == left:
                    max_dq.popleft()
                left += 1

            # Update best length
            curr_len = right - left + 1
            if curr_len > best:
                best = curr_len

        return best

