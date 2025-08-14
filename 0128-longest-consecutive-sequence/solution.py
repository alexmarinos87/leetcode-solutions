class Solution(object):
    def longestConsecutive(self, nums):
        """
        Longest Consecutive Sequence (LeetCode 128)

        Approach
        --------
        Hash set expansion (O(n)):
        - Insert all numbers into a set for O(1) average membership checks.
        - For each number that is a potential start of a run (x-1 not in set),
          walk forward x, x+1, x+2, ... counting the streak length.
        - Track the maximum streak length found.

        Parameters
        ----------
        nums : List[int]
            Unsorted list of integers (may contain duplicates).

        Returns
        -------
        int
            Length of the longest consecutive elements sequence.
        """
        if not nums:
            return 0

        s = set(nums)
        best = 0

        for x in s:  # iterate unique values
            if x - 1 not in s:  # start of a sequence
                length = 1
                y = x
                while y + 1 in s:
                    y += 1
                    length += 1
                if length > best:
                    best = length

        return best

