class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        Contains Duplicate II (LeetCode 219)

        Approach
        --------
        Sliding window with a hash set (O(n)):
        - Keep a set of the last at most `k` elements.
        - For each num:
          * If it's already in the set, we've found two equal values within distance k.
          * Insert it; if the window grows beyond k, remove the element k positions back.
        - Works because the set mirrors a window of indices [i-k, i-1].

        Parameters
        ----------
        nums : List[int]
            The integer array.
        k : int
            Maximum allowed index distance.

        Returns
        -------
        bool
            True if there exist i != j with nums[i] == nums[j] and |i - j| <= k; else False.
        """
        if k <= 0:
            return False

        window = set()
        for i, x in enumerate(nums):
            if x in window:
                return True
            window.add(x)
            if len(window) > k:
                window.remove(nums[i - k])
        return False
