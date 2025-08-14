class Solution(object):
    def twoSum(self, nums, target):
        """
        Two Sum (LeetCode 1)

        Approach
        --------
        One-pass hash map (O(n)):
        - Keep a dict mapping value -> index for numbers we've seen.
        - For each number x at index i, compute complement c = target - x.
        - If c is already in the map, we found the pair and return its indices.
        - Otherwise store x -> i and continue.

        Parameters
        ----------
        nums : List[int]
            Input array of integers.
        target : int
            Target sum.

        Returns
        -------
        List[int]
            Indices [i, j] such that nums[i] + nums[j] == target.
        """
        seen = {}
        for i, x in enumerate(nums):
            c = target - x
            if c in seen:
                return [seen[c], i]
            seen[x] = i
        # Given constraints guarantee a solution; this line is never reached.
